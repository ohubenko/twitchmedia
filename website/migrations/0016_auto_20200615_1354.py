# Generated by Django 3.0.7 on 2020-06-15 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_auto_20200615_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='twitch_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='website.TwitchProfile', verbose_name='Twitch профиль'),
        ),
    ]
