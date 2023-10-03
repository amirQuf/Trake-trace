from trace.shipment.models import Shipment
from django.test import TestCase


class YourModelTests(TestCase):
    def setUp(self):
        self.model_instance = Shipment.objects.create(
        tracking_number ="TN12345678"
        carrier = "DHL"
    )

    def test_model_creation(self):
        self.assertEqual(self.model_instance.tracking_number, "TN12345678")

    def test_shipment_carrier(self):
        result = self.model_instance.carrier
        self.assertEqual(result, "DHL")
