from django.db import models


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