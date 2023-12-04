from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.models import TitleSlugDescriptionModel,TimeStampedModel
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
# Create your models here.

    
class Topic(MPTTModel,TitleSlugDescriptionModel,TimeStampedModel):
    parent=TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    public=models.BooleanField(default=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('notebooks:topic-detail', kwargs={'pk': self.pk})

    
class Note(TimeStampedModel):
    title=models.CharField(max_length=256)
    body=models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    def get_absolute_url(self):
        return reverse('notebooks:note-detail', kwargs={'pk': self.pk})
    
    def __str__(self) -> str:
         return (self.title,self.body)
    
