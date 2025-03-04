import django_tables2 as tables
from .models import Warehouse

class WarehouseHTMxTable(tables.Table):
    class Meta:
        model = Warehouse
        fields = ['hbl', 'name', 'ci', 'phone_number', 'city', 'state']
        template_name = "tables/bootstrap_htmx.html"