from django.utils.decorators import method_decorator
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from django.contrib.auth.decorators import login_required

from .models import Warehouse
from .filter import WarehouseFilter
from .tables import WarehouseHTMxTable

@method_decorator(login_required, name='dispatch')
class WarehouseHTMxTableView(SingleTableMixin, FilterView):
    table_class = WarehouseHTMxTable
    queryset = Warehouse.objects.all()
    filterset_class = WarehouseFilter
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = WarehouseFilter(
            self.request.GET,
            queryset=queryset,
        )
        return self.filterset.qs

    def get_template_names(self):
        if self.request.htmx:
            template_name = "warehouse/warehouse_table_partial.html"
        else:
            template_name = "warehouse/warehouse_table_htmx.html"

        return template_name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query')
        context['form'] = self.filterset.form
        return context
