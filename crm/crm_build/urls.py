from django.urls import path

from crm_build.views import MainPageListView, AllSaleObjectListView

urlpatterns = [
    path('', MainPageListView.as_view(), name='index'),
    path('all_sale/', AllSaleObjectListView.as_view(), name='all_sale')

]
