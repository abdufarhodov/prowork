# Generated by Django 3.2.4 on 2021-06-29 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lwcapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_global',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='is_local',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
