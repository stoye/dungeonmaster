from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    actions = models.ManyToManyField('ActorAction')


class ActorAction(models.Model):
    name = models.CharField(max_length=200)

    ACTION_TYPES = (
        ('S', 'Spell'),
        ('A', 'Attack'),
    )
    action_type = models.CharField(max_length=1, choices=ACTION_TYPES)


