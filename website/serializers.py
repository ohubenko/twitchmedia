from rest_framework import serializers

from .models import Profile


class ProfileListSerializer(serializers.ModelSerializer):
    """Список пользователей"""

    class Meta:
        model = Profile
        fields = ("tg_chat_id", "tg_name")


class ProfileSerializer(serializers.ModelSerializer):
    """Профиль"""

    class Meta:
        model = Profile
        fields = ("tg_chat_id",)


class ProfileCreateSerializer(serializers.ModelSerializer):
    """Добавление профиля"""

    class Meta:
        model = Profile
        fields = ("tg_chat_id", "tg_name")
