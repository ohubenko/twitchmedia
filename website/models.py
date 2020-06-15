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
    oidc_token = models.TextField(verbose_name="OIDC токен", blank=True, unique=True)

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
    vk_token = models.TextField(verbose_name="Токкен доступа", blank=True)
    url = models.URLField(verbose_name="URL ссылка на профиль")
    vk_groups = models.ManyToManyField(VKGroup, verbose_name="Группы VK", blank=True)

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

    def __str__(self):
        return self.tg_profile.name

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class Subscribe(models.Model):
    twitch_profile = models.OneToOneField(TwitchProfile, verbose_name="Twitch профиль", primary_key=True,
                                          on_delete=models.CASCADE)
    time_end_of_subs = models.DateTimeField(verbose_name="Конец подписки", blank=True, null=True)

    sub_list = models.ManyToManyField(Profile, verbose_name="Подписчики", related_name="Подписчики", blank=True)

    # Профиль

    def __str__(self):
        return "Подписка на " + self.twitch_profile.username

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
