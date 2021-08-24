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
    elif type_filter is None and status_filter is None:
        result = None
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
    if request.get('tel1') is not None:
        context['main_filter_value'] = \
            f'tel1={request.get("tel1")}' \
            f'&np_auto={request.get("np_auto")}' \
            f'&street={request.get("street")}' \
            f'&responsible={request.get("responsible")}' \
            f'&rooms={request.get("rooms")}' \
            f'&floors_from={request.get("floors_from")}' \
            f'&floors_to={request.get("floors_to")}' \
            f'&tfloors_from={request.get("tfloors_from")}' \
            f'&param3={request.get("param3")}'
    else:
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
        context["q"] = request.get('q', '')

    return context


def get_filters(request):
    """Получаем фильтры"""
    status_filter = request.get('status', 'default')
    type_filter = request.get('obj_type', 'default')
    queryset_filter = get_filter(status_filter, type_filter)
    search = request.get('q')
    return queryset_filter, search


def get_form_filters(request):
    """Получаем фильтры из формы"""
    agent_filter_queue = request.get("responsible")
    if agent_filter_queue:
        agent_filter = Q(agent__contains=agent_filter_queue)
    else:
        agent_filter = None
    q_objects = Q()
    q_objects = add_filter_tel(q_objects, request.get("tel1"))
    q_objects = add_filter_city(q_objects,request.get("np_auto"))
    q_objects = add_filter_street(q_objects, request.get("street"))
    q_objects = add_filter_rooms(q_objects, request.get("rooms"))
    q_objects = add_range_floor_filter(
        q_objects,
        request.get("floors_from"),
        request.get("floors_to")
    )
    q_objects = add_range_floors_filter(
        q_objects,
        request.get("tfloors_from"),
        request.get("tfloors_to")
    )
    q_objects = add_filter_walls(q_objects, request.get("param3"))
    if request.get('check24') is not None:
        q_objects = add_filter_heat(q_objects, 1)

    return q_objects, agent_filter


def add_filter_tel(q_object, value):
    """Добавляем телефонный номер к фильтру"""
    result = q_object
    if value:
        result &= Q(tel1=value)
    return result


def add_filter_city(q_object, value):
    """Добавляем нас. пункт к фильтру"""
    result = q_object
    if value:
        result &= Q(np_auto=value)
    return result


def add_filter_street(q_object, value):
    """Добавляем улицу к фильтру"""
    result = q_object
    if value:
        result &= Q(street=value)
    return result


def add_filter_rooms(q_object, value):
    """Добавляем количество комнат к фильтру"""
    result = q_object
    if value:
        result &= Q(rooms__contains=value)
    return result


def add_filter_walls(q_object, value):
    """Добавляем материал стен к фильтру"""
    result = q_object
    if value:
        result &= Q(param3=value)
    return result


def add_filter_heat(q_object, value):
    """Добавляем отопление к  фильтру"""
    result = q_object
    if value:
        result &= Q(check24=value)
    return result


def add_range_floor_filter(q_object, start, end):
    """Добавляет фильтр по диапазону этажей"""
    start = start if start else 1
    end = end if end else 20
    if start == 1 and end == 20:
        return q_object
    q_object &= Q(floor__range=[start, end])
    return q_object


def add_range_floors_filter(q_object, start, end):
    """Добавляет фильтр по диапазону этажности"""
    start = start if start else 1
    end = end if end else 20
    if start == 1 and end == 20:
        return q_object
    q_object &= Q(floors__range=[start, end])
    return q_object
