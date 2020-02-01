from django.db import models
from django.utils.translation import gettext_lazy as _

class NOC(models.Model):
    """docstring for NOC"""
    noc = models.CharField(
        max_length=3,
        verbose_name=_('National Olympic Committee'),
        help_text=_('National Olympic Committee 3 letter code') 
        )
    region = models.CharField(
        max_length=100,
        verbose_name=_('Country name'),
        help_text=_("Country that the NOC represents")
        )
    notes = models.CharField(
        max_length=255,
        verbose_name=_('Notes'),
        help_text=_('Notes about the NOC')
        )

class Athlete(models.Model):
    """docstring for Athlete"""
    name = models.CharField(
        max_length=255,
        verbose_name=_('Athlete name'),
        help_text=_('Name of the Athlete'),
        )
    sex = models.CharField(
        max_length=1,
        verbose_name=_('Athlete sex'),
        help_text=_('Sex of the athlete')
        )
    age = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_('Athlete age'),
        help_text=_('Age of the athlete'),
        )
    height = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_('Athlete height'),
        help_text=_('Height of the athlete'),
        )
    weight = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_('Athlete weight'),
        help_text=_('Weight of the athlete'),
        )
    noc = models.ForeignKey(
        NOC,
        verbose_name=_('National Olympic Committee'),
        help_text=_('National Olympic Committee 3 letter code'),
        on_delete=models.CASCADE
        )
class Olympics(models.Model):
    """Games,Year and Season"""
    name = models.CharField(
        max_length=255,
        verbose_name=_('Games name'),
        help_text=_('Name of the Olympics'),
        )
    year = models.IntegerField(
        null=False,
        blank=False,
        verbose_name=_('Year'),
        help_text=_('Year that the Olympics happened'),
        )
    Season = models.CharField(
        max_length=6,
        verbose_name=_('Season'),
        help_text=_('Season that the Olympics happened'),
        )


class Sport(models.Model):
    """Sport"""
    name = models.CharField(
        max_length=255,
        verbose_name=_('Sport name'),
        help_text=_('Name of the sport'),
        )

class Event(models.Model):
    """Event"""
    name = models.CharField(
        max_length=255,
        verbose_name=_('Event name'),
        help_text=_('Name of the event'),
        )
    sport = models.ForeignKey(
        Sport,
        verbose_name=_('Sport'),
        help_text=_('Sport of this event'),
        on_delete=models.CASCADE
        )


class City(models.Model):
    """City"""
    name = models.CharField(
        max_length=255,
        verbose_name=_('City name'),
        help_text=_('Name of the city')
        )

class Participation(models.Model):
    """Medals,Team"""
    medal = models.CharField(
        max_length=10,
        verbose_name=_('Medal received'),
        help_text=_('Medal that the participant received'),
        )
    team = models.CharField(
        max_length=255,
        verbose_name=_('Team name'),
        help_text=_('Team of the participant'),
        )
    city = models.ForeignKey(
        City,
        verbose_name=_('City'),
        help_text=_('City that the event happened'),
        on_delete=models.CASCADE
        )
    event = models.ForeignKey(
        Event,
        verbose_name=_('Event'),
        help_text=_('Event that the athlete participated'),
        on_delete=models.CASCADE
        )
    olympic = models.ForeignKey(
        Olympics,
        verbose_name=_('Olympics'),
        help_text=_('Olympics related to the participation'),
        on_delete=models.CASCADE
        )



