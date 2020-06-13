# Generated by Django 3.0.7 on 2020-06-13 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200613_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitchProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_twitch', models.TextField(blank=True, max_length=15, unique=True)),
                ('url', models.URLField(blank=True, unique=True)),
                ('oidc_token', models.TextField(blank=True, default=None, max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'Twitch профиль',
                'verbose_name_plural': 'Twitch профили',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='subscribe_list',
            field=models.ManyToManyField(to='website.TwitchProfile', verbose_name='Список подписок'),
        ),
    ]
