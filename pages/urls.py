from django.urls import path
from . import views
from transfer.views import CachedProductListView

urlpatterns = [
    path('', views.index, name='home'),
    path('transference/all', CachedProductListView, name='transference')
]