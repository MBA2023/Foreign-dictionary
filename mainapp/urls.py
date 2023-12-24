from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("home", views.main, name="home"),
    path("home/", views.main, name="home"),
    path("words_list", views.main, name="words_list"),
    path("words_list/", views.main, name="words_list"),
    path("add_word", views.main, name="add_word"),
    path("add_word/", views.main, name="add_word"),
]