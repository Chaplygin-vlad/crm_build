from django.urls import path

from crm_build.views import MainPageListView, index

urlpatterns = [
    path('', index, name='index'),

    # path('', MainPageListView.as_view(), name='base'),

]