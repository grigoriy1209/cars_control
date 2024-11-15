from django.db import models


class CurrencyChoice(models.TextChoices):
    USD = 'USD',
    EUR = 'EUR',
    UAH = 'UAH',


class StatusChoice(models.TextChoices):
    ACTIVE = 'active',
    INACTIVE = 'inactive',
    PENDING = 'pending',
    EDIT_REQUIRED = 'edit_required',


class BodyTypeChoice(models.TextChoices):
    SEDAN = 'sedan',
    HATCHBACK = 'hatchback',
    SUV = 'suv',
    CROSSOVER = 'crossover',
    COUPE = 'coupe',
    CONVERTIBLE = 'convertible',
    WAGON = 'wagon',
    PICKUP = 'pickup',
    MINIVAN = 'minivan',
    VAN = 'van',
    ROADSTER = 'roadster',
    LUXURY_CAR = 'luxury car',
    SPORT_CAR = 'sport car',


class EngineTypeChoice(models.TextChoices):
    INLINE = 'inline',
    V_TYPE = 'v-type',
    FLAT = 'flat',
    ROTARY = 'rotary',
    ELECTRIC = 'electric',
    HYBRID = 'hybrid',
    DIESEL = 'diesel',
    TURBOCHARGED = 'turbocharged',
    SUPERCHARGED = 'supercharged',
    W_TYPE = 'w-type',


class EcologicalStandardTypeChoice(models.TextChoices):
    EVRO_6 = 'evro-6',
    EVRO_5 = "evro-5",
    EVRO_4 = "evro-4",
    EVRO_3 = "evro-3",
    EVRO_2 = "evro-2",
    EVRO_1 = "evro-1",


class CheckpointTypeChoice(models.TextChoices):
    MANUAL = 'manual',
    AUTOMATIC = 'automatic',
    TIPTRONIC = 'tiptronic',
    ROBOT = 'robot',
    VARIATOR = 'variator'
