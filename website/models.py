from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class TwitchProfile(models.Model):
    name_twitch = models.TextField(unique=True, max_length=15, primary_key=True)
    url = models.URLField(unique=True)
    oidc_token = models.TextField(unique=True, max_length=128, default=None)

    # sub_list = Список подписок

    class Meta:
        verbose_name = "Twitch профиль"
        verbose_name_plural = "Twitch профили"
        # abstract = True


class VKProfile(models.Model):
    vk_tokken = models.TextField(unique=True, max_length=128)
    vk_page_URL = models.URLField(unique=True)
    # vk_group_list = Список групп
    # vk_streamer_group = Если стример то его группа
    vk_key_group = models.TextField(max_length=21)

    class Meta:
        verbose_name = "VK профиль"
        verbose_name_plural = "VK профили"
        # abstract = True


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)
    tg_chat_id = models.IntegerField("ID чата Telegram",
                                     unique=True)
    tg_name = models.TextField("Имя пользователя Telegram",
                               max_length=50)
    tg_auth_key = models.TextField(max_length=10, default=tg_chat_id)
    vk_profile = models.OneToOneField(VKProfile, on_delete=models.CASCADE, default=None)
    twitch_profile = models.OneToOneField(TwitchProfile, on_delete=models.CASCADE, default=None)

    # vk_list = #Добавить список групп на которые он подписан
    # subscribe_list=  Добавить список подписок

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Article(models.Model):
    title = models.TextField(max_length=120)
    text = models.TextField(max_length=500)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
