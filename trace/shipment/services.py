from .models import Shipment, Article


def create_shipment(tracking_number: str, carrier: str) -> Shipment:
    return Shipment.objects.create(tracking_number=tracking_number, carrier=carrier)


def create_article(
    name: str,
    quantity: int,
    price: int,
    sender_address: str,
    receiver_address: str,
    SKU: str,
    status: int,
) -> Article:
    return Article.objects.create(
        name=name,
        quantity=quantity,
        price=price,
        sender_address=sender_address,
        receiver_address=receiver_address,
        SKU=SKU,
        status=status,
    )
