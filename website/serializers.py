from rest_framework import serializers

from .models import Profile


class ProfileListSerializer(serializers.ModelSerializer):
    """Список пользователей"""

    class Meta:
        model = Profile
        fields = ("tg_chat_id", "tg_name")


class ProfileCreateSerializer(serializers.ModelSerializer):
    """Добавление профиля"""

    class Meta:
        model = Profile
        fields = ("tg_chat_id", "tg_name")

