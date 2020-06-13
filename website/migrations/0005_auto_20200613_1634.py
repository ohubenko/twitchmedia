# Generated by Django 3.0.7 on 2020-06-13 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200613_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='twitch_profile',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='website.TwitchProfile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='vk_profile',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='website.VKProfile'),
        ),
        migrations.AlterField(
            model_name='twitchprofile',
            name='oidc_token',
            field=models.TextField(blank=True, default=None, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='vkprofile',
            name='vk_key_group',
            field=models.TextField(blank=True, max_length=21),
        ),
    ]
