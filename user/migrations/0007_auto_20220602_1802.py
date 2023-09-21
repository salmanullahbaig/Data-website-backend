# Generated by Django 3.1.5 on 2022-06-02 18:02

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20220525_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealUser',
            fields=[
            ],
            options={
                'verbose_name': '_Real User',
                'verbose_name_plural': '_Real Users',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserModerator',
            fields=[
            ],
            options={
                'verbose_name': '_User Moderator',
                'verbose_name_plural': '_User Moderators',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserStaff',
            fields=[
            ],
            options={
                'verbose_name': '_User Admin',
                'verbose_name_plural': '_User Admins',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserWorker',
            fields=[
            ],
            options={
                'verbose_name': '_Worker',
                'verbose_name_plural': '_Workers',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('user.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='userrole',
            name='role',
            field=models.CharField(choices=[('REGULAR', 'REGULAR'), ('CHATTER', 'CHATTER'), ('ADMIN', 'ADMIN'), ('SUPER_ADMIN', 'SUPER_ADMIN'), ('MODERATOR', 'MODERATOR')], default='REGULAR', max_length=20),
        ),
    ]
