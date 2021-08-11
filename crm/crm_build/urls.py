from django.urls import path

from crm_build.views import MainPageListView, index

urlpatterns = [
    path('', MainPageListView.as_view(), name='index'),

    # path('', MainPageListView.as_view(), name='base'),

]