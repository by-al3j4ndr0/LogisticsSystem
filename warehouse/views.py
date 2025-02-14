from django.shortcuts import render
from .models import Warehouse

def CachedWarehouseListView(request):
    warehouse = Warehouse.objects.all().order_by('name')
    context = {
        'warehouse': warehouse
    }
    return render(request, 'warehouse/warehouse_list.html', context)
