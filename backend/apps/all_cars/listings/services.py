import os
import uuid

from rest_framework.exceptions import ValidationError

from apps.all_cars.listings.choices.status_choice import StatusChoice


class CarsService:
    @staticmethod
    def upload_car_photos(instance, file: str) -> str:
        ext = file.split('.')[-1]
        return os.path.join(str(instance.car.user.id), 'car_photo', f'{uuid.uuid1()}.{ext}')

    @staticmethod
    def account_limit(user, data):
        if user.account.account_type == 'Basic' and user.cars.count() >= 1:
            raise ValidationError({"detail": {"basic account can add only 1 car"}})

    # @staticmethod
    # def validate_foul(description):
    #     foul_words = ['fuck', 'Fucking']
    #     for word in foul_words:
    #         if word.lower() in description.lower():
    #             raise ValidationError(
    #                 {"detail": {"The mask is saved, but you need to edit it, otherwise the manager will delete it"}})
    #     return description

    @staticmethod
    def counter_edit_attempts(car):
        if car.validate_foul():
            car.edit_attempts += 1
            if car.edit_attempts >= 3:
                car.status = StatusChoice.INACTIVE
        else:
            car.status = StatusChoice.ACTIVE
            car.edit_attempts = 0
        car.save()

    # @staticmethod
    # def edit_car(car, new_description: str):
    #     car.description = new_description
    #     CarsService.counter_edit_attempts(car)

    @staticmethod
    def increment_view(car):
        car.views += 1
        car.save(update_fields=['views'])
