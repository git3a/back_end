# Generated by Django 2.2.2 on 2019-06-26 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.BigIntegerField()),
                ('recipeId', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100, unique=True)),
                ('pwd', models.CharField(max_length=100)),
                ('email', models.EmailField(default='@', max_length=254, unique=True)),
                ('touxiang', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.BigIntegerField()),
                ('recipeId', models.BigIntegerField()),
            ],
        ),
    ]
