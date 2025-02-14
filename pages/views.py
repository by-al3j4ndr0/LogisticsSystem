from django.conf import settings
from django.shortcuts import render
from warehouse.models import Warehouse

def index(request):

    # transfer_count = PackagesTransfer.objects.count()
    warehouse_count = Warehouse.objects.count()

    context = {
        # 'transfer_count' :transfer_count,
        'warehouse_count' :warehouse_count,
    }
    return render(request, 'pages/index.html', context)

