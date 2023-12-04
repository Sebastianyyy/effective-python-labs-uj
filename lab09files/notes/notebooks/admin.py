from django.contrib import admin

# Register your models here.
from mptt.admin import MPTTModelAdmin
from notebooks.models import Topic
from notebooks.models import Note

admin.site.register(Note)
@admin.register(Topic)
class TopicAdmin(MPTTModelAdmin):
    list_display = ['title', 'public']
    list_editable = ['public']