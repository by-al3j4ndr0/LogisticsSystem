import django.forms
from django.forms import ModelForm
from .models import Transference

class TransferenceCreationForm(ModelForm):
    class Meta:
        model = Transference
        fields = ['name', 'file']

