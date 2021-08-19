from itertools import chain

from django.db.models import (
    Subquery,
    OuterRef,
    F, ExpressionWrapper,
    IntegerField, Q
)
from django.views.generic import ListView

from crm_build.models import RlClient, SysUser, MainImage, SysStat, RlShow
from crm_build.utils import change_stat_enum


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
        queryset = super().get_queryset().filter(
            client_enum='Продажа').exclude(
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


class BuyerDetail(ListView):
    """Карточка покупателя (покупка)"""
    model = RlClient
    context_object_name = 'object'
    template_name = 'object.html'

    def get_queryset(self):
        queryset = RlClient.objects.filter(
            row_id=self.kwargs.get('row_id')).annotate(
            square_price=ExpressionWrapper(
                F('cost') / F('area1'),
                output_field=IntegerField()
            ),
            hundred_square_price=ExpressionWrapper(
                F('cost') / F('area2'),
                output_field=IntegerField()
            ),
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
            row_realty_object=Subquery(
                RlClient.objects.filter(
                    row_id=OuterRef("realty_id")).values("row_id")

            ),
            name_alt_object=Subquery(
                RlClient.objects.filter(
                    row_id=OuterRef("alt_realty_id")).values("name")

            ),
            row_alt_object=Subquery(
                RlClient.objects.filter(
                    row_id=OuterRef("alt_realty_id")).values("row_id")

            )

        )

        return queryset[0]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = RlShow.objects.filter(
            realty_id=context['object'].row_id).annotate(
            create_agent=Subquery(
                SysUser.objects.filter(
                    row_id=OuterRef("user_id")).values("name")
            ),
            comment_object=Subquery(
                RlClient.objects.filter(
                    row_id=OuterRef("client_id")).values("name")
            )

        )

        return context


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        item = RlClient.objects.filter(
            row_id=self.kwargs.get('obj_id')
        ).values("name").first()
        context["name"] = item["name"]
        context['obj_id'] = self.kwargs.get("obj_id")
        return context


class ActionsView(ListView):
    """Выводит все действия, производимые над объектом"""
    model = SysStat
    context_object_name = 'objects'
    template_name = "actions.html"
    lookup_field = "obj_id"

    def get_queryset(self):
        queryset = SysStat.objects.filter(
            obj_id=self.kwargs.get("obj_id")
        ).values(
            "datetime1",
            "stat_enum"
        ).annotate(
            agent=Subquery(
                SysUser.objects.filter(
                    row_id=OuterRef("user_id")).values("name")
            ),
        )
        queryset = [change_stat_enum(item) for item in queryset]
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        item = RlClient.objects.filter(
            row_id=self.kwargs.get('obj_id')
        ).values("name").first()
        context["name"] = item["name"]
        context["obj_id"] = self.kwargs.get("obj_id")
        return context


class DuplicatesView(ListView):
    """Выводит все фотографии объекта"""
    model = RlClient
    context_object_name = 'objects'
    template_name = "duplicates.html"
    lookup_field = "row_id"

    def get_queryset(self):
        q_addr = None
        item = RlClient.objects.filter(
            row_id=self.kwargs.get('obj_id')
        ).first()
        self.name = item.name

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
        if item.addr and item.floor and item.rooms:
            q_addr = RlClient.objects.filter(
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
            for record in q_addr:
                record['duplicate'] = "по адресу"
        result = list(chain(queryset, q_addr)) if q_addr else queryset
        return result

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj_id'] = self.kwargs.get("obj_id")
        context["name"] = self.name
        return context
