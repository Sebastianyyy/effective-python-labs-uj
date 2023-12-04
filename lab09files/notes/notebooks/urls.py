from django.urls import re_path
from notebooks.views import *

app_name='notebooks'

urlpatterns = [
    re_path(r'^$', NoteListView.as_view(), name='note-list'),
    re_path(r'^(?P<pk>\d+)/$', NoteDetailView.as_view(), name='note-detail'),
    re_path(r'note/add/$', NoteCreate.as_view(), name='note-add'),
    re_path(r'note/(?P<pk>\d+)/$', NoteUpdate.as_view(), name='note-update'),
    re_path(r'note/(?P<pk>\d+)/delete/$', NoteDelete.as_view(), name='note-delete'),
    
    re_path(r'topic/$', TopicListView.as_view(), name='topic-list'),
    re_path(r'topic/(?P<pk>\d+)/$', TopicDetailView.as_view(), name='topic-detail'),
    re_path(r'topic/add/$', TopicCreate.as_view(), name='topic-add'),
    re_path(r'topic/(?P<pk>\d+)/update/$', TopicUpdate.as_view(), name='topic-update'),
    re_path(r'topic/(?P<pk>\d+)/delete/$', TopicDelete.as_view(), name='topic-delete'),


]