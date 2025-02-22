from django import forms
from django.forms import ModelForm
from .models import Shipment
from warehouse.models import Warehouse

class ShipmentCreationForm(ModelForm):
    clients = forms.ModelMultipleChoiceField(
        queryset=Warehouse.objects.all(),
        required=False,
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = Shipment
        fields = ['name', 'driver', 'vehicle', 'clients']
