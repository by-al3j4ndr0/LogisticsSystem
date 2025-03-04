from django import forms
from django.forms import ModelForm
from .models import Shipment
from warehouse.models import WarehouseSimplified


class ShipmentCreationForm(ModelForm):
    clients = forms.ModelMultipleChoiceField(
        queryset=WarehouseSimplified.objects.values_list('name', 'city', 'state', 'quantity').order_by('name'),
        required=True,
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = Shipment
        fields = ['name', 'driver', 'vehicle', 'clients']
