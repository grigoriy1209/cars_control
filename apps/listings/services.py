import os
import re
import uuid

from rest_framework.exceptions import ValidationError


class CarsService:
    @staticmethod
    def upload_car_photos(instance, file: str) -> str:
        ext = file.split('.')[-1]
        return os.path.join(str(instance.car.user.id), 'car_photo', f'{uuid.uuid1()}.{ext}')

    @staticmethod
    def account_limit(user, data):
        if user.account.account_type == 'Basic' and user.cars.count() >= 1:
            raise ValidationError({"detail": {"basic account can add only 1 car"}})

    @staticmethod
    def validate_foul(description):
        foul_words = ['fuck', 'Fucking']
        for word in foul_words:
            if word.lower() in description.lower():
                raise ValidationError({"detail": {"foul words can not"}})
        return description

    @staticmethod
    def count_attempts(car):
        max_attempts = 3
        if car.edit_attempts >= max_attempts:
            # car.status = 'inactive'
            # car.save()
            raise ValidationError({"detail": {"attempts exceeds max attempts"}})
        # else:
        car.edit_attempts += 1
        car.save()

