from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("profile/", views.ProfileListView.as_view()),
    path("profile/create/", views.ProfileCreateView.as_view()),
]
