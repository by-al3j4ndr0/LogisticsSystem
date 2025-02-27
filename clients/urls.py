from django.urls import path

from .views import UploadManifest

urlpatterns = [
    path('clients/upload', UploadManifest.as_view(), name='uploadManifest'),
]