from django.forms import ModelForm
from .models import Manifest

class UploadManifestForm(ModelForm):
    class Meta:
        model = Manifest
        fields = ['file']

