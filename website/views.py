from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileListSerializer, ProfileCreateSerializer


class ProfileListView(APIView):
    """Вывод списка пользователей"""

    def get(self, requset):
        profiles = Profile.objects
        serializer = ProfileListSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileCreateView(APIView):
    """Добавлениеь пользователя"""

    def post(self, requset):
        profile = ProfileCreateSerializer(data=requset.data)
        if profile.is_valid():
            profile.save()
        return Response(status=201)
