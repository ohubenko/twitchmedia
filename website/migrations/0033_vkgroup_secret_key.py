# Generated by Django 3.0.7 on 2020-06-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0032_auto_20200615_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='vkgroup',
            name='secret_key',
            field=models.TextField(blank=True, verbose_name='Секретный ключ'),
        ),
    ]
