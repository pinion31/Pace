# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-27 01:30
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Sit-ups', 'Sit-ups'), ('Running', 'Running'), ('Walking', 'Walking'), ('Weight-lifting', 'Weight-lifting'), ('Push-ups', 'Push-ups'), ('Choose Activity', 'Choose Activity')], default='Choose Activity', max_length=256)),
                ('activity_type', models.CharField(max_length=256)),
                ('hours', models.PositiveIntegerField(default=0)),
                ('minutes', models.PositiveIntegerField(default=0)),
                ('reps', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PaceUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_length', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pace.Session'),
        ),
    ]
