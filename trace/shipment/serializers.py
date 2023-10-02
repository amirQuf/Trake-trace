from rest_framework import serializers

from .models import Shipment, Article


class ArticleInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ()


class ArticleOutputSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = ()


class ShipmentInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ("tracking_number", "carrier")


class ShipmentOutputSerializer(serializers.Serializer):
    articles = ArticleOutputSerializer(many=True)

    class Meta:
        model = Shipment
        fields = ("tracking_number", "carrier")
