import unittest
from django.test import TestCase
from trace.shipment.models import Shipment, Article
from trace.shipment.services import create_shipment, create_article


class ShipmentTestCase(TestCase):
    def test_create_shipment(self):
        tracking_number = "123456"
        carrier = "USPS"
        shipment = create_shipment(tracking_number, carrier)
        self.assertIsInstance(shipment, Shipment)
        self.assertEqual(shipment.tracking_number, tracking_number)
        self.assertEqual(shipment.carrier, carrier)


class ArticleTestCase(TestCase):
    def test_create_article(self):
        name = "Sample Article"
        quantity = 10
        price = 100
        sender_address = "123 Main St, City, State"
        receiver_address = "456 Another St, City, State"
        SKU = "SKU123"
        status = 1

        article = create_article(
            name, quantity, price, sender_address, receiver_address, SKU, status
        )

        self.assertIsInstance(article, Article)
        self.assertEqual(article.name, name)
        self.assertEqual(article.quantity, quantity)
        self.assertEqual(article.price, price)
        self.assertEqual(article.sender_address, sender_address)
        self.assertEqual(article.receiver_address, receiver_address)
        self.assertEqual(article.SKU, SKU)
        self.assertEqual(article.status, status)


if __name__ == "__main__":
    unittest.main()
