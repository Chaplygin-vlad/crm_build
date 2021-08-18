STATUS_DICT = {
    "open": "Просмотр",
    "add": "Создал",
    "edit": "Редактирование"
}


def change_stat_enum(queryset):
    """Приводит действие к русскому"""
    queryset["stat_enum"] = STATUS_DICT.get( queryset.get("stat_enum"))
    return queryset
