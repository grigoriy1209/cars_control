from decimal import Decimal

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.all_cars.dropout_cars.models import BrandsModel, ModelCar
from apps.all_cars.listings.choices.body_type_choice import BodyTypeChoice
from apps.all_cars.listings.choices.eco_choice import EcologicalStandardTypeChoice
from apps.all_cars.listings.choices.engine_choice import EngineTypeChoice
from apps.all_cars.listings.choices.status_choice import StatusChoice
from apps.all_cars.listings.choices.transmission_choice import CheckpointTypeChoice
from apps.all_cars.listings.models import CarsModel
from apps.all_users.users.models import UserModel
from apps.payments.currency_choice import CurrencyChoice
from apps.payments.models import ExchangeRatesModel


class CarApiTest(APITestCase):

    def setUp(self):
        # Створюємо бренд
        self.brand = BrandsModel.objects.create(title="lada")

        # Створюємо модель автомобіля з посиланням на бренд
        self.model_car = ModelCar.objects.create(model_car="A4", brand=self.brand)

        # Створюємо користувача
        self.user = UserModel.objects.create_user(email="testuser@example.com", password="testpassword123")

        # Створюємо курс обміну валют
        self.exchange_rate = ExchangeRatesModel.objects.create(
            usd_to_uah=Decimal("36.5"),
            eur_to_uah=Decimal("38.5"),
            usd_to_eur=Decimal("1.05")
        )

        self.car1 = CarsModel.objects.create(
            brand=self.brand,
            model=self.model_car,
            user=self.user,
            year=2000,
            mileage=23333,
            user_price=2444,
            currency=CurrencyChoice.EUR,
            exchange_rates=self.exchange_rate,
            eco_standard=EcologicalStandardTypeChoice.EVRO_1,
            region="Jitomir",
            body_type=BodyTypeChoice.SPORT_CAR,
            engine=EngineTypeChoice.V_TYPE,
            checkpoint=CheckpointTypeChoice.ROBOT,
            color="red",
            status=StatusChoice.ACTIVE,
            description="asasac",
        )

        self.car2 = CarsModel.objects.create(
            brand=self.brand,
            model=self.model_car,
            user=self.user,
            year=2000,
            mileage=23333,
            user_price=2444,
            currency=CurrencyChoice.USD,
            exchange_rates=self.exchange_rate,
            eco_standard=EcologicalStandardTypeChoice.EVRO_1,
            region="Jitomir",
            body_type=BodyTypeChoice.SPORT_CAR,
            engine=EngineTypeChoice.V_TYPE,
            checkpoint=CheckpointTypeChoice.ROBOT,
            color="red",
            status=StatusChoice.ACTIVE,
            description="asasac",
        )

        # Авторизація
        self.client.login(email="testuser@example.com", password="testpassword123")

    def test_get_all_cars(self):
        res = self.client.get(reverse('car_create_list'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        data = res.data
        self.assertEqual(len(data), 2)
        CarsModel.objects.get(pk=self.car1.id)
        self.assertEqual(CarsModel.objects.get(pk=self.car1.id).model, 'lada')
        CarsModel.objects.get(pk=self.car2.id)
        self.assertEqual(CarsModel.objects.get(pk=self.car2.id).model, 'lada')
        CarsModel.objects.get(pk=self.car1.id)

    def test_get_all_cars(self):
        res = self.client.post(reverse('car_list_create'))
        print(res)
