# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiningHall',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(choices=[('Crossroads', 'Crossroads'), ('Clark Kerr', 'Clark Kerr'), ('Cafe 3', 'Cafe 3'), ('Foothill', 'Foothill')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('food_name', models.CharField(unique=True, max_length=255)),
                ('rating', models.IntegerField(null=True, blank=True)),
                ('time', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='dininghall',
            name='menu_items',
            field=models.ManyToManyField(to='food.MenuItem', blank=True),
        ),
    ]
