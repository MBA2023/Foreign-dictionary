from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("home", views.main, name="home"),
    path("home/", views.main, name="home"),
    path("words_list", views.words_list, name="words_list"),
    path("words_list/", views.words_list, name="words_list"),
    path("add_word", views.add_word, name="add_word"),
    path("add_word/", views.add_word, name="add_word"),
    path("1", views.index, name="index"),
]