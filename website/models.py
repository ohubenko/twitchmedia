from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tg_chat_id = models.PositiveIntegerField("ID чата Telegram", max_length=20)
    tg_name = models.TextField("Имя пользователя Telegram", max_length=50)

    # subscribe_list=  Добавить список подписок


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
