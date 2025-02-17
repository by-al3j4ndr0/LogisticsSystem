from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
import pandas as pd

from .models import Transference
from .forms import TransferenceCreationForm
from clients.models import Clients
from warehouse.models import Warehouse

@method_decorator(login_required, name='dispatch')
def CachedTransferenceListView(request):
    transfer = Transference.objects.all().order_by('-date')
    context = {
        'transfer': transfer
    }
    return render(request, 'transfer/transfer_list.html', context)

class TransferenceListView(ListView, LoginRequiredMixin):
    template_name = "transfer/transfer_list.html"
    queryset = Transference.objects.all().order_by('-date')
    context_object_name = "transfer"

class TransferenceCreationView(SuccessMessageMixin, CreateView):
    template_name = 'transfer/TransferCreation.html'
    form_class = TransferenceCreationForm
    success_url = "/transference/all"
    success_message = "Transference was created successfully"

    def form_valid(self, form):
        self.object = form.save()
        data = pd.read_excel(self.object.file)
        df = pd.DataFrame(data)

        for i in range(0, len(df)):
            if Clients.objects.get(hbl=df.at[i, 'cod_envio']):
                Warehouse.objects.create(
                    hbl=Clients.objects.filter(hbl=df.at[i, 'cod_envio']).values('hbl'),
                    name=Clients.objects.filter(hbl=df.at[i, 'cod_envio']).values('name'),
                    ci=Clients.objects.filter(hbl=df.at[i, 'cod_envio']).values('ci'),
                    phone_number=Clients.objects.filter(hbl=df.at[i, 'cod_envio']).values('phone'),
                    address=Clients.objects.filter(hbl=df.at[i, 'cod_envio']).values('address'),
                    city=Clients.objects.filter(hbl=df.at[i, 'cod_envio']).values('city'),
                    state=Clients.objects.filter(hbl=df.at[i, 'cod_envio']).values('province'),
                    tariff=Clients.objects.filter(hbl=df.at[i, 'cod_envio']).values('tariff'),
                )


        return HttpResponseRedirect(self.get_success_url())

class PrintTransference(CreateView):
    print("Hello world")
