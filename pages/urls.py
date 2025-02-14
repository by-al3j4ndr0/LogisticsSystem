from django.urls import path
from . import views
from transfer.views import CachedProductListView
from clients.views import UploadManifest
from warehouse.views import CachedWarehouseListView

urlpatterns = [
    path('', views.index, name='home'),
    path('transference/all', CachedProductListView, name='transference'),
    path('clients', UploadManifest, name='clients'),
    path('warehouse', CachedWarehouseListView, name='warehouse')
]