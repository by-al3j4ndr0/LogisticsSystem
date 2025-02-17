from django import forms
from django.forms import ModelForm
from .models import Shipment
from warehouse.models import Warehouse

class ShipmentCreationForm(ModelForm):
    clients = forms.ModelChoiceField(
        queryset=Warehouse.objects.all().values(),
        required=False,
        empty_label=None,
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = Shipment
        fields = ['name', 'driver', 'vehicle', 'clients']
