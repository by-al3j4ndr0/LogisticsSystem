from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from .forms import UploadManifestForm
from .models import Clients
import pandas as pd

@login_required()
class UploadManifest(SuccessMessageMixin, CreateView):
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
            clients_df.at[i, 'provincia'] = new_df.at[i, 'provincia']
            clients_df.at[i, 'municipio'] = new_df.at[i, 'municipio']
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
