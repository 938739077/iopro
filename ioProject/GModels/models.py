from django.db import models
from GModels import heroConfigure
# Create your models here.


class HeroManager(models.Manager):
    def get_queryset(self):
        return super(HeroManager, self).get_queryset().filter(_is_delete=True)


class BaseHero(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=16, blank=False)
    vitality = models.BigIntegerField(default=heroConfigure.HERO_BASE_ATTRIBUTES["vitality"])
    speed = models.IntegerField(default=heroConfigure.HERO_BASE_ATTRIBUTES["speed"])
    magic_power = models.IntegerField(default=heroConfigure.HERO_BASE_ATTRIBUTES["magic_power"])
    physical_power = models.IntegerField(default=heroConfigure.HERO_BASE_ATTRIBUTES["physical_power"])
    magic_defensive_power = models.IntegerField(default=heroConfigure.HERO_BASE_ATTRIBUTES["magic_defensive_power"])
    physical_defensive_power = models.IntegerField(default=heroConfigure.HERO_BASE_ATTRIBUTES["physical_defensive_power"])
    start = models.IntegerField(default=heroConfigure.HERO_BASE_ATTRIBUTES["start"])
    is_delete = models.BooleanField(default=False)

    objects = HeroManager()

    def create_hero(self, name="", vitality=None, speed=None, magic_power=None,
                    physical_power=None, magic_defensive_power=None, physical_defensive_power=None,
                    start=None):
        self.name = name
        self.vitality = vitality
        self.speed = speed
        self.magic_power = magic_power
        self.physical_power = physical_power
        self.magic_defensive_power = magic_defensive_power
        self.physical_defensive_power = physical_defensive_power
        self.start = start

    class Meta:
        managed = False
        ordering = ["id"]


class DemonClanHero(BaseHero):
    pass
