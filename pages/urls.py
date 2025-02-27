from django.urls import path
from . import views
from transfer.views import TransferenceListView
from clients.views import ClientsHTMxTableView
from warehouse.views import WarehouseHTMxTableView
from shipment.views import ShipmentListView

urlpatterns = [
    path('', views.index, name='home'),
    path('transference', TransferenceListView.as_view(), name='transference'),
    path('clients', ClientsHTMxTableView.as_view(), name='clients'),
    path('warehouse', WarehouseHTMxTableView.as_view(), name='warehouse'),
    path("shipments/all", ShipmentListView.as_view(), name='shipments')
]