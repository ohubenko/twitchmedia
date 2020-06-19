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


class TelegramProfileAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramProfile
        fields = ("chat_id",)


class ProfileAlertSerializer(serializers.ModelSerializer):
    tg_profile = TelegramProfileAlertSerializer()

    class Meta:
        model = Profile
        fields = ("tg_profile",)


class TwitchProfileAlertSerializer(serializers.ModelSerializer):
    subscriptions = ProfileAlertSerializer(many=True)

    class Meta:
        model = TwitchProfile
        fields = ("username", "message", "subscriptions")


class TwitchSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitchProfile
        fields = ("url", "instagram_url", "vk_group_url", "vk_main_url", "telegram_channel_url")
