from django.contrib import admin
from .models import *

admin.site.register(TelegramProfile)
admin.site.register(TwitchProfile)
admin.site.register(Profile)
admin.site.register(VKGroup)
admin.site.register(VKProfile)