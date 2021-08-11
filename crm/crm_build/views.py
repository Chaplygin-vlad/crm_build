from django.db.models import Subquery, OuterRef
from django.shortcuts import render
from django.views.generic import ListView

from crm_build.models import RlClient, SysUser


def index(request):
    return render(request, 'index.html')


class MainPageListView(ListView):
    """Главная страница, выводит сразу список всех клиентов"""
    model = RlClient
    context_object_name = 'objects'
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = RlClient.objects.exclude(
            status_enum='Архив (без сделки)'
        ).annotate(
            agent=Subquery(
                SysUser.objects.filter(
                    row_id=OuterRef("user_id")).values("name")
            ),
            last_agent=Subquery(
                SysUser.objects.filter(
                    row_id=OuterRef("last_work_user_id")).values("name")
            )
        )

        return queryset
