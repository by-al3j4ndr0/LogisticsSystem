from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from .forms import UploadManifestForm
from .models import Clients
from .tables import ClientsHTMxTable
from .filter import ClientsFilter

import pandas as pd

@method_decorator(login_required, name='dispatch')
class ClientsHTMxTableView(SingleTableMixin, FilterView):
    table_class = ClientsHTMxTable
    queryset = Clients.objects.all()
    filterset_class = ClientsFilter
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ClientsFilter(
            self.request.GET,
            queryset=queryset,
        )
        return self.filterset.qs

    def get_template_names(self):
        if self.request.htmx:
            template_name = "clients/clients_table_partial.html"
        else:
            template_name = "clients/clients_table_htmx.html"

        return template_name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query')
        context['form'] = self.filterset.form
        return context

class UploadManifest(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'clients/ManifestUpload.html'
    form_class = UploadManifestForm
    success_url = "/clients"
    success_message = "Manifest was uploaded successfully"

    def form_valid(self, form):
        self.object = form.save()
        data = pd.read_excel(self.object.file, header=14, usecols=[0,1,3,5,6,7,8,9,12,13,14,15,16,17,19,20],
                             names=[
                                 'cod_envio',
                                 'peso',
                                 'descripcion',
                                 'nombre1',
                                 'nombre2',
                                 'apellido1',
                                 'apellido2',
                                 'carnet',
                                 'telefono',
                                 'calle',
                                 'entrecalle1',
                                 'entrecalle2',
                                 'numero',
                                 'reparto',
                                 'provincia',
                                 'municipio',
                             ])
        df = pd.DataFrame(data)
        df.fillna("", inplace=True)
        new_df = df.assign(tariff=0)

        clients_df = pd.DataFrame(columns=['cod_envio',
                                            'peso',
                                            'descripcion',
                                            'nombre',
                                            'ci',
                                            'telefono',
                                            'direccion',
                                            'provincia',
                                            'municipio',
                                            'arancel'
                                            ])

        for i in range(0, len(new_df)):
            clients_df.at[i, 'cod_envio'] = new_df.at[i, 'cod_envio']
            clients_df.at[i, 'nombre'] = " ".join(
                [str(new_df.at[i, 'nombre1']), str(new_df.at[i, 'nombre2']),
                 str(new_df.at[i, 'apellido1']), str(new_df.at[i, 'apellido2'])])
            clients_df.at[i, 'peso'] = new_df.at[i, 'peso']
            clients_df.at[i, 'descripcion'] = new_df.at[i, 'descripcion']
            clients_df.at[i, 'ci'] = new_df.at[i, 'carnet']
            clients_df.at[i, 'telefono'] = new_df.at[i, 'telefono']
            clients_df.at[i, 'direccion'] = " ".join(
                [str(new_df.at[i, 'calle']), "e/", str(new_df.at[i, 'entrecalle1']), "y",
                 str(new_df.at[i, 'entrecalle2']), "#", str(new_df.at[i, 'numero']), ".",
                 str(new_df.at[i, 'reparto'])])
            provincia_splitted = str.split(new_df.at[i, 'provincia'], "/")
            clients_df.at[i, 'provincia'] = provincia_splitted[0]
            municipio_splitted = str.split(new_df.at[i, 'municipio'], "/")
            clients_df.at[i, 'municipio'] = municipio_splitted[0]
            clients_df.at[i, 'arancel'] = 0

        for index, row in clients_df.iterrows():
            Clients.objects.create(
                hbl=row['cod_envio'],
                weight=row['peso'],
                description=row['descripcion'],
                name=row['nombre'],
                ci=row['ci'],
                phone=row['telefono'],
                address=row['direccion'],
                province=row['provincia'],
                city=row['municipio'],
                tariff=row['arancel']
            )

        return HttpResponseRedirect(self.get_success_url())