from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Warehouse

@login_required()
def CachedWarehouseListView(request):
    warehouse = Warehouse.objects.all().order_by('name')
    context = {
        'warehouse': warehouse
    }
    return render(request, 'warehouse/warehouse_list.html', context)
