from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Article, Shipment
from .selectors import retrieve_all_articles, retrieve_all_shipments
from .serializers import (
    ArticleInputSerializer,
    ArticleOutputSerializer,
    ShipmentInputSerializer,
    ShipmentOutputSerializer,
)
from .services import create_article, create_shipment


class ShipmentViewSet(ModelViewSet):
    queryset = Shipment.objects.all()

    def list(self, request):
        """
        List of all shipments
        """
        query = retrieve_all_shipments()
        return Response(
            {
                "results": ShipmentOutputSerializer(
                    query, many=True, context={"request": request}
                ),
                "status": "Success",
            },
            status=status.HTTP_200_OK,
        )

    def create(self, request):
        """
        create a new shipment
        """
        serializer = self.get_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            shipment = create_shipment(
                tracking_number=serializer.validated_data.get("tracking_number"),
                carrier=serializer.validated_data.get("carrier"),
            )

        except Exception as ex:
            return Response(f"Database Error {ex}", status=status.HTTP_400_BAD_REQUEST)
        return Response(
            self.ShipmentOutputSerializer(shipment, context={"request": request}).data
        )

    def get_serializer_class(self, data):
        if self.action in ["retrieve", "list"]:
            return ShipmentOutputSerializer
        return ShipmentInputSerializer


class ArticleViewSet(ModelViewSet):
    query_set = Article.objects.all()

    def list(self, request):
        """List all shipments"""
        query = retrieve_all_articles()
        return Response(
            {
                "results": ArticleOutputSerializer(
                    query, many=True, context={"request": request}
                ),
                "status": "Success",
            },
            status=status.HTTP_200_OK,
        )

    def create(self, request, *args, **kwargs):
        """create a new shipment"""
        serializer = self.get_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            article = create_article(
                name=serializer.validated_data.get("name"),
                quantity=serializer.validated_data.get("quantity"),
                price=serializer.validated_data.get("price"),
                sender_address=serializer.validated_data.get("sender_address"),
                receiver_address=serializer.validated_data.get("receiver_address"),
                SKU=serializer.validated_data.get("SKU"),
                status=serializer.validated_data.get("status"),
            )

        except Exception as ex:
            return Response(f"Database Error {ex}", status=status.HTTP_400_BAD_REQUEST)
        return Response(
            self.ArticleOutputSerializer(article, context={"request": request}).data
        )

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return ArticleOutputSerializer
        return ArticleInputSerializer
