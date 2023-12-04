from django.urls import re_path
from notebooks.views import NoteListView,NoteDetailView,NoteCreate,NoteUpdate,NoteDelete
from . import views

app_name='account'

urlpatterns = [
    re_path(r"^register", views.register_request, name="register"),
    re_path(r"^login", views.login_request, name="login"),
    re_path(r"^logout", views.logout_request, name= "logout"),
    re_path(r"", views.homepage, name= "homepage"),

]