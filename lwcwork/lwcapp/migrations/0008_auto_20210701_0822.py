# Generated by Django 3.2.4 on 2021-07-01 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lwcapp', '0007_alter_blog_is_global'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='is_global',
        ),
        migrations.AlterField(
            model_name='blog',
            name='is_local',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
