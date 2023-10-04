from .models import Shipment, Article


def create_shipment(tracking_number: str, carrier: str) -> Shipment:
    """
    Create a new shipment with the provided tracking number and carrier.

    Args:
        tracking_number (str): The tracking number for the shipment.
        carrier (str): The carrier responsible for the shipment.

    Returns:
        Shipment: The newly created shipment object.
    """
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
    """
    Create a new article with the provided details.

    Args:
        name (str): The name of the article.
        quantity (int): The quantity of the article.
        price (int): The price of the article.
        sender_address (str): The address of the sender.
        receiver_address (str): The address of the receiver.
        SKU (str): The Stock Keeping Unit (SKU) for the article.
        status (int): The status of the article.

    Returns:
        Article: The newly created article object.
    """
    return Article.objects.create(
        name=name,
        quantity=quantity,
        price=price,
        sender_address=sender_address,
        receiver_address=receiver_address,
        SKU=SKU,
        status=status,
    )
