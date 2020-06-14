from django.contrib import admin
from .models import TelegramProfile, TwitchProfile, VKGroup, VKProfile, Subscribe, Profile

admin.register(Profile)
admin.register(TelegramProfile)
admin.register(TwitchProfile)
admin.register(VKGroup)
admin.register(VKProfile)
admin.register(Subscribe)
