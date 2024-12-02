from django.test import TestCase

from apps.all_cars.dropout_cars.models import BrandsModel, ModelCar


class BrandsModelTestCase(TestCase):
    def setUp(self):
        self.brand = BrandsModel.objects.create(title="Toyota")

    def test_brand_creation(self):
        """Перевіряємо створення бренду."""
        self.assertEqual(self.brand.title, "Toyota")
        self.assertTrue(BrandsModel.objects.filter(title="Toyota").exists())

    def test_brand_string_representation(self):
        """Перевіряємо метод __str__."""
        self.assertEqual(str(self.brand), "Toyota")


class ModelCarTestCase(TestCase):
    def setUp(self):
        self.brand = BrandsModel.objects.create(title="Honda")
        self.model_car = ModelCar.objects.create(model_car="Civic", brand=self.brand)

    def test_model_car_creation(self):
        """Перевіряємо створення моделі автомобіля."""
        self.assertEqual(self.model_car.model_car, "Civic")
        self.assertEqual(self.model_car.brand, self.brand)

    def test_model_car_string_representation(self):
        """Перевіряємо метод __str__."""
        self.assertEqual(str(self.model_car), "Civic")

    def test_model_car_related_to_brand(self):
        """Перевіряємо, чи модель автомобіля прив'язана до бренду."""
        self.assertEqual(self.brand.car_models.count(), 1)
        self.assertEqual(self.brand.car_models.first(), self.model_car)
