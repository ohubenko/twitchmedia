from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileListSerializer, ProfileCreateSerializer, ProfileSerializer


class ProfileListView(APIView):
    """Вывод списка пользователей"""

    def get(self, requset):
        profiles = Profile.objects
        serializer = ProfileListSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileView(APIView):
    """Вывод пользователя"""

    def get(self, requset, chat_id):
        try:
            profile = Profile.objects.get(tg_chat_id=chat_id)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response(status=404)


class ProfileCreateView(APIView):
    """Добавлениеь пользователя"""

    def post(self, requset):
        profile = ProfileCreateSerializer(data=requset.data)
        if profile.is_valid():
            profile.save()
        return Response(status=201)
