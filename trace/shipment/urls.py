from django.urls import path


from rest_framework.routers import DefaultRouter
from .views import ShipmentViewSet, ArticleViewSet


router = DefaultRouter()

router.register("shipments", ShipmentViewSet, basename="Shipment")
router.register("articles", ArticleViewSet, basename="Article")

urlpatterns = []


urlpatterns += router.urls
