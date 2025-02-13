from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
import pandas as pd

from .models import Transference
from .forms import TransferenceCreationForm

def CachedProductListView(request):
    transfer = Transference.objects.all()
    context = {
        'transfer': transfer
    }
    return render(request, 'transfer/transfer_list.html', context)

class TransferenceCreationView(SuccessMessageMixin, CreateView):
    template_name = 'transfer/TransferCreation.html'
    form_class = TransferenceCreationForm
    success_url = "/transference/all"
    success_message = "Transference was created successfully"

    # def form_valid(self, form):
    #     self.object = form.save()
    #     data = pd.read_excel(self.object.file)
    #     df = pd.DataFrame(data)
    #     self.object.packages = len(df)
    #     return HttpResponseRedirect(self.get_success_url())

class PrintTransference(CreateView):
    print("Hello world")
