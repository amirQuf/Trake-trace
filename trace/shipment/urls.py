from django.urls import path


from rest_framework.routers import DefaultRouter
from .views import ShipmentViewSet, ArticleViewSet


router = DefaultRouter()

router.register("shipments", ShipmentViewSet)
router.register("articles", ArticleViewSet)

urlpatterns = []


urlpatterns += router.urls
