# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t411', '0002_auto_20160403_0137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=15)),
                ('lien', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='historique',
            name='profil',
        ),
        migrations.RemoveField(
            model_name='historique',
            name='torrent',
        ),
        migrations.RemoveField(
            model_name='profil',
            name='torrents',
        ),
        migrations.DeleteModel(
            name='Historique',
        ),
        migrations.DeleteModel(
            name='Torrent',
        ),
        migrations.AddField(
            model_name='profil',
            name='menus',
            field=models.ManyToManyField(to='t411.Menu'),
        ),
    ]
