# Generated by Django 4.0 on 2022-11-11 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Football',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True, verbose_name='Заголовок')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='football')),
                ('url', models.SlugField(default='', max_length=130, unique=True)),
            ],
            options={
                'verbose_name': 'Футбол',
                'verbose_name_plural': 'Футбол',
            },
        ),
        migrations.CreateModel(
            name='MinyFootball',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True, verbose_name='Заголовок')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='miny_football')),
                ('slug', models.SlugField(default='', max_length=130, unique=True)),
            ],
            options={
                'verbose_name': 'Мини-футбол',
                'verbose_name_plural': 'Мини-футбол',
            },
        ),
    ]
