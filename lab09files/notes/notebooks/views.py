from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Note,Topic

# Create your views here.


class NoteListView(ListView):
    model=Note
    
class NoteDetailView(DetailView):
    model=Note
    
class NoteCreate(LoginRequiredMixin,CreateView):
    model=Note
    fields=['title','body','topic']
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(NoteCreate, self).form_valid(form)
    
class NoteUpdate(UserPassesTestMixin,UpdateView):
    model=Note
    fields=['title','body']

    def test_func(self):
        return self.request.user == self.get_object().created_by or self.request.user.is_staff

class NoteDelete(UserPassesTestMixin,DeleteView):
    model=Note
    success_url=reverse_lazy('notebooks:note-list')
    
    def test_func(self):
        return self.request.user == self.get_object().created_by or self.request.user.is_staff

class TopicListView(ListView):
    model=Topic
    
class TopicDetailView(DetailView):
    model=Topic
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes']=self.get_topics()
        return context
    def get_topics(self):
        current_topic=self.object
        related_topics=Topic.objects.filter(parent=current_topic.parent)[:3]
        return related_topics
    
class TopicCreate(LoginRequiredMixin,CreateView):
    model=Topic
    fields=['title','parent','public']
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TopicCreate, self).form_valid(form)
    
class TopicUpdate(UserPassesTestMixin,UpdateView):
    model=Topic
    fields=['title','parent','public']

    def test_func(self):
        return self.request.user == self.get_object().created_by or self.request.user.is_staff

class TopicDelete(UserPassesTestMixin,DeleteView):
    model=Topic
    success_url=reverse_lazy('notebooks:topic-list')
    
    def test_func(self):
        return self.request.user == self.get_object().created_by or self.request.user.is_staff


