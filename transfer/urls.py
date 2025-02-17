from django.urls import path
from . import views

urlpatterns = [
    path('transference/<int:id>/print', views.PrintTransference.as_view(), name='print-transference'),
    path('transference', views.TransferenceListView.as_view(), name="all-transference"),
    path('transference/all', views.CachedTransferenceListView, name='cached'),
    path('transference/new', views.TransferenceCreationView.as_view(), name="add-transference"),
]