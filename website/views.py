from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class ProfileListView(APIView):
    """Список пользователей"""

    def get(self, request):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)


class TelegramProfileListView(APIView):
    """Список профилей телеграм"""

    def get(self, request):
        tgp = TelegramProfile.objects.all()
        serializer = TelegramProfileSerializer(tgp, many=True)
        return Response(serializer.data)


class TwitchProfileListView(APIView):
    """Список профилей Twitch"""

    def get(self, request):
        twp = TwitchProfile.objects.all()
        serializer = TwitchProfileSerializer(twp, many=True)
        return Response(serializer.data)


class TelegramProfileCreateView(APIView):
    """Создание профиля Telegram"""

    def post(self, request):
        # TODO: С запроса вытянуть chat_id,name,username
        return Response(status=201)


class ProfileCreateView(APIView):
    """Создание профиля"""

    def post(self, request):
        # TODO: С запроса вытянуть данные для создания профиля
        tg, ctg = TelegramProfile.objects.get_or_create(
            chat_id=request.data.get("chat_id"),
            username=request.data.get("username"),
            name=request.data.get("name"),
        )
        profile, cp = Profile.objects.get_or_create(tg_profile=tg)
        if ctg and cp:
            return Response(status=201)
        else:
            return Response(status=403)


class ProfileView(APIView):
    """Информация о пользователе"""

    def get(self, request, chat_id):
        try:
            profile = Profile.objects.get(tg_profile=TelegramProfile.objects.get(chat_id=chat_id))
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist or TelegramProfile.DoesNotExist:
            return Response(status=404)


class ProfileMakeSubscriptions(APIView):
    """Подписки пользователя"""

    def post(self, request, chat_id):
        try:
            profile = Profile.objects.get(tg_profile=TelegramProfile.objects.get(chat_id=chat_id))
            name_streamer = request.data.get("streamer")
            twitch_profile, created = TwitchProfile.objects.get_or_create(username=name_streamer)
            if created:
                # TODO: Запрос на twitch с созданием подписки
                print("Создан профиль Twitch")
            profile.subscriptions.add(twitch_profile)
            return Response(status=201)
        except Profile.DoesNotExist or TelegramProfile.DoesNotExist:
            return Response(status=404)

    def get(self, request, chat_id):
        try:
            profile = Profile.objects.get(tg_profile=TelegramProfile.objects.get(chat_id=chat_id))
            serializer = ProfileSerializer(profile)
            return Response(serializer.data.get("subscriptions"))
        except Profile.DoesNotExist or TelegramProfile.DoesNotExist:
            return Response(status=404)
