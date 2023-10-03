from rest_framework import serializers

from .models import Shipment, Article


class ArticleInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "name",
            "quantity",
            "price",
            "sender_address",
            "receiver_address",
            "SKU",
            "status",
        )


class ArticleOutputSerializer(serializers.Serializer):
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = Article
        fields = (
            "name",
            "quantity",
            "price",
            "sender_address",
            "receiver_address",
            "SKU",
            "status",
        )


class ShipmentInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ("tracking_number", "carrier")


class ShipmentOutputSerializer(serializers.Serializer):
    articles = ArticleOutputSerializer(many=True)

    class Meta:
        model = Shipment
        fields = ("tracking_number", "carrier", "articles")
