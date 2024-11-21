import os
import uuid

from rest_framework.exceptions import ValidationError

from better_profanity import profanity


class CarsService:

    @staticmethod
    def upload_car_photos(instance, file: str) -> str:
        ext = file.split('.')[-1]
        return os.path.join(str(instance.car.user.id), 'car_photo', f'{uuid.uuid1()}.{ext}')

    def validate_car_details(self, user, data):
        if user.account.account_type == 'Basic' and user.cars.count() >= 1:
            raise ValidationError({"detail": {"basic account can add only 1 car"}})

        for field in ['brand', 'model', 'color', 'region']:
            if profanity.contains_profanity(data.get(field, '')):
                from apps.listings.models import CarsModel
                car_instance = CarsModel.objects.filter(user=user, brand=data.get('brand', )).first()

                if car_instance is None:
                    car_instance = CarsModel(**data)

                car_instance.edit_attempts += 1
                car_instance.save()

                if car_instance.edit_attempts >= 3:
                    raise ValidationError({"detail": {"Maximum car edit attempts reached"}})

                raise ValidationError({"detail": {"Profanity detected in car details"}})
        return data
