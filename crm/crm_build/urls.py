from django.urls import path

from crm_build.views import MainPageListView, AllSaleObjectListView, AllBuyersListView

urlpatterns = [
    path('', MainPageListView.as_view(), name='index'),
    path('all_sale/', AllSaleObjectListView.as_view(), name='all_sale'),
    path('all_buyers/', AllBuyersListView.as_view(), name='all_buyers')

]
