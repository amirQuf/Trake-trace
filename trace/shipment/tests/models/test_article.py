from trace.shipment.models import Article
from django.test import TestCase


class YourModelTests(TestCase):
    def setUp(self):
        self.model_instance = Article.objects.create(
            name="Laptop",
            quantity=1,
            price=800,
            sender_address="Street 1, 10115 Berlin, Germany",
            receiver_address="Street 10, 75001 Paris, France",
            SKU="LP123",
            status=0,
        )

    def test_model_creation(self):
        self.assertEqual(self.model_instance.name, "LP123")

    def test_Article_status(self):
        result = self.model_instance.get_status_display()
        self.assertEqual(result, "IN_TRANSIT")
