from django.db import models

from rest_framework.exceptions import ValidationError

from better_profanity import profanity


class CarManager(models.Manager):
    def _validate_words(self, data):
        fields_valid = ['brand', 'model', 'region','color']
        for field in fields_valid:
            if field in data and profanity.contains_profanity(data[field]):
                raise ValidationError({"detail": "You words incorrect, please change"})

    def create(self, **kwargs):
        self._validate_words(kwargs)
        return super().create(**kwargs)

    def update_car(self, instance, **kwargs):
        self._validate_words(kwargs)

        instance.edit_attemps += 1
        if kwargs:
            instance.edit_count += 1
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance

