from django.db.models import (
    Subquery,
    OuterRef,
    F,
    ExpressionWrapper,
    IntegerField
)
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from crm_build.models import RlClient, SysUser, MainImage


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
    template_name = 'all_sell_objects.html'
    paginate_by = 10
    expression = F('cost') / F('area1')
    wrapped_expression = ExpressionWrapper(expression, IntegerField())
    queryset = RlClient.objects.all().annotate(square_price=wrapped_expression)

    def get_queryset(self):
        queryset = super().get_queryset().filter(client_enum='Продажа').exclude(
            status_enum='Архив (без сделки)'
        ).annotate(
            photo=Subquery(
                MainImage.objects.filter(
                    obj_id=OuterRef("row_id")).values("row_id")[:1]
            ),
            ext=Subquery(
                MainImage.objects.filter(
                    obj_id=OuterRef("row_id")).values("extention")[:1]
            ),
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


class AllBuyersListView(ListView):
    """Выводит список покупателей"""
    model = RlClient
    context_object_name = 'objects'
    template_name = 'all_buyers.html'
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


class BuyerDetail(DetailView):
    """Карточка покупателя (покупка)"""
    model = RlClient
    context_object_name = 'object'
    template_name = 'buyer.html'

    def get_queryset(self):
        queryset = RlClient.objects.exclude(
            status_enum='Архив (без сделки)'
        ).annotate(
            create_agent=Subquery(
                SysUser.objects.filter(
                    row_id=OuterRef("sys_user_create")).values("name")
            ),
            agent=Subquery(
                SysUser.objects.filter(
                    row_id=OuterRef("user_id")).values("name")
            ),
            name_realty_object=Subquery(
                RlClient.objects.filter(
                    row_id=OuterRef("realty_id")).values("name")

            ),
            lot_realty_object=Subquery(
                RlClient.objects.filter(
                    row_id=OuterRef("realty_id")).values("lot")

            )
        )

        return queryset

