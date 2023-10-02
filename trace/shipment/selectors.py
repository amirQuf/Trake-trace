from .models import Shipment
from typing import List


def retrieve_all_shipment() -> List[Shipment]:
    return Shipment.objects.all()


def retrieve_shipment(shipment_id: int) -> Shipment:
    return Shipment.objects.get(id=shipment_id)
