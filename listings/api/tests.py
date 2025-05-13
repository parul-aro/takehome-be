from django.test import TestCase
from rest_framework.test import APIClient
from .models import House

class HouseTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_house(self):
        response = self.client.post("/api/houses/", {
            "address": "123 Main St",
            "city": "San Francisco",
            "price": "1000000.00"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(House.objects.count(), 1)
