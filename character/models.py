from django.db import models

from adventure.models import Actor, ActorAction


class Character(Actor):
    # Ability scores
    char_strength = models.IntegerField(max_length=2)
    char_dexterity = models.IntegerField(max_length=2)
    char_constitution = models.IntegerField(max_length=2)
    char_intelligence = models.IntegerField(max_length=2)
    char_wisdom = models.IntegerField(max_length=2)
    char_charisma = models.IntegerField(max_length=2)

    # Proficiency Bonus
    char_prof = models.IntegerField(max_length=2)

    # Descriptive Values
    char_class = models.CharField(max_length=50)
    char_race = models.CharField(max_length=50)
    char_level = models.IntegerField(max_length=2)
    char_exp = models.IntegerField()

    ALIGNMENTS = (
        ('LG', 'Lawful Good'),
        ('NG', 'Neutral Good'),
        ('CG', 'Chaotic Good'),
        ('LN', 'Lawful Neutral'),
        ('TN', 'True Neutral'),
        ('CN', 'Chaotic Neutral'),
        ('LE', 'Lawful Evil'),
        ('NE', 'Neutral Evil'),
        ('CE', 'Chaotic Evil'),
    )
    char_alignments = models.CharField(max_length=2, choices=ALIGNMENTS)

    # Inventory
    char_inventory = models.ManyToManyField('InventoryItem')


class InventoryItem(models.Model):
    name = models.CharField(max_length=200)


class CharacterAttackAction(ActorAction):
    action = models.CharField(max_length=200)