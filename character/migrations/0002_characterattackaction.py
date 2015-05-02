# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterAttackAction',
            fields=[
                ('actoraction_ptr', models.OneToOneField(to='adventure.ActorAction', serialize=False, primary_key=True, parent_link=True, auto_created=True)),
                ('action', models.CharField(max_length=200)),
            ],
            bases=('adventure.actoraction',),
        ),
    ]
