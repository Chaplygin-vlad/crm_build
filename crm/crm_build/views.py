from itertools import chain

from django.db.models import (
    Subquery,
    OuterRef,
    F, ExpressionWrapper,
    IntegerField, Q
)
from django.shortcuts import render
from django.views.generic import ListView

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
    template_name = 'all_sale_objects.html'
    paginate_by = 10
    expression = F('cost')/F('area1')
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


class PhotosView(ListView):
    """Выводит все фотографии объекта"""
    model = MainImage
    context_object_name = 'objects'
    template_name = "photo.html"
    lookup_field = "obj_id"

    def get_queryset(self):
        queryset = MainImage.objects.filter(
            obj_id=self.kwargs.get("obj_id")
        ).values("row_id", "extention", "obj_id")

        return queryset


class DuplicatesView(ListView):
    """Выводит все фотографии объекта"""
    model = RlClient
    context_object_name = 'objects'
    template_name = "duplicates.html"
    lookup_field = "row_id"

    def get_queryset(self):

        item = RlClient.objects.filter(
            row_id=self.kwargs.get('row_id')
        ).first()

        queryset1 = RlClient.objects.filter(
            ~Q(row_id=item.row_id),
            tel1=item.tel1,
        ).values(
            "name", "sys_date_create", "row_id"
        ).annotate(
            agent=Subquery(
                SysUser.objects.filter(
                    row_id=OuterRef("user_id")).values("name")
            )
        )
        queryset2 = RlClient.objects.filter(
            ~Q(row_id=item.row_id),
            tel2=item.tel1,
        ).values(
            "name", "sys_date_create", "row_id"
        ).annotate(
            agent=Subquery(
                SysUser.objects.filter(
                    row_id=OuterRef("user_id")).values("name")
            )
        )
        queryset3 = RlClient.objects.filter(
            ~Q(row_id=item.row_id),
            tel3=item.tel1,
        ).values(
            "name", "sys_date_create", "row_id"
        ).annotate(
            agent=Subquery(
                SysUser.objects.filter(
                    row_id=OuterRef("user_id")).values("name")
            )
        )
        queryset4 = RlClient.objects.filter(
            ~Q(row_id=item.row_id),
            tel4=item.tel1,
        ).values(
            "name", "sys_date_create", "row_id"
        ).annotate(
            agent=Subquery(
                SysUser.objects.filter(
                    row_id=OuterRef("user_id")).values("name")
            )
        )
        queryset5 = RlClient.objects.filter(
            ~Q(row_id=item.row_id),
            tel5=item.tel1,
        ).values(
            "name", "sys_date_create", "row_id"
        ).annotate(
            agent=Subquery(
                SysUser.objects.filter(
                    row_id=OuterRef("user_id")).values("name")
            )
        )
        queryset6 = RlClient.objects.filter(
            ~Q(row_id=item.row_id),
            tel6=item.tel1,
        ).values(
            "name", "sys_date_create", "row_id"
        ).annotate(
            agent=Subquery(
                SysUser.objects.filter(
                    row_id=OuterRef("user_id")).values("name")
            ),
        )
        queryset = (queryset1 | queryset2 | queryset3 |
                    queryset4 | queryset5 | queryset6)
        for record in queryset:
            record['duplicate'] = "по телефону"

        addr = Q(
            addr=item.addr
        )
        floor = Q(
            floor=item.floor
        )
        rooms = Q(
            rooms=item.rooms
        )
        queryset_addr = RlClient.objects.filter(
            ~Q(row_id=item.row_id),
            addr & floor & rooms
        ).values(
            "name", "sys_date_create", "row_id"
        ).annotate(
            agent=Subquery(
                SysUser.objects.filter(
                    row_id=OuterRef("user_id")).values("name")
            )
        )
        for record in queryset_addr:
            record['duplicate'] = "по адресу"

        return list(chain(queryset, queryset_addr))
