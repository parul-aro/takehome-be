import os
from django.core.management import call_command
from django.test import TestCase
from api.models import House
from django.conf import settings
from django.test import override_settings

class ImportHouseDataCommandTest(TestCase):
    def test_import_command_creates_house(self):
        test_csv_path = os.path.join(settings.BASE_DIR, "api", "tests", "fixtures", "sample.csv")
        os.environ["CSV_PATH"] = test_csv_path

        call_command("import_house_data")

        house = House.objects.get(zillow_id=99999999)
        self.assertEqual(house.address, "123 Fake St")
        self.assertEqual(house.city, "Springfield")
        self.assertEqual(house.price, "500K")
        self.assertEqual(house.bathrooms, 2.0)
        self.assertEqual(house.bedrooms, 3)