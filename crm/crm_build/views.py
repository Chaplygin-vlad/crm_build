from django.shortcuts import render
from django.views.generic import ListView

from crm_build.models import RlClient


def index(request):
    return render(request, 'index.html')


class MainPageListView(ListView):
    """Главная страница, выводит сразу список всех объектов"""
    model = RlClient
    context_object_name = 'objects'
    template_name = 'index.html'
    paginate_by = 10


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['objects'] = context['objects'].filter(lot=381)

        return context
