from django.db.models import (
    Subquery,
    OuterRef,
    F,
    ExpressionWrapper,
    IntegerField
)
from django.shortcuts import render
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
        queryset = RlClient.objects.filter(row_id=self.kwargs.get('row_id')).annotate(
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
        context['comments'] = RlShow.objects.filter(realty_id=context['object'].row_id).annotate(
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
        context['obj_id'] = self.kwargs.get("obj_id")
        return context
