from django.db.models import Q
import django_filters
from .models import Warehouse

class WarehouseFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Warehouse
        fields = ['query']

    def universal_search(self, queryset, name, value):
        return Warehouse.objects.filter(
            Q(name__icontains=value) | Q(address__icontains=value) | Q(city__icontains=value) | Q(state__icontains=value)
        )