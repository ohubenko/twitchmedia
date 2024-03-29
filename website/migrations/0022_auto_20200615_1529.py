# Generated by Django 3.0.7 on 2020-06-15 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_auto_20200615_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='sub_list',
            field=models.ManyToManyField(blank=True, null=True, related_name='Подписчики', to='website.Profile', verbose_name='Подписчики'),
        ),
        migrations.AlterField(
            model_name='twitchprofile',
            name='url',
            field=models.URLField(blank=True, default='https://twitch.tv/<django.db.models.fields.TextField>', verbose_name='Ссылка на профиль Twitch'),
        ),
    ]
