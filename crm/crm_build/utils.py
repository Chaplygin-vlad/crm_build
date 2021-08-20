from django.db.models import Q

STATUS_DICT = {
    "open": "Просмотр",
    "add": "Создал",
    "edit": "Редактирование"
}

DEAL_STATUS = {
    "default": "В работе, Новые, Аванс",
    "all": "Все статусы",
    "new": "Новые",
    "in_work": "В работе",
    "avans": "Аванс",
    "delayed": "Отложенные",
    "closed": "Сделка (завершена)",
    "archive": "Архив (без сделки)",
    "advert": "Рекламные"
}

DEAL_TYPE = {
    "default": "Все объекты недвижимости",
    "apart": "Квартира",
    "house": "Дом",
    "land": "Земельный участок",

}


def change_stat_enum(queryset):
    """Приводит действие к русскому"""
    queryset["stat_enum"] = STATUS_DICT.get(queryset.get("stat_enum"))
    return queryset


def get_status_filter(status):
    """Получаем фильтр для статуса сделки"""
    if status == "default":
        result = Q(status_enum__in=["В работе", "Новые", "Аванс"])
    elif status == "all":
        result = None
    else:
        result = Q(status_enum=DEAL_STATUS[status])
    return result


def get_type_filter(obj_type):
    """Получаем фильтр для типа сделки"""
    if obj_type == "default":
        result = None
    else:
        result = Q(realty_enum=DEAL_TYPE[obj_type])
    return result


def get_filter(status, obj_type):
    """Собирает общий фильтр по двум параметрам"""
    status_filter = get_status_filter(status)
    type_filter = get_type_filter(obj_type)
    if status_filter is None:
        result = type_filter
    elif type_filter is None:
        result = status_filter
    else:
        result = Q(status_filter, type_filter)
    return result


def get_search(queue):
    """Возвращаем параметры для поиска"""
    result = (
            Q(tel1__contains=queue) |
            Q(fff__contains=queue) |
            Q(iii__contains=queue) |
            Q(ooo__contains=queue) |
            Q(lot__contains=queue) |
            Q(addr__contains=queue)
    )
    return result


def get_context_values(request, context):
    """Добавляет данные в контекст"""
    context["status_value"] = DEAL_STATUS[request.get(
        "status",
        "default"
    )]
    context["status_key"] = request.get("status", "default")
    context["obj_type_value"] = DEAL_TYPE[request.get(
        "obj_type",
        "default"
    )]
    context["obj_type_key"] = request.get("obj_type", "default")
    return context


def get_filters(request):
    """Получаем фильтры"""
    status_filter = request.get('status', 'default')
    type_filter = request.get('obj_type', 'default')
    queryset_filter = get_filter(status_filter, type_filter)
    search = request.get('q')
    return queryset_filter, search
