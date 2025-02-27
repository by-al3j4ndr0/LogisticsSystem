from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from django_pandas.io import read_frame
import pandas as pd

from shipment.forms import ShipmentCreationForm
from shipment.models import Shipment
from warehouse.models import Warehouse


@method_decorator(login_required, name='dispatch')
class ShipmentListView(ListView, LoginRequiredMixin):
    template_name = "shipment/shipment_list.html"
    queryset = Shipment.objects.all().order_by('-date')
    context_object_name = "shipments"

class ShipmentCreationView(SuccessMessageMixin, CreateView):
    template_name = 'shipment/ShipmentCreation.html'
    form_class = ShipmentCreationForm
    success_url = "/shipments"
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        self.object = form.save()
        for client in self.object.clients.all():
            print(client.hbl)
        return HttpResponseRedirect(self.get_success_url())

class ShipmentDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Shipment
    context_object_name = "shipments"
    pk_url_kwarg = 'id'
    success_url = '/shipments'
    template_name = 'shipment/ShipmentDelete.html'
    success_message = "Shipment was deleted successfully"

class ShipmentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Shipment
    pk_url_kwarg = 'id'
    template_name_suffix =  '_update_form'
    fields = ['name', 'driver', 'vehicle', 'clients']
    success_url = '/shipments'
    success_message = "%(name)s was edited successfully"

def exportRoute(request, id):
    clients_id = Shipment.objects.filter(id=id).values('clients')
    clients_id_df = read_frame(clients_id)
