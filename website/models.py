from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tg_chat_id = models.PositiveIntegerField(max_length=20)
    tg_name = models.TextField(max_length=50)

    # subscribe_list=  Добавить список подписок

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
