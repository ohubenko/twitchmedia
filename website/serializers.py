from rest_framework import serializers

from .models import Profile


class ProfileListSerializer(serializers.ModelSerializer):
    """Список пользователей"""

    class Meta:
        model = Profile
        fields = ("tg_chat_id", "tg_name",)


class ProfileSerializer(serializers.ModelSerializer):
    """Профиль"""

    class Meta:
        model = Profile
        fields = ("tg_chat_id", "subscribe_list")


class ProfileCreateSerializer(serializers.ModelSerializer):
    """Добавление профиля"""

    class Meta:
        model = Profile
        fields = ("tg_chat_id", "tg_name",)


class ProfileSubscribeSerializer(serializers.ModelSerializer):
    """Добавление подписки"""

    class Meta:
        model = Profile
        fields = ("tg_chat_id", "subscribe_list",)

    def create(self, validated_data):
        sub_lit = Profile.objects.update_or_create(
            subscribe_list=validated_data.get('subscribe_list', None),
            tg_chat_id=validated_data.get('tg_chat_id', None),
            defaults={'subscribe_list': validated_data.get('subscribe_list')},
        )
        return sub_lit
