from django.urls import path
from . import views

urlpatterns = [
    path('transference/<int:id>/print', views.PrintTransference.as_view(), name='print-transference'),
    path('transference/add', views.TransferenceCreationView.as_view(), name='addTransference'),
]