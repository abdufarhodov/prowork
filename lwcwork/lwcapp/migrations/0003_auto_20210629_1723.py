# Generated by Django 3.2.4 on 2021-06-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lwcapp', '0002_auto_20210629_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='hashtag',
        ),
        migrations.AddField(
            model_name='blog',
            name='hashtag',
            field=models.ManyToManyField(to='lwcapp.Hashtags'),
        ),
    ]
