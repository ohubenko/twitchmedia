# Generated by Django 3.0.7 on 2020-06-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_auto_20200615_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='time_end_of_subs',
            field=models.DateTimeField(blank=True, verbose_name='Конец подписки'),
        ),
    ]