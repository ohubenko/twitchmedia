from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tg_chat_id = models.PositiveIntegerField("ID чата Telegram", max_length=20)
    tg_name = models.TextField("Имя пользователя Telegram", max_length=50)

    # subscribe_list=  Добавить список подписок

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
