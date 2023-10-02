from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import ModelViewSet
from services import create_shipment, create_article

from .models import Article
from .selectors import retrieve_all_shipments, retrieve_all_articles
from .serializers import (
    ArticleInputSerializer,
    ArticleOutputSerializer,
    ShipmentInputSerializer,
    ShipmentOutputSerializer,
)


class ShipmentViewSet(ModelViewSet):
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
            article = create_article()

        except Exception as ex:
            return Response(f"Database Error {ex}", status=status.HTTP_400_BAD_REQUEST)
        return Response(
            self.ArticleOutputSerializer(article, context={"request": request}).data
        )

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return ArticleOutputSerializer
        return ArticleInputSerializer
