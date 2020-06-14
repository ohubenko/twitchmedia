from django.contrib import admin
from .models import TelegramProfile, TwitchProfile, VKGroup, VKProfile, Subscribe, Profile

admin.site.register(Profile)
admin.site.register(TelegramProfile)
admin.site.register(TwitchProfile)
admin.site.register(VKGroup)
admin.site.register(VKProfile)
admin.site.register(Subscribe)
