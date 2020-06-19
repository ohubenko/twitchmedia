# Generated by Django 3.0.7 on 2020-06-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0033_vkgroup_secret_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitchprofile',
            name='discord_channel_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на канал в Discord'),
        ),
        migrations.AddField(
            model_name='twitchprofile',
            name='instagram_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на страницу в инстаграме'),
        ),
        migrations.AddField(
            model_name='twitchprofile',
            name='telegram_channel_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на канал в Telegram'),
        ),
        migrations.AddField(
            model_name='twitchprofile',
            name='vk_group_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на группу VK'),
        ),
        migrations.AddField(
            model_name='twitchprofile',
            name='vk_main_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на страницу VK'),
        ),
        migrations.AlterField(
            model_name='twitchprofile',
            name='message',
            field=models.TextField(blank=True, max_length=140, verbose_name='Текст уведомления'),
        ),
        migrations.AlterField(
            model_name='twitchprofile',
            name='url',
            field=models.URLField(blank=True, verbose_name='Ссылка на профиль Twitch'),
        ),
    ]
