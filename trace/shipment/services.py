from .models import Shipment, Article


def create_shipment(tracking_number: str, carrier: str) -> Shipment:
    return Shipment.objects.create(tracking_number=tracking_number, carrier=carrier)
