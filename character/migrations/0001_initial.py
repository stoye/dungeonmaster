# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('actor_ptr', models.OneToOneField(parent_link=True, primary_key=True, auto_created=True, to='adventure.Actor', serialize=False)),
                ('char_strength', models.IntegerField(max_length=2)),
                ('char_dexterity', models.IntegerField(max_length=2)),
                ('char_constitution', models.IntegerField(max_length=2)),
                ('char_intelligence', models.IntegerField(max_length=2)),
                ('char_wisdom', models.IntegerField(max_length=2)),
                ('char_charisma', models.IntegerField(max_length=2)),
                ('char_prof', models.IntegerField(max_length=2)),
                ('char_class', models.CharField(max_length=50)),
                ('char_race', models.CharField(max_length=50)),
                ('char_level', models.IntegerField(max_length=2)),
                ('char_exp', models.IntegerField()),
                ('char_alignments', models.CharField(choices=[('LG', 'Lawful Good'), ('NG', 'Neutral Good'), ('CG', 'Chaotic Good'), ('LN', 'Lawful Neutral'), ('TN', 'True Neutral'), ('CN', 'Chaotic Neutral'), ('LE', 'Lawful Evil'), ('NE', 'Neutral Evil'), ('CE', 'Chaotic Evil')], max_length=2)),
            ],
            bases=('adventure.actor',),
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='char_inventory',
            field=models.ManyToManyField(to='character.InventoryItem'),
        ),
    ]
