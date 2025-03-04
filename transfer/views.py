import os
from io import BytesIO
import pandas as pd
from django_pandas.io import read_frame

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import LETTER, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, TableStyle, Table, Image, Paragraph

from LogisticsSystem.settings import MEDIA_ROOT
from .models import Transference
from .forms import TransferenceCreationForm
from clients.models import Clients
from warehouse.models import Warehouse, WarehouseSimplified


@method_decorator(login_required, name='dispatch')
class TransferenceListView(ListView, LoginRequiredMixin):
    template_name = "transfer/transfer_list.html"
    queryset = Transference.objects.all().order_by('-date')
    context_object_name = "transfer"

def CachedTransferenceListView(request):
    transfer = Transference.objects.all().order_by('-date')
    context = {
        'transfer': transfer
    }
    return render(request, 'transfer/transfer_list.html', context)

class TransferenceCreationView(SuccessMessageMixin, CreateView):
    template_name = 'transfer/TransferCreation.html'
    form_class = TransferenceCreationForm
    success_url = "/transference/all"
    success_message = "Transference was created successfully"

    def form_valid(self, form):
        self.object = form.save()
        transfer_id = self.object.id
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
                    transference_id=transfer_id,
                )
                Clients.objects.filter(hbl=df.at[i, 'cod_envio']).update(status='Almacen')

        # Create the simplified model for the shipments
        clients_data = Warehouse.objects.filter(transference_id=transfer_id)
        clients_data_df = read_frame(clients_data)

        i = 0
        while i < len(clients_data_df):
            quantity = 1
            tariff = clients_data_df.at[i, 'tariff']
            element = clients_data_df.at[i, 'ci']
            for j in range(i + 1, len(clients_data_df)):
                if element in clients_data_df.loc[j, 'ci']:
                    quantity = quantity + 1

            WarehouseSimplified.objects.create(
                name=clients_data_df.at[i, 'name'],
                ci=clients_data_df.at[i, 'ci'],
                phone_number=clients_data_df.at[i, 'phone_number'],
                address=clients_data_df.at[i, 'address'],
                city=clients_data_df.at[i, 'city'],
                state=clients_data_df.at[i, 'state'],
                tariff=tariff,
                quantity=quantity,
                transference_id=transfer_id,
            )

            clients_data_df.reset_index(drop=True, inplace=True)
            i += 1

        return HttpResponseRedirect(self.get_success_url())

def exportTransference(request, id):
    # Set up the response
    file_name = 'Transference-%s.pdf' % id
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=%s' % file_name

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=landscape(LETTER), rightMargin=30, leftMargin=30, topMargin=30,
                            bottomMargin=18)

    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
    s = s["BodyText"]
    s.wordWrap = 'CJK'

    # Build header.
    header_text = '<font size=25>Reporte de Transferencia\n</font><font size=15>\n%s</font>' % id
    header_text_p = Paragraph(header_text, s)
    header_logo = Image(os.path.join(MEDIA_ROOT, 'images', 'logo.png'), width=192, height=75)
    header_table = Table([(header_logo, header_text_p,)], colWidths=[11*cm], rowHeights=[4*cm])
    header_table.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'CENTER'),
                                      ('ALIGN', (0, 0), (0, 0), 'LEFT'),
                                      ('ALIGN', (1, 0), (0, 0), 'LEFT'),
                                      ]))

    data = [
        ["HBL", "Consignatario", "Municipio", "Provincia"],
    ]

    transference_file = MEDIA_ROOT + '/transferencias/transference-%s.xlsx' % id
    transference_data = pd.read_excel(transference_file)
    transference_df = pd.DataFrame(transference_data)

    for i in range(0, len(transference_df)):
        hbl = transference_df.at[i, 'cod_envio']
        info = Clients.objects.filter(hbl=transference_df.at[i, 'cod_envio']).values()

        data.append([str(hbl), str(info[0]['name']), str(info[0]['city']), str(info[0]['province'])])

    content_table = Table(data=data)
    content_table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                                       ('ALIGN', (3, 0), (-1, -1), 'RIGHT'),
                                       ]))

    # Build footer.
    # footer_top_row = ('', '', '', '', '')
    # footer_bot_row = ('Ort/Datum', 'Kunde', '', 'Ort/Datum', 'Consultant',)
    # footer_table = Table([footer_top_row, footer_bot_row], colWidths=[3*cm, 3*cm, 4*cm, 3*cm, 3*cm], rowHeights=[2*cm, 0.5*cm])
    # footer_table.setStyle(TableStyle([('INNERGRID', (0, 0), (0, 1), 0.25, colors.black),
    #                                   ('INNERGRID', (1, 0), (1, 1), 0.25, colors.black),
    #                                   ('INNERGRID', (3, 0), (3, 1), 0.25, colors.black),
    #                                   ('INNERGRID', (4, 0), (4, 1), 0.25, colors.black),
    #                                   ]))

    # Build layout table.
    layout = [header_table, content_table]

    doc.build(layout)

    response.write(buffer.getvalue())
    buffer.close()

    return response