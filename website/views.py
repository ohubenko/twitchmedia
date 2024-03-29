import os
import time
from threading import Thread

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .models import Profile, TelegramProfile, TwitchProfile
from .serializers import ProfileSerializer, TelegramProfileSerializer, TwitchProfileSerializer, \
    TwitchProfileAlertSerializer, TwitchSocialSerializer
import requests


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
            tg_profile = TelegramProfile.objects.get(chat_id=chat_id)
            profile = Profile.objects.get(tg_profile=tg_profile)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except TelegramProfile.DoesNotExist or Profile.DoesNotExist:
            return Response(status=404)

    def post(self, request, chat_id):
        try:
            tg_profile = TelegramProfile.objects.get(chat_id=chat_id)
            profile = Profile.objects.get(tg_profile=tg_profile)
            streamer = request.data.get('streamer')
            tw_profile = TwitchProfile.objects.get(username=streamer)
            profile.subscriptions.remove(tw_profile)
            return Response(status=201)
        except TelegramProfile.DoesNotExist or Profile.DoesNotExist or TwitchProfile.DoesNotExist:
            return Response(status=404)

    def delete(self, request, chat_id):
        try:
            tg_profile = TelegramProfile.objects.get(chat_id=chat_id)
            profile = Profile.objects.get(tg_profile=tg_profile)
            tg_profile.delete()
            return Response(status=204)
        except TelegramProfile.DoesNotExist or Profile.DoesNotExist:
            return Response(status=404)


class ProfileMakeSubscriptions(APIView):
    """Подписки пользователя"""

    def post(self, request, chat_id):
        try:
            profile = Profile.objects.get(tg_profile=TelegramProfile.objects.get(chat_id=chat_id))
            name_streamer = request.data.get("streamer")
            twitch_profile, created = TwitchProfile.objects.get_or_create(username=name_streamer)
            if created:
                headers = {
                    'Client-ID': str(os.environ.get('client_id')),
                    'Authorization': "Bearer " + str(os.environ.get('twitch_bearer'))
                }
                r_id = requests.get("https://api.twitch.tv/helix/users?login=" + name_streamer,
                                    headers=headers)
                streamer_id = r_id.json().get("data")[0].get("id")
                print(streamer_id)
                print(r_id.status_code)
                payload = {
                    'hub.callback': 'https://twitch-media.me/api/v1/profiles/twitch/' + str(
                        name_streamer) + '/webhook/',
                    'hub.mode': 'subscribe',
                    'hub.topic': 'https://api.twitch.tv/helix/streams?user_id=' + str(streamer_id),
                    'hub.lease_seconds': 864000}
                url = "https://api.twitch.tv/helix/webhooks/hub"
                r_p = requests.post(url, headers=headers, data=payload)
                print(r_p.status_code)
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


def alert_bot(twitch_profile):
    time.sleep(1)
    print("Отправка имени стримера боту")
    print(requests.post("https://twitchmediabot.herokuapp.com/twitch_alert",
                        data={"streamer": str(twitch_profile.username)}).status_code)


class TwitchWebHookSubscriptions(APIView):
    """Установка WebHook Twitch"""
    def get(self, request, streamer):
        try:
            tp = TwitchProfile.objects.get(username=streamer)
            content = str(request.GET['hub.challenge'])
            return HttpResponse(content, content_type="text/plain", status=200, )
        except TelegramProfile.DoesNotExist:
            return Response(status=404)

    def post(self, request, streamer):
        try:
            print(str(request.data))
            if request.data == "":
                print("Стрим окончен")
            else:
                print("Изминение статуса стрима " + str(streamer))
                twitch_profile = TwitchProfile.objects.get(username=streamer)
                thread = Thread(target=alert_bot(twitch_profile))
                thread.start()
                return Response(status=200)
        except TwitchProfile.DoesNotExist:
            return Response(status=404)


class TwitchProfileView(APIView):
    """Список подписаных пользователей"""
    def get(self, request, streamer):
        try:
            tp = TwitchProfile.objects.get(username=streamer)
            serializer = TwitchProfileAlertSerializer(tp)
            return Response(serializer.data)
        except TwitchProfile.DoesNotExist:
            return Response(status=404)


class TwitchSocialView(APIView):
    """Список ссылок на соц. сети стримера"""
    def get(self, request, streamer):
        try:
            tw = TwitchProfile.objects.get(username=streamer)
            serializer = TwitchSocialSerializer(tw)
            return Response(serializer.data)
        except TwitchProfile.DoesNotExist:
            return Response(status=404)
