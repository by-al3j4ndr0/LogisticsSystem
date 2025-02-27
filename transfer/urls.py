from django.urls import path
from . import views

urlpatterns = [
    path('transference/<uuid:id>/export', views.exportTransference, name='export-transference'),
    path('transference', views.TransferenceListView.as_view(), name="all-transference"),
    path('transference/all', views.CachedTransferenceListView, name='cached'),
    path('transference/new', views.TransferenceCreationView.as_view(), name="add-transference"),
]