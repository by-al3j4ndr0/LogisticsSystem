import django_tables2 as tables
from .models import Clients

class ClientsHTMxTable(tables.Table):
    class Meta:
        model = Clients
        fields = ['hbl', 'description', 'name', 'ci', 'phone', 'city', 'province', 'tariff', 'status']
        template_name = "tables/bootstrap_htmx.html"