from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("profiles/", views.ProfileListView.as_view()),
    path("profiles/create/", views.ProfileCreateView.as_view()),
    path("profiles/<int:chat_id>/", views.ProfileView.as_view()),
    path("profiles/<int:chat_id>/subscriptions/", views.ProfileMakeSubscriptions.as_view()),
    path("profiles/twitch/<str:streamer>/webhook/", views.TwitchWebHookSubscriptions.as_view())
]
