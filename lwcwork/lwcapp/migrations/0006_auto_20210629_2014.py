# Generated by Django 3.2.4 on 2021-06-29 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lwcapp', '0005_rename_key_hashtags_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='hashtags',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hashtags',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='regions',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]