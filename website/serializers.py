from rest_framework import serializers

from .models import *


class TelegramProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramProfile
        fields = ("chat_id", "username", "name")


class TwitchProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitchProfile
        fields = ("username", "message")


class TwitchNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitchProfile
        fields = ("username",)


class ProfileSerializer(serializers.ModelSerializer):
    tg_profile = TelegramProfileSerializer()
    twitch_profile = TwitchProfileSerializer()
    subscriptions = TwitchNameSerializer(many=True)

    class Meta:
        model = Profile
        exclude = ("vk_profile",)
