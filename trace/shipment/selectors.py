from .models import Shipment, Article
from typing import List


def retrieve_all_shipment() -> List[Shipment]:
    return Shipment.objects.all()


def retrieve_shipment(shipment_id: int) -> Shipment:
    return Shipment.objects.get(id=shipment_id)


def retrieve_all_articles() -> List[Article]:
    return Article.objects.all()


def retrieve_article(article_id: int) -> Article:
    return Article.objects.get(id=article_id)
