# Generated by Django 3.0.7 on 2020-06-15 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_auto_20200615_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='sub_list',
            field=models.ManyToManyField(blank=True, related_name='Подписчики', to='website.Profile', verbose_name='Подписчики'),
        ),
    ]
