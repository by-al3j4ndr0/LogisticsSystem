import django_filters
from django import forms
from django.urls import reverse_lazy

from .models import Clients

class ClientsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(attrs={
            'hx-get': reverse_lazy('clients'),
            'hx-target': 'div.table-container',
            'hx-swap' : 'outerHTML',
            'hx-trigger': 'keyup',
            'hx-indicator': '.progress',
            'placeholder': 'Nombre...',
            'class': 'form-inline',
        })
    )

    class Meta:
        model = Clients
        fields = ['name']
