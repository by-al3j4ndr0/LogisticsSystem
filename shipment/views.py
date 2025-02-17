from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from shipment.forms import ShipmentCreationForm
from shipment.models import Shipment

@method_decorator(login_required, name='dispatch')
class ShipmentCreationView(SuccessMessageMixin, CreateView):
    template_name = 'shipment/ShipmentCreation.html'
    form_class = ShipmentCreationForm
    success_url = "/shipments"
    success_message = "Shipment was created successfully"

class ShipmentListView(ListView, LoginRequiredMixin):
    template_name = "shipment/shipment_list.html"
    queryset = Shipment.objects.all().order_by('-date')
    context_object_name = "shipments"

class ShipmentDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Shipment
    context_object_name = "shipment"
    pk_url_kwarg = 'id'
    success_url = '/shipments'
    template_name = 'shipment/ShipmentDelete.html'
    success_message = "%(shipment)s was deleted successfully"

class ShipmentUpdateView(SuccessMessageMixin, UpdateView):
    model = Shipment
    pk_url_kwarg = 'id'
    template_name_suffix =  '_update_form'
    fields = ['name', 'driver', 'vehicle', 'clients']
    success_url = '/shipments'
    success_message = "%(name)s was edited successfully"