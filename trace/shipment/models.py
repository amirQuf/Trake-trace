from django.db import models

from trace.common.models import BaseModel


class Article(BaseModel):
    IN_TRANSIT = 0
    INBOUND_SCAN = 1
    DELIVERY = 2
    SCANNED = 3
    TRANSIT = 4

    STATUS_CHOICES = (
        (IN_TRANSIT, "IN_TRANSIT"),
        (INBOUND_SCAN, "INBOUND_SCAN"),
        (DELIVERY, "DELIVERY"),
        (SCANNED, "SCANNED"),
        (TRANSIT, "TRANSIT"),
    )

    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveBigIntegerField()
    sender_address = models.CharField(max_length=100, null=True)
    receiver_address = models.CharField(max_length=100, null=True)
    SKU = models.CharField(max_length=100, unique=True)
    status = models.PositiveIntegerField(default=0, choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return f"{self.name}|{self.SKU}"

    class Meta:
        ordering = ["-created_at", "-updated_at"]


class Shipment(BaseModel):
    tracking_number = models.CharField(max_length=100, unique=True)
    carrier = models.CharField(max_length=100, null=True)
    articles = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="shipments"
    )

    def __str__(self) -> str:
        return f"{self.tracking_number}|{self.carrier}"

    class Meta:
        ordering = ["-created_at", "-updated_at"]
