from django.contrib.auth.models import User
from django.db import models


class TelegramProfile(models.Model):
    chat_id = models.IntegerField(verbose_name="ID чата с ботом", unique=True, primary_key=True)
    username = models.TextField(verbose_name="Имя пользователя")
    name = models.TextField(verbose_name="Имя")

    def __str__(self):
        return self.name + ":" + str(self.chat_id)

    class Meta:
        verbose_name = "Профиль Telegram"
        verbose_name_plural = "Профили Telegram"


class TwitchProfile(models.Model):
    username = models.TextField(max_length=15, verbose_name="Имя пользователя", primary_key=True, unique=True)
    url = models.URLField(verbose_name="Ссылка на профиль Twitch", default="https://twitch.tv/" + str(username),
                          blank=True)
    message = models.TextField(max_length=140, verbose_name="Текст уведомления",
                               default="Пользователь " + str(username) + " начал прямую трансляцию.\n Заходи " + str(
                                   url),
                               blank=True)
    oidc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Профиль Twitch"
        verbose_name_plural = "Профили Twitch"


class VKGroup(models.Model):
    id = models.SmallIntegerField(verbose_name="ID Группы", primary_key=True)
    name = models.TextField(verbose_name="Название группы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа VK"
        verbose_name_plural = "Группы VK"


class VKProfile(models.Model):
    name = models.TextField(verbose_name="Имя")
    token = models.TextField(verbose_name="Токкен доступа", blank=True)
    url = models.URLField(verbose_name="URL ссылка на профиль")
    groups = models.ManyToManyField(VKGroup, verbose_name="Группы VK", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Профиль VK"
        verbose_name_plural = "Профили VK"


class Profile(models.Model):
    tg_profile = models.OneToOneField(TelegramProfile, on_delete=models.CASCADE, verbose_name="Профиль Telegram",
                                      blank=True)
    vk_profile = models.OneToOneField(VKProfile, on_delete=models.CASCADE, verbose_name="Профиль VK", blank=True,
                                      null=True)
    twitch_profile = models.OneToOneField(TwitchProfile, on_delete=models.CASCADE, verbose_name="Профиль Twitch",
                                          blank=True, null=True)
    subscriptions = models.ManyToManyField(TwitchProfile, verbose_name="Подписки", related_name="subscriptions",
                                           blank=True)

    def __str__(self):
        return self.tg_profile.name + ":" + str(self.tg_profile.chat_id)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
