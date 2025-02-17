from django.urls import path

from shipment.views import ShipmentCreationView, ShipmentDeleteView, ShipmentListView, ShipmentUpdateView

urlpatterns = [
    path('shipments/new', ShipmentCreationView.as_view(), name="addShipment"),
    path('shipments', ShipmentListView.as_view(), name="all-shipment"),
    path('shipments/<int:id>/delete', ShipmentDeleteView.as_view(), name="delete-shipment"),
    path('shipments/<int:id>/edit', ShipmentUpdateView.as_view(), name="edit-shipment"),
]