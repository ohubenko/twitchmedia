
from django.contrib import admin
from .models import Profile, Article, TwitchProfile, VKProfile

admin.site.register(Profile)
admin.site.register(Article)
admin.site.register(TwitchProfile)
admin.site.register(VKProfile)
