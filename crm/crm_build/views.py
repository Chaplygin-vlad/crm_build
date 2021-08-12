from django.db.models import Subquery, OuterRef, F, ExpressionWrapper, IntegerField
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


class AllSaleObjectListView(ListView):
    """Выводит все объекты недвижимости"""
    model = RlClient
    context_object_name = 'objects'
    template_name = 'all_sale_objects.html'
    paginate_by = 10
    expression = F('cost')/F('area1')
    wrapped_expression = ExpressionWrapper(expression, IntegerField())
    queryset = RlClient.objects.all().annotate(square_price=wrapped_expression)

    def get_queryset(self):
        queryset = super().get_queryset().filter(client_enum='Продажа').exclude(
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
