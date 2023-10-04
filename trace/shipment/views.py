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

from django_filters.rest_framework import DjangoFilterBackend


class ShipmentViewSet(ModelViewSet):
    queryset = Shipment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tracking_number", "carrier"]

    def list(self, request):
        """
        Retrieve a list of all shipments.

        This method retrieves a list of all shipments from the database using the
        'retrieve_all_shipments' selector function. It then serializes the data using
        the 'ShipmentOutputSerializer' and returns a Response object containing the
        serialized data and a success status.

        Parameters:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: A Response object containing a list of serialized shipments and a
            success status.

        Raises:
            N/A
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
        Create a new shipment.

        This method handles the creation of a new shipment based on the provided data.
        It utilizes the specified serializer to validate the request data and then creates
        a shipment using the validated tracking number and carrier information.

        Parameters:
            request (HttpRequest): The HTTP request object containing the payload data.

        Returns:
            Response: A Response object containing the serialized data of the created shipment.

        Raises:
            HTTP_400_BAD_REQUEST: If there's a database error during shipment creation.
            ValidationError: If the request data is invalid or missing required fields.
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
        """
        Determine the appropriate serializer class for the view action.

        This method determines the serializer class to use based on the action being
        performed (retrieve or list) and returns the corresponding serializer class.

        Parameters:
            data: The data associated with the request.

        Returns:
            Serializer Class: The appropriate serializer class based on the action.

        Raises:
            N/A
        """
        if self.action in ["retrieve", "list"]:
            return ShipmentOutputSerializer
        return ShipmentInputSerializer


class ArticleViewSet(ModelViewSet):
    query_set = Article.objects.all()

    def list(self, request):
        """
        List all articles.

        This method retrieves a list of all articles from the database using the
        'retrieve_all_articles' selector function. It then serializes the data using
        the 'ArticleOutputSerializer' and returns a Response object containing the
        serialized data and a success status.

        Parameters:
            request (HttpRequest): The HTTP request object.

        Returns:
            Response: A Response object containing a list of serialized articles and a
            success status.

        Raises:
            N/A
        """
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
        """
        Create a new article.

        This method handles the creation of a new article based on the provided data.
        It utilizes the specified serializer to validate the request data and then creates
        an article using the validated article information.

        Parameters:
            request (HttpRequest): The HTTP request object containing the payload data.
            args (tuple): Additional positional arguments.
            kwargs (dict): Additional keyword arguments.

        Returns:
            Response: A Response object containing the serialized data of the created article.

        Raises:
            HTTP_400_BAD_REQUEST: If there's a database error during article creation.
            ValidationError: If the request data is invalid or missing required fields.
        """
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
        """
        Determine the appropriate serializer class for the view action.

        This method determines the serializer class to use based on the action being
        performed (retrieve or list) and returns the corresponding serializer class.

        Returns:
            Serializer Class: The appropriate serializer class based on the action.

        Raises:
            N/A
        """
        if self.action in ["retrieve", "list"]:
            return ArticleOutputSerializer
        return ArticleInputSerializer
