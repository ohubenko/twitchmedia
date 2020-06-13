from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tg_chat_id = models.IntegerField("ID чата Telegram")
    tg_name = models.TextField("Имя пользователя Telegram", max_length=50)

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
