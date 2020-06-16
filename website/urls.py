from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("profiles/", views.ProfileListView.as_view()),
    path("profiles/<int:chat_id>/", views.ProfileView.as_view()),
    path("profiles/<int:chat_id>/subscribtions/", views.ProfileMakeSubscriptions.as_view()),

]
