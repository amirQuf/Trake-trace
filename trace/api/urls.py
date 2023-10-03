from django.urls import path, include

urlpatterns = [
    path(" ", include("trace.shipment.urls")),
]
