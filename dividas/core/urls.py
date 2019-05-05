from django.urls import path
from dividas.core.views import DividaList, DividaDetail, home, nova

app_name = 'dividas'

urlpatterns = [
    path('', home, name='home'),
    path('nova/', nova, name='nova-divida'),
    path('<int:id>', DividaDetail.as_view(), name='alterar-divida'),
    path('dividas/', DividaList.as_view(), name='dividas-list'),
    path('dividas/<int:pk>/', DividaDetail.as_view(), name='dividas-detail'),
]
