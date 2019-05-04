from django.urls import path
from dividas.core.views import DividaList, DividaDetail, home

app_name = 'dividas'

urlpatterns = [
    path('', home, name='home'),
    path('<int:id>', DividaDetail.as_view(), name='alterar_divida'),
    path('dividas/', DividaList.as_view(), name='dividas-list'),
    path('dividas/<int:pk>/', DividaDetail.as_view(), name='dividas-detail'),
]
