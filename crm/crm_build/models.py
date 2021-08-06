# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MainDocument(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=146, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_date_update = models.DateTimeField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    doc_name = models.CharField(max_length=245, blank=True, null=True)
    text1 = models.TextField(blank=True, null=True)
    active_check = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_document'
        app_label = 'crm_build'


class MainFile(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=146, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    obj_id = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    path = models.CharField(max_length=145, blank=True, null=True)
    extention = models.CharField(max_length=10, blank=True, null=True)
    md5 = models.CharField(max_length=45, blank=True, null=True)
    old_name = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=345, blank=True, null=True)
    to_role_ids = models.CharField(max_length=45, blank=True, null=True)
    check1 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_file'
        app_label = 'crm_build'


class MainImage(models.Model):
    row_id = models.IntegerField(primary_key=True)
    old_name = models.CharField(max_length=255)
    user = models.IntegerField()
    time = models.IntegerField()
    card_name = models.CharField(max_length=25)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_change = models.DateTimeField(blank=True, null=True)
    obj_id = models.IntegerField()
    extention = models.CharField(max_length=10)
    md5 = models.CharField(max_length=32)
    main_check = models.IntegerField(blank=True, null=True)
    name_type = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=345, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    name_auto = models.CharField(max_length=145, blank=True, null=True)
    check1 = models.IntegerField(blank=True, null=True)
    plan_check = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_image'
        app_label = 'crm_build'


class MainNumber(models.Model):

    class Meta:
        managed = False
        db_table = 'main_number'
        app_label = 'crm_build'


class MainSpamObj(models.Model):
    spam_id = models.IntegerField(blank=True, null=True)
    obj_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=145, blank=True, null=True)
    subject_cache = models.CharField(max_length=32, blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_spam_obj'
        app_label = 'crm_build'


class RlCall(models.Model):
    row_id = models.IntegerField(unique=True)
    lot = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_update = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    stop_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    fio = models.TextField(blank=True, null=True)
    fff = models.CharField(max_length=45, blank=True, null=True)
    iii = models.CharField(max_length=45, blank=True, null=True)
    ooo = models.CharField(max_length=45, blank=True, null=True)
    tel1 = models.CharField(max_length=45, blank=True, null=True)
    tel2 = models.CharField(max_length=45, blank=True, null=True)
    tel3 = models.CharField(max_length=45, blank=True, null=True)
    tel4 = models.CharField(max_length=45, blank=True, null=True)
    tel5 = models.CharField(max_length=45, blank=True, null=True)
    tel6 = models.CharField(max_length=45, blank=True, null=True)
    tel1_comment = models.TextField(blank=True, null=True)
    tel2_comment = models.TextField(blank=True, null=True)
    tel3_comment = models.TextField(blank=True, null=True)
    tel4_comment = models.TextField(blank=True, null=True)
    tel5_comment = models.TextField(blank=True, null=True)
    tel6_comment = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    adv_type = models.IntegerField(blank=True, null=True)
    status_type = models.IntegerField(blank=True, null=True)
    status_enum = models.CharField(max_length=45, blank=True, null=True)
    not_sms_agent_check = models.IntegerField(blank=True, null=True)
    client_enum = models.CharField(max_length=45, blank=True, null=True)
    deal_enum = models.CharField(max_length=45, blank=True, null=True)
    realty_enum = models.CharField(max_length=45, blank=True, null=True)
    addr = models.TextField(blank=True, null=True)
    deal_type = models.IntegerField(blank=True, null=True)
    np_auto = models.TextField(blank=True, null=True)
    rayon_types = models.TextField(blank=True, null=True)
    street = models.CharField(max_length=45, blank=True, null=True)
    dom = models.CharField(max_length=45, blank=True, null=True)
    drob = models.CharField(max_length=5, blank=True, null=True)
    str = models.CharField(max_length=45, blank=True, null=True)
    korp = models.CharField(max_length=45, blank=True, null=True)
    section_number = models.CharField(max_length=45, blank=True, null=True)
    kv = models.CharField(max_length=45, blank=True, null=True)
    flat_number = models.IntegerField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    floors = models.IntegerField(blank=True, null=True)
    rooms = models.CharField(max_length=15, blank=True, null=True)
    area1 = models.FloatField(blank=True, null=True)
    area2 = models.FloatField(blank=True, null=True)
    area3 = models.FloatField(blank=True, null=True)
    area4 = models.CharField(max_length=45, blank=True, null=True)
    area5 = models.FloatField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    valuta_type = models.IntegerField(blank=True, null=True)
    geocode = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateTimeField(blank=True, null=True)
    check1 = models.IntegerField(blank=True, null=True)
    check2 = models.IntegerField(blank=True, null=True)
    check3 = models.IntegerField(blank=True, null=True)
    check4 = models.IntegerField(blank=True, null=True)
    check5 = models.IntegerField(blank=True, null=True)
    check6 = models.IntegerField(blank=True, null=True)
    check7 = models.IntegerField(blank=True, null=True)
    check8 = models.IntegerField(blank=True, null=True)
    check9 = models.IntegerField(blank=True, null=True)
    param1 = models.CharField(max_length=45, blank=True, null=True)
    param2 = models.CharField(max_length=45, blank=True, null=True)
    param3 = models.CharField(max_length=45, blank=True, null=True)
    param4 = models.IntegerField(blank=True, null=True)
    param5 = models.CharField(max_length=45, blank=True, null=True)
    param6 = models.CharField(max_length=45, blank=True, null=True)
    param7 = models.CharField(max_length=45, blank=True, null=True)
    param8 = models.CharField(max_length=45, blank=True, null=True)
    param9 = models.CharField(max_length=45, blank=True, null=True)
    param10 = models.CharField(max_length=45, blank=True, null=True)
    param11 = models.CharField(max_length=45, blank=True, null=True)
    param12 = models.CharField(max_length=45, blank=True, null=True)
    param13 = models.CharField(max_length=45, blank=True, null=True)
    param14 = models.CharField(max_length=45, blank=True, null=True)
    param15 = models.CharField(max_length=45, blank=True, null=True)
    param16 = models.CharField(max_length=45, blank=True, null=True)
    param17 = models.TextField(blank=True, null=True)
    param18 = models.CharField(max_length=45, blank=True, null=True)
    param19 = models.CharField(max_length=45, blank=True, null=True)
    param20 = models.CharField(max_length=45, blank=True, null=True)
    param21 = models.CharField(max_length=45, blank=True, null=True)
    param22 = models.CharField(max_length=45, blank=True, null=True)
    param23 = models.CharField(max_length=45, blank=True, null=True)
    param24 = models.CharField(max_length=45, blank=True, null=True)
    param25 = models.CharField(max_length=45, blank=True, null=True)
    param26 = models.CharField(max_length=45, blank=True, null=True)
    param27 = models.CharField(max_length=45, blank=True, null=True)
    param28 = models.CharField(max_length=45, blank=True, null=True)
    param29 = models.CharField(max_length=45, blank=True, null=True)
    param100 = models.CharField(max_length=45, blank=True, null=True)
    param101 = models.CharField(max_length=45, blank=True, null=True)
    sex_enum = models.CharField(max_length=4, blank=True, null=True)
    way_type = models.IntegerField(blank=True, null=True)
    blag_check = models.IntegerField(blank=True, null=True)
    agency = models.TextField(blank=True, null=True)
    floor_enum = models.CharField(max_length=45, blank=True, null=True)
    obl_rayon_auto = models.TextField(blank=True, null=True)
    np_rayon_auto = models.TextField(blank=True, null=True)
    way_auto = models.CharField(max_length=45, blank=True, null=True)
    realty_id = models.IntegerField(blank=True, null=True)
    jk_id = models.IntegerField(blank=True, null=True)
    pos_enum = models.CharField(max_length=20, blank=True, null=True)
    okrug_type = models.IntegerField(blank=True, null=True)
    district_type = models.IntegerField(blank=True, null=True)
    metro1_type = models.IntegerField(blank=True, null=True)
    metro2_type = models.IntegerField(blank=True, null=True)
    metro3_type = models.IntegerField(blank=True, null=True)
    to_metro_w = models.IntegerField(blank=True, null=True)
    to_metro_t = models.IntegerField(blank=True, null=True)
    obl_auto = models.CharField(max_length=45, blank=True, null=True)
    jk_name = models.CharField(max_length=145, blank=True, null=True)
    from_mkad = models.IntegerField(blank=True, null=True)
    from_way = models.IntegerField(blank=True, null=True)
    rooms_from = models.IntegerField(blank=True, null=True)
    cost_from = models.IntegerField(blank=True, null=True)
    area1_from = models.IntegerField(blank=True, null=True)
    area2_from = models.IntegerField(blank=True, null=True)
    kontr_check = models.IntegerField(blank=True, null=True)
    kontr_agency = models.CharField(max_length=65, blank=True, null=True)
    kontr_list = models.CharField(max_length=15, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    face_auto = models.CharField(max_length=45, blank=True, null=True)
    ex_check = models.IntegerField(blank=True, null=True)
    alt_check = models.IntegerField(blank=True, null=True)
    nal_check = models.IntegerField(blank=True, null=True)
    ipoteka_check = models.IntegerField(blank=True, null=True)
    rassrochka_check = models.IntegerField(blank=True, null=True)
    np_rayon_auto2 = models.CharField(max_length=45, blank=True, null=True)
    np_rayon_auto3 = models.CharField(max_length=45, blank=True, null=True)
    np_rayon_auto4 = models.CharField(max_length=45, blank=True, null=True)
    np_rayon_auto5 = models.CharField(max_length=45, blank=True, null=True)
    np_rayon_auto6 = models.CharField(max_length=45, blank=True, null=True)
    street2 = models.CharField(max_length=45, blank=True, null=True)
    street3 = models.CharField(max_length=45, blank=True, null=True)
    street4 = models.CharField(max_length=45, blank=True, null=True)
    street5 = models.CharField(max_length=45, blank=True, null=True)
    ugl_check = models.IntegerField(blank=True, null=True)
    obj_id = models.IntegerField(blank=True, null=True)
    kladr_city_id = models.CharField(max_length=20, blank=True, null=True)
    kladr_street_id = models.CharField(max_length=20, blank=True, null=True)
    floor_not_first_check = models.IntegerField(blank=True, null=True)
    floor_not_last_check = models.IntegerField(blank=True, null=True)
    auto1 = models.CharField(max_length=45, blank=True, null=True)
    auto2 = models.CharField(max_length=45, blank=True, null=True)
    auto3 = models.CharField(max_length=45, blank=True, null=True)
    sobstv_check = models.IntegerField(blank=True, null=True)
    dialstatus = models.CharField(max_length=45, blank=True, null=True)
    dialstring = models.CharField(max_length=100, blank=True, null=True)
    uniqueid = models.CharField(max_length=45, blank=True, null=True)
    record_link = models.TextField(blank=True, null=True)
    in_out = models.CharField(max_length=3, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    dial_check = models.IntegerField(blank=True, null=True)
    event_id = models.IntegerField(blank=True, null=True)
    destination = models.CharField(max_length=45, blank=True, null=True)
    channel = models.CharField(max_length=45, blank=True, null=True)
    exten = models.CharField(max_length=45, blank=True, null=True)
    fy_enum = models.CharField(max_length=8, blank=True, null=True)
    check36 = models.IntegerField(blank=True, null=True)
    check37 = models.IntegerField(blank=True, null=True)
    check38 = models.IntegerField(blank=True, null=True)
    check39 = models.IntegerField(blank=True, null=True)
    check40 = models.IntegerField(blank=True, null=True)
    check41 = models.IntegerField(blank=True, null=True)
    check24 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_call'
        app_label = 'crm_build'


class RlClient(models.Model):
    row_id = models.IntegerField(unique=True)
    lot = models.AutoField(primary_key=True)
    name = models.CharField(max_length=145, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_update = models.DateTimeField(blank=True, null=True)
    fio = models.CharField(max_length=145, blank=True, null=True)
    fff = models.CharField(max_length=45, blank=True, null=True)
    iii = models.CharField(max_length=145, blank=True, null=True)
    ooo = models.CharField(max_length=45, blank=True, null=True)
    tel1 = models.CharField(max_length=45, blank=True, null=True)
    tel2 = models.CharField(max_length=45, blank=True, null=True)
    tel3 = models.CharField(max_length=45, blank=True, null=True)
    tel4 = models.CharField(max_length=45, blank=True, null=True)
    tel5 = models.CharField(max_length=45, blank=True, null=True)
    tel6 = models.CharField(max_length=45, blank=True, null=True)
    tel1_comment = models.CharField(max_length=145, blank=True, null=True)
    tel2_comment = models.CharField(max_length=145, blank=True, null=True)
    tel3_comment = models.CharField(max_length=145, blank=True, null=True)
    tel4_comment = models.CharField(max_length=345, blank=True, null=True)
    tel5_comment = models.CharField(max_length=145, blank=True, null=True)
    tel6_comment = models.CharField(max_length=145, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    contacts = models.CharField(max_length=445, blank=True, null=True)
    comment = models.CharField(max_length=1645, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    user_id2 = models.IntegerField(blank=True, null=True)
    user_ids = models.CharField(max_length=145, blank=True, null=True)
    user_ids_tmp = models.CharField(max_length=145, blank=True, null=True)
    user_ids_date = models.DateTimeField(blank=True, null=True)
    adv_type = models.IntegerField(blank=True, null=True)
    archive_check = models.IntegerField(blank=True, null=True)
    status_type = models.IntegerField(blank=True, null=True)
    status_enum = models.CharField(max_length=45, blank=True, null=True)
    show_all_check = models.IntegerField(blank=True, null=True)
    not_sms_agent_check = models.IntegerField(blank=True, null=True)
    client_enum = models.CharField(max_length=45, blank=True, null=True)
    deal_enum = models.CharField(max_length=45, blank=True, null=True)
    realty_enum = models.CharField(max_length=20, blank=True, null=True)
    addr = models.CharField(max_length=245, blank=True, null=True)
    deal_type = models.IntegerField(blank=True, null=True)
    np_auto = models.CharField(max_length=245, blank=True, null=True)
    rayon_types = models.CharField(max_length=245, blank=True, null=True)
    street = models.CharField(max_length=45, blank=True, null=True)
    dom = models.CharField(max_length=45, blank=True, null=True)
    drob = models.CharField(max_length=5, blank=True, null=True)
    str = models.CharField(max_length=45, blank=True, null=True)
    korp = models.CharField(max_length=45, blank=True, null=True)
    section_number = models.CharField(max_length=45, blank=True, null=True)
    kv = models.CharField(max_length=45, blank=True, null=True)
    flat_number = models.IntegerField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    floors = models.IntegerField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    area1 = models.FloatField(blank=True, null=True)
    area2 = models.FloatField(blank=True, null=True)
    area3 = models.FloatField(blank=True, null=True)
    area4 = models.CharField(max_length=45, blank=True, null=True)
    area5 = models.FloatField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    valuta_type = models.IntegerField(blank=True, null=True)
    geocode = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date1 = models.DateTimeField(blank=True, null=True)
    date2 = models.DateTimeField(blank=True, null=True)
    date3 = models.DateTimeField(blank=True, null=True)
    date4 = models.DateTimeField(blank=True, null=True)
    date5 = models.DateTimeField(blank=True, null=True)
    date6 = models.DateTimeField(blank=True, null=True)
    date7 = models.DateTimeField(blank=True, null=True)
    date8 = models.DateTimeField(blank=True, null=True)
    check1 = models.IntegerField(blank=True, null=True)
    check2 = models.IntegerField(blank=True, null=True)
    check3 = models.IntegerField(blank=True, null=True)
    check4 = models.IntegerField(blank=True, null=True)
    check5 = models.IntegerField(blank=True, null=True)
    check6 = models.IntegerField(blank=True, null=True)
    check7 = models.IntegerField(blank=True, null=True)
    check8 = models.IntegerField(blank=True, null=True)
    check9 = models.IntegerField(blank=True, null=True)
    check10 = models.IntegerField(blank=True, null=True)
    check11 = models.IntegerField(blank=True, null=True)
    check12 = models.IntegerField(blank=True, null=True)
    check13 = models.IntegerField(blank=True, null=True)
    check14 = models.IntegerField(blank=True, null=True)
    check15 = models.IntegerField(blank=True, null=True)
    check16 = models.IntegerField(blank=True, null=True)
    check17 = models.IntegerField(blank=True, null=True)
    check18 = models.IntegerField(blank=True, null=True)
    check19 = models.IntegerField(blank=True, null=True)
    check20 = models.IntegerField(blank=True, null=True)
    check21 = models.IntegerField(blank=True, null=True)
    check22 = models.IntegerField(blank=True, null=True)
    check23 = models.IntegerField(blank=True, null=True)
    check24 = models.IntegerField(blank=True, null=True)
    check25 = models.IntegerField(blank=True, null=True)
    check26 = models.IntegerField(blank=True, null=True)
    check27 = models.IntegerField(blank=True, null=True)
    check28 = models.IntegerField(blank=True, null=True)
    check29 = models.IntegerField(blank=True, null=True)
    check30 = models.IntegerField(blank=True, null=True)
    check31 = models.IntegerField(blank=True, null=True)
    check32 = models.IntegerField(blank=True, null=True)
    check33 = models.IntegerField(blank=True, null=True)
    check34 = models.IntegerField(blank=True, null=True)
    check35 = models.IntegerField(blank=True, null=True)
    check36 = models.IntegerField(blank=True, null=True)
    check37 = models.IntegerField(blank=True, null=True)
    check38 = models.IntegerField(blank=True, null=True)
    check39 = models.IntegerField(blank=True, null=True)
    check40 = models.IntegerField(blank=True, null=True)
    check41 = models.IntegerField(blank=True, null=True)
    param1 = models.CharField(max_length=45, blank=True, null=True)
    param2 = models.CharField(max_length=45, blank=True, null=True)
    param3 = models.CharField(max_length=80, blank=True, null=True)
    param4 = models.CharField(max_length=145, blank=True, null=True)
    param5 = models.CharField(max_length=45, blank=True, null=True)
    param6 = models.CharField(max_length=45, blank=True, null=True)
    param7 = models.CharField(max_length=45, blank=True, null=True)
    param8 = models.CharField(max_length=45, blank=True, null=True)
    param9 = models.CharField(max_length=45, blank=True, null=True)
    param10 = models.CharField(max_length=45, blank=True, null=True)
    param11 = models.CharField(max_length=45, blank=True, null=True)
    param12 = models.CharField(max_length=45, blank=True, null=True)
    param13 = models.CharField(max_length=45, blank=True, null=True)
    param14 = models.CharField(max_length=45, blank=True, null=True)
    param15 = models.CharField(max_length=45, blank=True, null=True)
    param16 = models.CharField(max_length=45, blank=True, null=True)
    param17 = models.CharField(max_length=345, blank=True, null=True)
    param18 = models.CharField(max_length=45, blank=True, null=True)
    param19 = models.CharField(max_length=45, blank=True, null=True)
    param20 = models.CharField(max_length=45, blank=True, null=True)
    param21 = models.CharField(max_length=45, blank=True, null=True)
    param22 = models.CharField(max_length=45, blank=True, null=True)
    param23 = models.CharField(max_length=45, blank=True, null=True)
    param24 = models.CharField(max_length=45, blank=True, null=True)
    param25 = models.CharField(max_length=45, blank=True, null=True)
    param26 = models.CharField(max_length=45, blank=True, null=True)
    param27 = models.CharField(max_length=45, blank=True, null=True)
    param28 = models.CharField(max_length=145, blank=True, null=True)
    param29 = models.CharField(max_length=60, blank=True, null=True)
    param30 = models.CharField(max_length=14, blank=True, null=True)
    param31 = models.CharField(max_length=37, blank=True, null=True)
    param100 = models.CharField(max_length=45, blank=True, null=True)
    param101 = models.CharField(max_length=45, blank=True, null=True)
    passport_group = models.IntegerField(blank=True, null=True)
    passport_number = models.CharField(max_length=45, blank=True, null=True)
    passport_serial = models.CharField(max_length=10, blank=True, null=True)
    passport_date = models.DateField(blank=True, null=True)
    passport_issued = models.CharField(max_length=345, blank=True, null=True)
    passport_kod = models.CharField(max_length=45, blank=True, null=True)
    passport_reg = models.CharField(max_length=345, blank=True, null=True)
    passport_live = models.CharField(max_length=545, blank=True, null=True)
    passport_born = models.CharField(max_length=445, blank=True, null=True)
    passport_inn = models.BigIntegerField(blank=True, null=True)
    passport_ogrn = models.BigIntegerField(blank=True, null=True)
    site_check1 = models.IntegerField(blank=True, null=True)
    site_check2 = models.IntegerField(blank=True, null=True)
    site_check3 = models.IntegerField(blank=True, null=True)
    site_check4 = models.IntegerField(blank=True, null=True)
    site_check5 = models.IntegerField(blank=True, null=True)
    site_check6 = models.IntegerField(blank=True, null=True)
    site_check7 = models.IntegerField(blank=True, null=True)
    site_check8 = models.IntegerField(blank=True, null=True)
    last_comment = models.CharField(max_length=1000, blank=True, null=True)
    last_work_date = models.DateTimeField(blank=True, null=True)
    last_work_user_id = models.IntegerField(blank=True, null=True)
    sex_enum = models.CharField(max_length=4, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    doc_enum = models.CharField(max_length=45, blank=True, null=True)
    doc_date = models.DateField(blank=True, null=True)
    doc_date_to = models.DateField(blank=True, null=True)
    doc_number = models.CharField(max_length=45, blank=True, null=True)
    area_room1 = models.FloatField(blank=True, null=True)
    area_room2 = models.FloatField(blank=True, null=True)
    area_room3 = models.FloatField(blank=True, null=True)
    area_room4 = models.FloatField(blank=True, null=True)
    area_room5 = models.FloatField(blank=True, null=True)
    area_room6 = models.FloatField(blank=True, null=True)
    area_balcon1 = models.FloatField(blank=True, null=True)
    area_balcon2 = models.FloatField(blank=True, null=True)
    area_balcon3 = models.FloatField(blank=True, null=True)
    way_type = models.IntegerField(blank=True, null=True)
    text1 = models.CharField(max_length=2000, blank=True, null=True)
    bc_id = models.IntegerField(blank=True, null=True)
    bc2_id = models.IntegerField(blank=True, null=True)
    bron_date = models.DateTimeField(blank=True, null=True)
    archive_date = models.DateTimeField(blank=True, null=True)
    blag_check = models.IntegerField(blank=True, null=True)
    new_hoto_check = models.IntegerField(blank=True, null=True)
    commission = models.IntegerField(blank=True, null=True)
    commission_enum = models.CharField(max_length=3, blank=True, null=True)
    commission_client = models.IntegerField(blank=True, null=True)
    commission_client_enum = models.CharField(max_length=3, blank=True, null=True)
    agency = models.CharField(max_length=345, blank=True, null=True)
    floor_enum = models.CharField(max_length=45, blank=True, null=True)
    site_check = models.IntegerField(blank=True, null=True)
    obl_rayon_auto = models.CharField(max_length=145, blank=True, null=True)
    np_rayon_auto = models.CharField(max_length=145, blank=True, null=True)
    way_auto = models.CharField(max_length=45, blank=True, null=True)
    realty_id = models.IntegerField(blank=True, null=True)
    jk_id = models.IntegerField(blank=True, null=True)
    pos_enum = models.CharField(max_length=20, blank=True, null=True)
    okrug_type = models.IntegerField(blank=True, null=True)
    district_type = models.IntegerField(blank=True, null=True)
    metro1_type = models.IntegerField(blank=True, null=True)
    metro2_type = models.IntegerField(blank=True, null=True)
    metro3_type = models.IntegerField(blank=True, null=True)
    to_metro_w = models.IntegerField(blank=True, null=True)
    to_metro_t = models.IntegerField(blank=True, null=True)
    obl_auto = models.CharField(max_length=45, blank=True, null=True)
    jk_name = models.CharField(max_length=145, blank=True, null=True)
    from_mkad = models.IntegerField(blank=True, null=True)
    from_way = models.IntegerField(blank=True, null=True)
    rooms_from = models.CharField(max_length=30, blank=True, null=True)
    cost_from = models.IntegerField(blank=True, null=True)
    area1_from = models.IntegerField(blank=True, null=True)
    area2_from = models.IntegerField(blank=True, null=True)
    kontr_check = models.IntegerField(blank=True, null=True)
    kontr_agency = models.CharField(max_length=65, blank=True, null=True)
    kontr_list = models.CharField(max_length=15, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    face_auto = models.CharField(max_length=45, blank=True, null=True)
    ex_check = models.IntegerField(blank=True, null=True)
    site_name = models.CharField(max_length=1000, blank=True, null=True)
    site_link = models.CharField(max_length=600, blank=True, null=True)
    site_text = models.CharField(max_length=2000, blank=True, null=True)
    alt_check = models.IntegerField(blank=True, null=True)
    nal_check = models.IntegerField(blank=True, null=True)
    ipoteka_check = models.IntegerField(blank=True, null=True)
    rassrochka_check = models.IntegerField(blank=True, null=True)
    np_rayon_auto2 = models.CharField(max_length=45, blank=True, null=True)
    np_rayon_auto3 = models.CharField(max_length=45, blank=True, null=True)
    np_rayon_auto4 = models.CharField(max_length=45, blank=True, null=True)
    np_rayon_auto5 = models.CharField(max_length=45, blank=True, null=True)
    np_rayon_auto6 = models.CharField(max_length=45, blank=True, null=True)
    street2 = models.CharField(max_length=45, blank=True, null=True)
    street3 = models.CharField(max_length=45, blank=True, null=True)
    street4 = models.CharField(max_length=45, blank=True, null=True)
    street5 = models.CharField(max_length=45, blank=True, null=True)
    ugl_check = models.IntegerField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    alt_client_id = models.IntegerField(blank=True, null=True)
    alt_realty_id = models.IntegerField(blank=True, null=True)
    kladr_city_id = models.CharField(max_length=20, blank=True, null=True)
    kladr_street_id = models.CharField(max_length=20, blank=True, null=True)
    assis_check = models.IntegerField(blank=True, null=True)
    afy_check = models.IntegerField(blank=True, null=True)
    floor_not_first_check = models.IntegerField(blank=True, null=True)
    floor_not_last_check = models.IntegerField(blank=True, null=True)
    contragent_id = models.IntegerField(blank=True, null=True)
    contragent_lot = models.IntegerField(blank=True, null=True)
    auto1 = models.CharField(max_length=45, blank=True, null=True)
    auto2 = models.CharField(max_length=45, blank=True, null=True)
    auto3 = models.CharField(max_length=45, blank=True, null=True)
    call_id = models.IntegerField(blank=True, null=True)
    sms_to_client_check = models.IntegerField(blank=True, null=True)
    commission_check = models.IntegerField(blank=True, null=True)
    show_admin_check = models.IntegerField(blank=True, null=True)
    assis_group = models.IntegerField(blank=True, null=True)
    rent_csv_md5 = models.CharField(max_length=32, blank=True, null=True)
    rek_check = models.IntegerField(blank=True, null=True)
    ged_check = models.IntegerField(blank=True, null=True)
    sobstv_check = models.IntegerField(blank=True, null=True)
    prichina = models.CharField(max_length=145, blank=True, null=True)
    alt_do_check = models.IntegerField(blank=True, null=True)
    irr_check = models.IntegerField(blank=True, null=True)
    russianrealty_check = models.IntegerField(blank=True, null=True)
    rbc_check = models.IntegerField(blank=True, null=True)
    realestate_check = models.IntegerField(blank=True, null=True)
    idinaidi_check = models.IntegerField(blank=True, null=True)
    bpn_check = models.IntegerField(blank=True, null=True)
    yandex_check = models.IntegerField(blank=True, null=True)
    cian_commerce_type = models.CharField(max_length=45, blank=True, null=True)
    cian_contract_type = models.CharField(max_length=31, blank=True, null=True)
    cian_phones = models.IntegerField(blank=True, null=True)
    cian_check = models.IntegerField(blank=True, null=True)
    cian_land_type = models.CharField(max_length=45, blank=True, null=True)
    cian_prepay = models.IntegerField(blank=True, null=True)
    cian_deposit_enum = models.CharField(max_length=3, blank=True, null=True)
    cian_deposit = models.IntegerField(blank=True, null=True)
    cian_agent = models.IntegerField(blank=True, null=True)
    cian_client = models.IntegerField(blank=True, null=True)
    cat_enum = models.CharField(max_length=13, blank=True, null=True)
    site_tel = models.CharField(max_length=25, blank=True, null=True)
    avito_check = models.IntegerField(blank=True, null=True)
    avito_commerce_enum = models.CharField(max_length=45, blank=True, null=True)
    avito_zem_enum = models.CharField(max_length=28, blank=True, null=True)
    yandex2_check = models.IntegerField(blank=True, null=True)
    stidio_check = models.IntegerField(blank=True, null=True)
    winner_check = models.IntegerField(blank=True, null=True)
    sob_check = models.IntegerField(blank=True, null=True)
    winner_status = models.CharField(max_length=52, blank=True, null=True)
    sob_type_check = models.IntegerField(blank=True, null=True)
    eip_check = models.IntegerField(blank=True, null=True)
    chance_check = models.IntegerField(blank=True, null=True)
    piter_realtor_check = models.IntegerField(blank=True, null=True)
    bsn_check = models.IntegerField(blank=True, null=True)
    restate_check = models.IntegerField(blank=True, null=True)
    kvmeter_check = models.IntegerField(blank=True, null=True)
    buy_do_check = models.IntegerField(blank=True, null=True)
    yandex3_check = models.IntegerField(blank=True, null=True)
    tel_concat = models.CharField(max_length=70, blank=True, null=True)
    site_select_check = models.IntegerField(blank=True, null=True)
    cost_update_date = models.DateField(blank=True, null=True)
    last_cost = models.IntegerField(blank=True, null=True)
    winner_aptp = models.CharField(max_length=45, blank=True, null=True)
    new_contact_check = models.IntegerField(blank=True, null=True)
    ged_premium_begin = models.DateField(blank=True, null=True)
    ged_premium_end = models.DateField(blank=True, null=True)
    load_check = models.IntegerField(blank=True, null=True)
    gazeta_text = models.CharField(max_length=1000, blank=True, null=True)
    all_to_sms_check = models.IntegerField(blank=True, null=True)
    all_to_email_check = models.IntegerField(blank=True, null=True)
    all_to_check = models.IntegerField(blank=True, null=True)
    video_link = models.CharField(max_length=100, blank=True, null=True)
    avito_asstatus_enum = models.CharField(max_length=9, blank=True, null=True)
    from_city = models.IntegerField(blank=True, null=True)
    ipoteka_do_check = models.IntegerField(blank=True, null=True)
    kvadrum_check = models.IntegerField(blank=True, null=True)
    emls_check = models.IntegerField(blank=True, null=True)
    avito_np_auto = models.CharField(max_length=25, blank=True, null=True)
    cost_m2_year = models.IntegerField(blank=True, null=True)
    yandex_promo_enum = models.CharField(max_length=11, blank=True, null=True)
    cian_promotions_enum = models.CharField(max_length=7, blank=True, null=True)
    cian_highlight_check = models.IntegerField(blank=True, null=True)
    fy_enum = models.CharField(max_length=8, blank=True, null=True)
    metro_types = models.CharField(max_length=145, blank=True, null=True)
    cost_m2_from = models.IntegerField(blank=True, null=True)
    cost_m2 = models.IntegerField(blank=True, null=True)
    voronka_type = models.IntegerField(blank=True, null=True)
    mail_check = models.IntegerField(blank=True, null=True)
    irr_product_name_enum = models.CharField(max_length=19, blank=True, null=True)
    kadastr = models.CharField(max_length=30, blank=True, null=True)
    dolya = models.CharField(max_length=10, blank=True, null=True)
    domclick_check = models.IntegerField(blank=True, null=True)
    yandex_building_id = models.IntegerField(blank=True, null=True)
    cian_jk_id = models.IntegerField(blank=True, null=True)
    cian_jk_korpus_id = models.IntegerField(blank=True, null=True)
    avito_jk_id = models.IntegerField(blank=True, null=True)
    cian_auction_bet = models.IntegerField(blank=True, null=True)
    reklama_check_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_client'
        app_label = 'crm_build'


class RlClientAdv(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    link = models.CharField(max_length=945, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_client_adv'
        app_label = 'crm_build'


class RlClientBank(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    bank = models.CharField(max_length=245, blank=True, null=True)
    status_enum = models.CharField(max_length=45, blank=True, null=True)
    check1 = models.IntegerField(blank=True, null=True)
    bank_date = models.DateField(blank=True, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_client_bank'
        app_label = 'crm_build'


class RlClientBirthday(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    status_enum = models.CharField(max_length=145, blank=True, null=True)
    check1 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_client_birthday'
        app_label = 'crm_build'


class RlClientOwner(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    realty_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    fio = models.CharField(max_length=145, blank=True, null=True)
    comment = models.CharField(max_length=345, blank=True, null=True)
    tel = models.CharField(max_length=145, blank=True, null=True)
    type_enum = models.CharField(max_length=145, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    site = models.CharField(max_length=145, blank=True, null=True)
    email = models.CharField(max_length=55, blank=True, null=True)
    company = models.CharField(max_length=145, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_client_owner'
        app_label = 'crm_build'


class RlClientOwnerAll(models.Model):
    row_id = models.IntegerField(unique=True, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    owner_id = models.IntegerField(primary_key=True)
    client_id = models.IntegerField()
    sys_date_create = models.DateTimeField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_client_owner_all'
        unique_together = (('owner_id', 'client_id'),)
        app_label = 'crm_build'


class RlClientRealtyCheck(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    realty_id = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=21, blank=True, null=True)
    comment = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_client_realty_check'
        app_label = 'crm_build'


class RlClientReportWeekly(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.IntegerField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    realty_id = models.IntegerField(blank=True, null=True)
    etap_check1 = models.IntegerField(blank=True, null=True)
    etap_check2 = models.IntegerField(blank=True, null=True)
    etap_check3 = models.IntegerField(blank=True, null=True)
    etap_check4 = models.IntegerField(blank=True, null=True)
    etap_check5 = models.IntegerField(blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    number_1param1 = models.CharField(db_column='1param1', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param2 = models.CharField(db_column='1param2', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param3 = models.CharField(db_column='1param3', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param4 = models.CharField(db_column='1param4', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param5 = models.CharField(db_column='1param5', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param6 = models.CharField(db_column='1param6', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param7 = models.CharField(db_column='1param7', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param8 = models.CharField(db_column='1param8', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param9 = models.CharField(db_column='1param9', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param10 = models.CharField(db_column='1param10', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param11 = models.CharField(db_column='1param11', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param12 = models.CharField(db_column='1param12', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param13 = models.CharField(db_column='1param13', max_length=2045, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param14 = models.CharField(db_column='1param14', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param15 = models.CharField(db_column='1param15', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1param16 = models.CharField(db_column='1param16', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1date1 = models.DateField(db_column='1date1', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1date2 = models.DateField(db_column='1date2', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2param1 = models.CharField(db_column='2param1', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2param2 = models.CharField(db_column='2param2', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2param3 = models.CharField(db_column='2param3', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2param4 = models.CharField(db_column='2param4', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2param5 = models.CharField(db_column='2param5', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2param6 = models.CharField(db_column='2param6', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2param7 = models.CharField(db_column='2param7', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2param8 = models.IntegerField(db_column='2param8', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2param9 = models.IntegerField(db_column='2param9', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2param10 = models.IntegerField(db_column='2param10', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2param11 = models.IntegerField(db_column='2param11', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2date1 = models.DateField(db_column='2date1', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param1 = models.CharField(db_column='3param1', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param2 = models.CharField(db_column='3param2', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param3 = models.CharField(db_column='3param3', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param4 = models.CharField(db_column='3param4', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param5 = models.CharField(db_column='3param5', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param6 = models.CharField(db_column='3param6', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param7 = models.CharField(db_column='3param7', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param8 = models.CharField(db_column='3param8', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param9 = models.CharField(db_column='3param9', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param10 = models.CharField(db_column='3param10', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param11 = models.CharField(db_column='3param11', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param12 = models.CharField(db_column='3param12', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param13 = models.CharField(db_column='3param13', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param14 = models.CharField(db_column='3param14', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param15 = models.CharField(db_column='3param15', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param16 = models.CharField(db_column='3param16', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param17 = models.CharField(db_column='3param17', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param18 = models.CharField(db_column='3param18', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param19 = models.CharField(db_column='3param19', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param20 = models.CharField(db_column='3param20', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param21 = models.CharField(db_column='3param21', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param22 = models.CharField(db_column='3param22', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param23 = models.CharField(db_column='3param23', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param24 = models.CharField(db_column='3param24', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date1 = models.DateField(db_column='3date1', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date2 = models.DateField(db_column='3date2', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param1 = models.CharField(db_column='4param1', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param2 = models.CharField(db_column='4param2', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param3 = models.CharField(db_column='4param3', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param4 = models.CharField(db_column='4param4', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param5 = models.CharField(db_column='4param5', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param6 = models.CharField(db_column='4param6', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param7 = models.CharField(db_column='4param7', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param8 = models.CharField(db_column='4param8', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param9 = models.CharField(db_column='4param9', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param10 = models.CharField(db_column='4param10', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param11 = models.CharField(db_column='4param11', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param12 = models.CharField(db_column='4param12', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param13 = models.CharField(db_column='4param13', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param14 = models.CharField(db_column='4param14', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param15 = models.CharField(db_column='4param15', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param16 = models.CharField(db_column='4param16', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param17 = models.CharField(db_column='4param17', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param18 = models.CharField(db_column='4param18', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param19 = models.CharField(db_column='4param19', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param20 = models.CharField(db_column='4param20', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param21 = models.CharField(db_column='4param21', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param22 = models.CharField(db_column='4param22', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param23 = models.CharField(db_column='4param23', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param24 = models.CharField(db_column='4param24', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param25 = models.CharField(db_column='4param25', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param26 = models.CharField(db_column='4param26', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param27 = models.CharField(db_column='4param27', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param28 = models.CharField(db_column='4param28', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param29 = models.CharField(db_column='4param29', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param30 = models.CharField(db_column='4param30', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param31 = models.CharField(db_column='4param31', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param32 = models.CharField(db_column='4param32', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param33 = models.CharField(db_column='4param33', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param34 = models.CharField(db_column='4param34', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param35 = models.CharField(db_column='4param35', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param36 = models.CharField(db_column='4param36', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param37 = models.CharField(db_column='4param37', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param38 = models.CharField(db_column='4param38', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param39 = models.CharField(db_column='4param39', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param40 = models.CharField(db_column='4param40', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param41 = models.CharField(db_column='4param41', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param42 = models.CharField(db_column='4param42', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param43 = models.CharField(db_column='4param43', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param44 = models.CharField(db_column='4param44', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param45 = models.CharField(db_column='4param45', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param46 = models.CharField(db_column='4param46', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param47 = models.CharField(db_column='4param47', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param48 = models.CharField(db_column='4param48', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param49 = models.CharField(db_column='4param49', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param50 = models.CharField(db_column='4param50', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param51 = models.CharField(db_column='4param51', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param52 = models.CharField(db_column='4param52', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param53 = models.CharField(db_column='4param53', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param54 = models.CharField(db_column='4param54', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param55 = models.CharField(db_column='4param55', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date1 = models.DateField(db_column='4date1', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date2 = models.DateField(db_column='4date2', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date3 = models.DateField(db_column='4date3', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date4 = models.DateField(db_column='4date4', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date5 = models.DateField(db_column='4date5', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date6 = models.DateField(db_column='4date6', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date7 = models.DateField(db_column='4date7', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date8 = models.DateField(db_column='4date8', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date9 = models.DateField(db_column='4date9', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date10 = models.DateField(db_column='4date10', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date11 = models.DateField(db_column='4date11', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date12 = models.DateField(db_column='4date12', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date13 = models.DateField(db_column='4date13', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date14 = models.DateField(db_column='4date14', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date15 = models.DateField(db_column='4date15', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date16 = models.DateField(db_column='4date16', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date17 = models.DateField(db_column='4date17', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date18 = models.DateField(db_column='4date18', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date19 = models.DateField(db_column='4date19', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date20 = models.DateField(db_column='4date20', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date21 = models.DateField(db_column='4date21', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date22 = models.DateField(db_column='4date22', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date23 = models.DateField(db_column='4date23', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date24 = models.DateField(db_column='4date24', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date25 = models.DateField(db_column='4date25', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date26 = models.DateField(db_column='4date26', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date27 = models.DateField(db_column='4date27', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date28 = models.DateField(db_column='4date28', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date29 = models.DateTimeField(db_column='4date29', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date30 = models.DateField(db_column='4date30', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5date1 = models.DateField(db_column='5date1', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5date2 = models.DateField(db_column='5date2', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5date3 = models.DateField(db_column='5date3', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5date4 = models.DateField(db_column='5date4', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    etap_enum = models.CharField(max_length=145, blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    type_enum = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=145, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    number_3date3 = models.DateField(db_column='3date3', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date4 = models.DateField(db_column='3date4', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date5 = models.DateField(db_column='3date5', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date6 = models.DateField(db_column='3date6', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date7 = models.DateField(db_column='3date7', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date8 = models.DateField(db_column='3date8', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    opeka_check = models.IntegerField(blank=True, null=True)
    ipoteka_check = models.IntegerField(blank=True, null=True)
    copy_to_user_id = models.IntegerField(blank=True, null=True)
    copy_to_me = models.IntegerField(blank=True, null=True)
    recomendation = models.CharField(max_length=2500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_client_report_weekly'
        app_label = 'crm_build'


class RlContragent(models.Model):
    row_id = models.IntegerField(unique=True)
    lot = models.AutoField(primary_key=True)
    name = models.CharField(max_length=145, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_update = models.DateTimeField(blank=True, null=True)
    fio = models.CharField(max_length=145, blank=True, null=True)
    fff = models.CharField(max_length=45, blank=True, null=True)
    iii = models.CharField(max_length=45, blank=True, null=True)
    ooo = models.CharField(max_length=45, blank=True, null=True)
    tel1 = models.CharField(max_length=45, blank=True, null=True)
    tel2 = models.CharField(max_length=45, blank=True, null=True)
    tel3 = models.CharField(max_length=45, blank=True, null=True)
    tel4 = models.CharField(max_length=45, blank=True, null=True)
    tel1_comment = models.CharField(max_length=145, blank=True, null=True)
    tel2_comment = models.CharField(max_length=145, blank=True, null=True)
    tel3_comment = models.CharField(max_length=145, blank=True, null=True)
    tel4_comment = models.CharField(max_length=345, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    contacts = models.CharField(max_length=445, blank=True, null=True)
    comment = models.CharField(max_length=1645, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    adv_type = models.IntegerField(blank=True, null=True)
    archive_check = models.IntegerField(blank=True, null=True)
    status_type = models.IntegerField(blank=True, null=True)
    status_enum = models.CharField(max_length=45, blank=True, null=True)
    show_all_check = models.IntegerField(blank=True, null=True)
    not_sms_agent_check = models.IntegerField(blank=True, null=True)
    client_enum = models.CharField(max_length=45, blank=True, null=True)
    deal_enum = models.CharField(max_length=45, blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateTimeField(blank=True, null=True)
    date3 = models.DateTimeField(blank=True, null=True)
    check1 = models.IntegerField(blank=True, null=True)
    check2 = models.IntegerField(blank=True, null=True)
    check3 = models.IntegerField(blank=True, null=True)
    param1 = models.CharField(max_length=45, blank=True, null=True)
    param2 = models.CharField(max_length=45, blank=True, null=True)
    param3 = models.CharField(max_length=45, blank=True, null=True)
    passport_group = models.IntegerField(blank=True, null=True)
    passport_number = models.CharField(max_length=45, blank=True, null=True)
    passport_serial = models.CharField(max_length=10, blank=True, null=True)
    passport_date = models.DateField(blank=True, null=True)
    passport_issued = models.CharField(max_length=345, blank=True, null=True)
    passport_kod = models.CharField(max_length=45, blank=True, null=True)
    passport_reg = models.CharField(max_length=345, blank=True, null=True)
    passport_live = models.CharField(max_length=545, blank=True, null=True)
    passport_born = models.CharField(max_length=445, blank=True, null=True)
    last_comment = models.CharField(max_length=1000, blank=True, null=True)
    last_work_date = models.DateTimeField(blank=True, null=True)
    last_work_user_id = models.IntegerField(blank=True, null=True)
    sex_enum = models.CharField(max_length=4, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    archive_date = models.DateTimeField(blank=True, null=True)
    agency = models.CharField(max_length=345, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_contragent'
        app_label = 'crm_build'


class RlDeal(models.Model):
    row_id = models.IntegerField(unique=True)
    lot = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    realty_id = models.IntegerField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    user_id2 = models.IntegerField(blank=True, null=True)
    etap_type = models.IntegerField(blank=True, null=True)
    avans_date = models.DateField(blank=True, null=True)
    avans_time = models.IntegerField(blank=True, null=True)
    avans_cost = models.IntegerField(blank=True, null=True)
    deal_date = models.DateField(blank=True, null=True)
    deal_cost = models.IntegerField(blank=True, null=True)
    deal_cost2 = models.IntegerField(blank=True, null=True)
    deal_doc_type = models.IntegerField(blank=True, null=True)
    deal_end_date = models.DateField(blank=True, null=True)
    deal_flat_date = models.DateField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    etap_check3 = models.IntegerField(blank=True, null=True)
    etap_check4 = models.IntegerField(blank=True, null=True)
    etap_check5 = models.IntegerField(blank=True, null=True)
    number_3param1 = models.CharField(db_column='3param1', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param2 = models.CharField(db_column='3param2', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param3 = models.CharField(db_column='3param3', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param4 = models.CharField(db_column='3param4', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param5 = models.CharField(db_column='3param5', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param6 = models.CharField(db_column='3param6', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param7 = models.CharField(db_column='3param7', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param8 = models.CharField(db_column='3param8', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param9 = models.CharField(db_column='3param9', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param10 = models.CharField(db_column='3param10', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param11 = models.CharField(db_column='3param11', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param12 = models.CharField(db_column='3param12', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param13 = models.CharField(db_column='3param13', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param14 = models.CharField(db_column='3param14', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param15 = models.CharField(db_column='3param15', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param16 = models.CharField(db_column='3param16', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param17 = models.CharField(db_column='3param17', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param18 = models.CharField(db_column='3param18', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param19 = models.CharField(db_column='3param19', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param20 = models.CharField(db_column='3param20', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param21 = models.CharField(db_column='3param21', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param22 = models.CharField(db_column='3param22', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param23 = models.CharField(db_column='3param23', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3param24 = models.CharField(db_column='3param24', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date1 = models.DateField(db_column='3date1', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date2 = models.DateField(db_column='3date2', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param1 = models.CharField(db_column='4param1', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param2 = models.CharField(db_column='4param2', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param3 = models.CharField(db_column='4param3', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param4 = models.CharField(db_column='4param4', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param5 = models.CharField(db_column='4param5', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param6 = models.CharField(db_column='4param6', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param7 = models.CharField(db_column='4param7', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param8 = models.CharField(db_column='4param8', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param9 = models.CharField(db_column='4param9', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param10 = models.CharField(db_column='4param10', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param11 = models.CharField(db_column='4param11', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param12 = models.CharField(db_column='4param12', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param13 = models.CharField(db_column='4param13', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param14 = models.CharField(db_column='4param14', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param15 = models.CharField(db_column='4param15', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param16 = models.CharField(db_column='4param16', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param17 = models.CharField(db_column='4param17', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param18 = models.CharField(db_column='4param18', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param19 = models.CharField(db_column='4param19', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param20 = models.CharField(db_column='4param20', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param21 = models.CharField(db_column='4param21', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param22 = models.CharField(db_column='4param22', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param23 = models.CharField(db_column='4param23', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param24 = models.CharField(db_column='4param24', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param25 = models.CharField(db_column='4param25', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param26 = models.CharField(db_column='4param26', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param27 = models.CharField(db_column='4param27', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param28 = models.CharField(db_column='4param28', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param29 = models.CharField(db_column='4param29', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param30 = models.CharField(db_column='4param30', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param31 = models.CharField(db_column='4param31', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param32 = models.CharField(db_column='4param32', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param33 = models.CharField(db_column='4param33', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param34 = models.CharField(db_column='4param34', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param35 = models.CharField(db_column='4param35', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param36 = models.CharField(db_column='4param36', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param37 = models.CharField(db_column='4param37', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param38 = models.CharField(db_column='4param38', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param39 = models.CharField(db_column='4param39', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param40 = models.CharField(db_column='4param40', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param41 = models.CharField(db_column='4param41', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param42 = models.CharField(db_column='4param42', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param43 = models.CharField(db_column='4param43', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param44 = models.CharField(db_column='4param44', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param45 = models.CharField(db_column='4param45', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param46 = models.CharField(db_column='4param46', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param47 = models.CharField(db_column='4param47', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param48 = models.CharField(db_column='4param48', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param49 = models.CharField(db_column='4param49', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param50 = models.CharField(db_column='4param50', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param51 = models.CharField(db_column='4param51', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param52 = models.CharField(db_column='4param52', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param53 = models.CharField(db_column='4param53', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param54 = models.CharField(db_column='4param54', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4param55 = models.CharField(db_column='4param55', max_length=145, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date1 = models.DateField(db_column='4date1', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date2 = models.DateField(db_column='4date2', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date3 = models.DateField(db_column='4date3', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date4 = models.DateField(db_column='4date4', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date5 = models.DateField(db_column='4date5', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date6 = models.DateField(db_column='4date6', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date7 = models.DateField(db_column='4date7', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date8 = models.DateField(db_column='4date8', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date9 = models.DateField(db_column='4date9', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date10 = models.DateField(db_column='4date10', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date11 = models.DateField(db_column='4date11', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date12 = models.DateField(db_column='4date12', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date13 = models.DateField(db_column='4date13', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date14 = models.DateField(db_column='4date14', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date15 = models.DateField(db_column='4date15', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date16 = models.DateField(db_column='4date16', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date17 = models.DateField(db_column='4date17', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date18 = models.DateField(db_column='4date18', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date19 = models.DateField(db_column='4date19', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date20 = models.DateField(db_column='4date20', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date21 = models.DateField(db_column='4date21', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date22 = models.DateField(db_column='4date22', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date23 = models.DateField(db_column='4date23', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date24 = models.DateField(db_column='4date24', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date25 = models.DateField(db_column='4date25', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date26 = models.DateField(db_column='4date26', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date27 = models.DateField(db_column='4date27', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date28 = models.DateField(db_column='4date28', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date29 = models.DateTimeField(db_column='4date29', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4date30 = models.DateField(db_column='4date30', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5date1 = models.DateField(db_column='5date1', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5date2 = models.DateField(db_column='5date2', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5date3 = models.DateField(db_column='5date3', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5date4 = models.DateField(db_column='5date4', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date3 = models.DateField(db_column='3date3', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date4 = models.DateField(db_column='3date4', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date5 = models.DateField(db_column='3date5', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date6 = models.DateField(db_column='3date6', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date7 = models.DateField(db_column='3date7', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3date8 = models.DateField(db_column='3date8', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    opeka_check = models.IntegerField(blank=True, null=True)
    ipoteka_check = models.IntegerField(blank=True, null=True)
    deal_type = models.IntegerField(blank=True, null=True)
    doc_pay_check = models.IntegerField(blank=True, null=True)
    doc_rashod_check = models.IntegerField(blank=True, null=True)
    archive_check = models.IntegerField(blank=True, null=True)
    actual_date = models.DateField(blank=True, null=True)
    status_enum = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_deal'
        app_label = 'crm_build'


class RlDealOwner(models.Model):
    row_id = models.IntegerField(primary_key=True)
    user = models.IntegerField(blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    birthday_date = models.DateField(blank=True, null=True)
    proportion = models.CharField(max_length=45, blank=True, null=True)
    passport = models.CharField(max_length=145, blank=True, null=True)
    issue = models.CharField(max_length=145, blank=True, null=True)
    kp = models.CharField(max_length=145, blank=True, null=True)
    reg_text = models.CharField(max_length=345, blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    deal_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_deal_owner'
        app_label = 'crm_build'


class RlDealPay(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    deal_id = models.IntegerField(blank=True, null=True)
    summ_plan = models.IntegerField(blank=True, null=True)
    date_plan = models.DateField(blank=True, null=True)
    summ_fact = models.IntegerField(blank=True, null=True)
    date_fact = models.DateField(blank=True, null=True)
    comment = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_deal_pay'
        app_label = 'crm_build'


class RlDealRashod(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    deal_id = models.IntegerField(blank=True, null=True)
    summ = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=545, blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    rashod_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_deal_rashod'
        app_label = 'crm_build'


class RlJk(models.Model):
    row_id = models.IntegerField(unique=True)
    lot = models.AutoField(primary_key=True)
    name = models.CharField(max_length=145, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    status_enum = models.CharField(max_length=45, blank=True, null=True)
    jk_enum = models.CharField(max_length=45, blank=True, null=True)
    jk_name = models.CharField(max_length=45, blank=True, null=True)
    addr = models.CharField(max_length=245, blank=True, null=True)
    np_auto = models.CharField(max_length=245, blank=True, null=True)
    street = models.CharField(max_length=45, blank=True, null=True)
    dom = models.CharField(max_length=45, blank=True, null=True)
    str = models.CharField(max_length=45, blank=True, null=True)
    korp = models.CharField(max_length=45, blank=True, null=True)
    kv = models.CharField(max_length=45, blank=True, null=True)
    floors = models.IntegerField(blank=True, null=True)
    geocode = models.CharField(max_length=45, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    param1 = models.CharField(max_length=45, blank=True, null=True)
    param2 = models.CharField(max_length=45, blank=True, null=True)
    param3 = models.CharField(max_length=45, blank=True, null=True)
    param4 = models.CharField(max_length=45, blank=True, null=True)
    param5 = models.IntegerField(blank=True, null=True)
    param6 = models.IntegerField(blank=True, null=True)
    param7 = models.CharField(max_length=45, blank=True, null=True)
    param8 = models.CharField(max_length=45, blank=True, null=True)
    param9 = models.CharField(max_length=145, blank=True, null=True)
    param10 = models.CharField(max_length=100, blank=True, null=True)
    param11 = models.CharField(max_length=20, blank=True, null=True)
    param12 = models.CharField(max_length=20, blank=True, null=True)
    site_check = models.IntegerField(blank=True, null=True)
    obl_rayon_auto = models.CharField(max_length=145, blank=True, null=True)
    np_rayon_auto = models.CharField(max_length=145, blank=True, null=True)
    way_auto = models.CharField(max_length=45, blank=True, null=True)
    pos_enum = models.CharField(max_length=20, blank=True, null=True)
    okrug_type = models.IntegerField(blank=True, null=True)
    district_type = models.IntegerField(blank=True, null=True)
    metro1_type = models.IntegerField(blank=True, null=True)
    metro2_type = models.IntegerField(blank=True, null=True)
    metro3_type = models.IntegerField(blank=True, null=True)
    to_metro_w = models.IntegerField(blank=True, null=True)
    to_metro_t = models.IntegerField(blank=True, null=True)
    obl_auto = models.CharField(max_length=45, blank=True, null=True)
    drob = models.CharField(max_length=5, blank=True, null=True)
    area1_from = models.IntegerField(blank=True, null=True)
    area1_to = models.IntegerField(blank=True, null=True)
    cost_from = models.IntegerField(blank=True, null=True)
    cost_to = models.IntegerField(blank=True, null=True)
    check1 = models.IntegerField(blank=True, null=True)
    check2 = models.IntegerField(blank=True, null=True)
    check3 = models.IntegerField(blank=True, null=True)
    check4 = models.IntegerField(blank=True, null=True)
    check5 = models.IntegerField(blank=True, null=True)
    check6 = models.IntegerField(blank=True, null=True)
    check7 = models.IntegerField(blank=True, null=True)
    check8 = models.IntegerField(blank=True, null=True)
    check9 = models.IntegerField(blank=True, null=True)
    check10 = models.IntegerField(blank=True, null=True)
    check11 = models.IntegerField(blank=True, null=True)
    check12 = models.IntegerField(blank=True, null=True)
    check13 = models.IntegerField(blank=True, null=True)
    check14 = models.IntegerField(blank=True, null=True)
    check15 = models.IntegerField(blank=True, null=True)
    check16 = models.IntegerField(blank=True, null=True)
    check17 = models.IntegerField(blank=True, null=True)
    from_mkad = models.IntegerField(blank=True, null=True)
    from_way = models.IntegerField(blank=True, null=True)
    way_auto2 = models.CharField(max_length=45, blank=True, null=True)
    way_auto3 = models.CharField(max_length=45, blank=True, null=True)
    valuta_type = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    area1 = models.IntegerField(blank=True, null=True)
    area2 = models.IntegerField(blank=True, null=True)
    cost1 = models.IntegerField(blank=True, null=True)
    cost2 = models.IntegerField(blank=True, null=True)
    cost3 = models.IntegerField(blank=True, null=True)
    cost1_valuta = models.IntegerField(blank=True, null=True)
    cost2_valuta = models.IntegerField(blank=True, null=True)
    cost3_valuta = models.IntegerField(blank=True, null=True)
    param13 = models.CharField(max_length=20, blank=True, null=True)
    param14 = models.CharField(max_length=20, blank=True, null=True)
    param15 = models.CharField(max_length=20, blank=True, null=True)
    param16 = models.CharField(max_length=20, blank=True, null=True)
    param17 = models.CharField(max_length=80, blank=True, null=True)
    param18 = models.CharField(max_length=45, blank=True, null=True)
    param19 = models.CharField(max_length=20, blank=True, null=True)
    param20 = models.CharField(max_length=20, blank=True, null=True)
    param21 = models.CharField(max_length=45, blank=True, null=True)
    param22 = models.CharField(max_length=45, blank=True, null=True)
    param23 = models.CharField(max_length=45, blank=True, null=True)
    param24 = models.CharField(max_length=330, blank=True, null=True)
    param25 = models.CharField(max_length=350, blank=True, null=True)
    param26 = models.CharField(max_length=45, blank=True, null=True)
    param27 = models.CharField(max_length=20, blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    project_url = models.CharField(max_length=345, blank=True, null=True)
    yandex_building_id = models.IntegerField(blank=True, null=True)
    cian_jk_id = models.IntegerField(blank=True, null=True)
    cian_jk_korpus_id = models.IntegerField(blank=True, null=True)
    avito_jk_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_jk'
        app_label = 'crm_build'


class RlJkSection(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    jk_id = models.IntegerField(blank=True, null=True)
    section_number = models.IntegerField(blank=True, null=True)
    section_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_jk_section'
        app_label = 'crm_build'


class RlJkSectionFloor(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    section_id = models.IntegerField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    floor_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_jk_section_floor'
        app_label = 'crm_build'


class RlLoadCall(models.Model):
    lot = models.AutoField(primary_key=True)
    row_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    service = models.CharField(max_length=245, blank=True, null=True)
    type = models.CharField(max_length=245, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tel = models.CharField(max_length=45, blank=True, null=True)
    tel_from = models.CharField(max_length=45, blank=True, null=True)
    tel_to = models.CharField(max_length=45, blank=True, null=True)
    prev_count = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    duration = models.CharField(max_length=45, blank=True, null=True)
    client_id = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_load_call'
        app_label = 'crm_build'


class RlLoadCallClient(models.Model):
    load_call_id = models.BigIntegerField(primary_key=True)
    client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rl_load_call_client'
        unique_together = (('load_call_id', 'client_id'),)
        app_label = 'crm_build'


class RlParser(models.Model):
    row_id = models.AutoField(primary_key=True)
    sys_project_id = models.IntegerField()
    user = models.IntegerField()
    sys_date_create = models.DateTimeField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    id = models.IntegerField(unique=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    source = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=145, blank=True, null=True)
    square = models.CharField(max_length=45, blank=True, null=True)
    contactphone = models.IntegerField(blank=True, null=True)
    contactperson = models.CharField(max_length=145, blank=True, null=True)
    roomcount = models.IntegerField(blank=True, null=True)
    countphone = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=145, blank=True, null=True)
    type = models.CharField(max_length=19, blank=True, null=True)
    photo = models.IntegerField(blank=True, null=True)
    image1 = models.CharField(max_length=300, blank=True, null=True)
    image2 = models.CharField(max_length=300, blank=True, null=True)
    image3 = models.CharField(max_length=300, blank=True, null=True)
    image4 = models.CharField(max_length=300, blank=True, null=True)
    image5 = models.CharField(max_length=300, blank=True, null=True)
    image6 = models.CharField(max_length=300, blank=True, null=True)
    tel = models.CharField(max_length=145, blank=True, null=True)
    link = models.CharField(max_length=450, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    realty_enum = models.CharField(max_length=45, blank=True, null=True)
    not_sms_agent_check = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=2000, blank=True, null=True)
    sobstv_check = models.IntegerField(blank=True, null=True)
    kontr_check = models.IntegerField(blank=True, null=True)
    kontr_agency = models.CharField(max_length=45, blank=True, null=True)
    kontr_list = models.CharField(max_length=6, blank=True, null=True)
    obj_id = models.IntegerField(blank=True, null=True)
    rl_parsercol = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_parser'
        app_label = 'crm_build'


class RlParser2(models.Model):
    id = models.IntegerField(primary_key=True)
    dt = models.DateTimeField(blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)
    url = models.CharField(max_length=145, blank=True, null=True)
    address = models.CharField(max_length=145, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    fio = models.CharField(max_length=45, blank=True, null=True)
    photo = models.CharField(max_length=500, blank=True, null=True)
    phone_find = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    type_ad = models.CharField(max_length=45, blank=True, null=True)
    material = models.CharField(max_length=45, blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    floors_house = models.IntegerField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=20, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    sub_type = models.CharField(max_length=45, blank=True, null=True)
    metro = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=145, blank=True, null=True)
    region_id = models.IntegerField(db_column='region_Id', blank=True, null=True)  # Field name made lowercase.
    commission = models.CharField(max_length=45, blank=True, null=True)
    latitude = models.CharField(max_length=45, blank=True, null=True)
    longitude = models.CharField(max_length=45, blank=True, null=True)
    source = models.CharField(max_length=45, blank=True, null=True)
    kitchen_area = models.IntegerField(blank=True, null=True)
    agent = models.IntegerField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_parser2'
        app_label = 'crm_build'


class RlParser4(models.Model):
    row_id = models.IntegerField(primary_key=True)
    id = models.BigIntegerField(blank=True, null=True)
    url = models.CharField(max_length=245, blank=True, null=True)
    title = models.CharField(max_length=145, blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    phone_operator = models.CharField(max_length=45, blank=True, null=True)
    person = models.CharField(max_length=45, blank=True, null=True)
    person_type = models.CharField(max_length=21, blank=True, null=True)
    person_type_id = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=145, blank=True, null=True)
    metro = models.CharField(max_length=45, blank=True, null=True)
    rayon = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=145, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    nedvigimost_type = models.CharField(max_length=7, blank=True, null=True)
    nedvigimost_type_id = models.IntegerField(blank=True, null=True)
    avitoid = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=145, blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    params = models.TextField(blank=True, null=True)
    cat1_id = models.IntegerField(blank=True, null=True)
    cat2_id = models.IntegerField(blank=True, null=True)
    cat1 = models.CharField(max_length=45, blank=True, null=True)
    cat2 = models.CharField(max_length=45, blank=True, null=True)
    coords = models.CharField(max_length=45, blank=True, null=True)
    region = models.CharField(max_length=45, blank=True, null=True)
    city1 = models.CharField(max_length=45, blank=True, null=True)
    count_ads_same_phone = models.IntegerField(blank=True, null=True)
    phone_protected = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    kolichestvo_komnat = models.CharField(db_column='Kolichestvo_komnat', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vid_obekta = models.CharField(db_column='Vid_obekta', max_length=40, blank=True, null=True)  # Field name made lowercase.
    plocshad = models.CharField(db_column='Plocshad', max_length=15, blank=True, null=True)  # Field name made lowercase.
    etazh = models.CharField(db_column='Etazh', max_length=15, blank=True, null=True)  # Field name made lowercase.
    etazhej_v_dome = models.CharField(db_column='Etazhej_v_dome', max_length=20, blank=True, null=True)  # Field name made lowercase.
    plocshad_kuhni = models.CharField(db_column='Plocshad_kuhni', max_length=15, blank=True, null=True)  # Field name made lowercase.
    zhilaya_plocshad = models.CharField(db_column='ZHilaya_plocshad', max_length=15, blank=True, null=True)  # Field name made lowercase.
    srok_arendy = models.CharField(db_column='Srok_arendy', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tip_doma = models.CharField(db_column='Tip_doma', max_length=45, blank=True, null=True)  # Field name made lowercase.
    komnat_v_kvartire = models.CharField(db_column='Komnat_v_kvartire', max_length=20, blank=True, null=True)  # Field name made lowercase.
    komissiya = models.CharField(db_column='Komissiya', max_length=20, blank=True, null=True)  # Field name made lowercase.
    zalog = models.CharField(db_column='Zalog', max_length=20, blank=True, null=True)  # Field name made lowercase.
    razmer_komissii = models.CharField(db_column='Razmer_komissii', max_length=20, blank=True, null=True)  # Field name made lowercase.
    plocshad_uchastka = models.CharField(db_column='Plocshad_uchastka', max_length=20, blank=True, null=True)  # Field name made lowercase.
    plocshad_doma = models.CharField(db_column='Plocshad_doma', max_length=20, blank=True, null=True)  # Field name made lowercase.
    material_sten = models.CharField(db_column='Material_sten', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rasstoyanie_do_goroda = models.CharField(db_column='Rasstoyanie_do_goroda', max_length=20, blank=True, null=True)  # Field name made lowercase.
    kategoriya_zemel = models.CharField(db_column='Kategoriya_zemel', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ohrana = models.CharField(db_column='Ohrana', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tip_garazha = models.CharField(db_column='Tip_garazha', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tip_mashinomesta = models.CharField(db_column='Tip_mashinomesta', max_length=45, blank=True, null=True)  # Field name made lowercase.
    klass_zdaniya = models.CharField(db_column='Klass_zdaniya', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tip_obyavleniya = models.CharField(db_column='Tip_obyavleniya', max_length=20, blank=True, null=True)  # Field name made lowercase.
    plocshad_komnaty = models.CharField(db_column='Plocshad_komnaty', max_length=20, blank=True, null=True)  # Field name made lowercase.
    main_image = models.CharField(max_length=145, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    check_check = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_parser4'
        app_label = 'crm_build'


class RlRealtySite(models.Model):
    row_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    realty_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_realty_site'
        app_label = 'crm_build'


class RlSber(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    fio = models.CharField(max_length=45, blank=True, null=True)
    born_date = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    passport = models.CharField(max_length=45, blank=True, null=True)
    residential_address = models.CharField(max_length=245, blank=True, null=True)
    work_address = models.CharField(max_length=245, blank=True, null=True)
    request_id = models.IntegerField(blank=True, null=True)
    to_bank_check = models.IntegerField(blank=True, null=True)
    is_draft = models.IntegerField(blank=True, null=True)
    office_id = models.IntegerField(blank=True, null=True)
    object_type_id = models.CharField(max_length=25, blank=True, null=True)
    sum_request = models.IntegerField(blank=True, null=True)
    sum_supposes = models.IntegerField(blank=True, null=True)
    agent_email = models.CharField(max_length=45, blank=True, null=True)
    responsible_agent_email = models.CharField(max_length=45, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    to_bank_date = models.DateTimeField(blank=True, null=True)
    status_enum = models.CharField(max_length=45, blank=True, null=True)
    next_contact_date = models.DateTimeField(blank=True, null=True)
    is_training = models.IntegerField(blank=True, null=True)
    notice_status_check = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_sber'
        app_label = 'crm_build'


class RlShow(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    call_id = models.IntegerField(blank=True, null=True)
    show_enum = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    notified_type = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=4000, blank=True, null=True)
    result_check = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=4000, blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    realty_id = models.IntegerField(blank=True, null=True)
    kontr_id = models.IntegerField(blank=True, null=True)
    to_sms_check = models.IntegerField(blank=True, null=True)
    to_email_check = models.IntegerField(blank=True, null=True)
    check_check = models.IntegerField(blank=True, null=True)
    deal_id = models.IntegerField(blank=True, null=True)
    notified_check = models.IntegerField(blank=True, null=True)
    contragent_id = models.IntegerField(blank=True, null=True)
    contragent_id1 = models.IntegerField(blank=True, null=True)
    contragent_id2 = models.IntegerField(blank=True, null=True)
    notified_new_check = models.IntegerField(blank=True, null=True)
    result_enum = models.CharField(max_length=3, blank=True, null=True)
    show_enum_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_show'
        app_label = 'crm_build'


class SysComment(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    obj_id = models.IntegerField(blank=True, null=True)
    obj_card_name = models.CharField(max_length=45, blank=True, null=True)
    obj_table_name = models.CharField(max_length=45, blank=True, null=True)
    comment = models.CharField(max_length=2000, blank=True, null=True)
    param1 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_comment'
        app_label = 'crm_build'


class SysDop(models.Model):
    row_id = models.AutoField(primary_key=True)
    global_field = models.CharField(db_column='global', max_length=45, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    obj_name = models.CharField(max_length=45, blank=True, null=True)
    col = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    before = models.CharField(max_length=45, blank=True, null=True)
    filter = models.CharField(max_length=245, blank=True, null=True)
    element = models.TextField(blank=True, null=True)
    not_exists = models.IntegerField(blank=True, null=True)
    readonly = models.IntegerField(blank=True, null=True)
    required = models.IntegerField(blank=True, null=True)
    not_required = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_dop'
        app_label = 'crm_build'


class SysHist(models.Model):
    row_id = models.IntegerField(primary_key=True)
    table_name = models.CharField(max_length=45, blank=True, null=True)
    obj_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    field = models.CharField(max_length=45, blank=True, null=True)
    value = models.CharField(max_length=500, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    user = models.CharField(max_length=45, blank=True, null=True)
    value_id = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_hist'
        app_label = 'crm_build'


class SysLock(models.Model):
    obj_id = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    table_name = models.CharField(max_length=45, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    lock_time = models.IntegerField(blank=True, null=True)
    win_id = models.CharField(max_length=45, blank=True, null=True)
    win_mode = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_lock'
        app_label = 'crm_build'


class SysNotice(models.Model):
    notice_name = models.CharField(max_length=45, blank=True, null=True)
    table_name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    from_user_id = models.IntegerField(blank=True, null=True)
    from_sys = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=245, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    obj_id = models.IntegerField(blank=True, null=True)
    obj_card_name = models.CharField(max_length=45, blank=True, null=True)
    notice_date = models.DateTimeField(blank=True, null=True)
    cenceled = models.TextField(blank=True, null=True)  # This field type is a guess.
    cache = models.CharField(max_length=45, blank=True, null=True)
    to_role_ids = models.CharField(max_length=345, blank=True, null=True)
    to_user_ids = models.CharField(max_length=345, blank=True, null=True)
    type_enum = models.CharField(max_length=9, blank=True, null=True)
    to_all_check = models.IntegerField(blank=True, null=True)
    to_online_check = models.IntegerField(blank=True, null=True)
    row_id = models.IntegerField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    to_user_check = models.IntegerField(blank=True, null=True)
    to_teh_check = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    support_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    to_sms_check = models.IntegerField(blank=True, null=True)
    to_email_check = models.IntegerField(blank=True, null=True)
    bold_check = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_notice'
        app_label = 'crm_build'


class SysNoticeCrsUser(models.Model):
    notice_id = models.IntegerField(blank=True, null=True)
    to_user_id = models.IntegerField(blank=True, null=True)
    date_readed = models.DateTimeField(blank=True, null=True)
    date_defer = models.DateTimeField(blank=True, null=True)
    row_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_notice_crs_user'
        app_label = 'crm_build'


class SysOffice(models.Model):
    row_id = models.IntegerField(primary_key=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    addr = models.CharField(max_length=445, blank=True, null=True)
    rs = models.CharField(max_length=45, blank=True, null=True)
    rsg = models.CharField(max_length=445, blank=True, null=True)
    kpp = models.CharField(max_length=45, blank=True, null=True)
    inn = models.CharField(max_length=45, blank=True, null=True)
    ogrn = models.CharField(max_length=45, blank=True, null=True)
    tel = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    ks = models.CharField(max_length=45, blank=True, null=True)
    city_type = models.IntegerField(blank=True, null=True)
    office_type = models.IntegerField(blank=True, null=True)
    firm = models.CharField(max_length=245, blank=True, null=True)
    param1 = models.CharField(max_length=245, blank=True, null=True)
    param2 = models.CharField(max_length=245, blank=True, null=True)
    param3 = models.CharField(max_length=245, blank=True, null=True)
    param4 = models.CharField(max_length=245, blank=True, null=True)
    int1 = models.IntegerField(blank=True, null=True)
    int2 = models.IntegerField(blank=True, null=True)
    int3 = models.IntegerField(blank=True, null=True)
    date1 = models.DateTimeField(blank=True, null=True)
    date2 = models.DateTimeField(blank=True, null=True)
    date3 = models.DateTimeField(blank=True, null=True)
    text1 = models.TextField(blank=True, null=True)
    text2 = models.TextField(blank=True, null=True)
    text3 = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_office'
        app_label = 'crm_build'


class SysProject(models.Model):
    row_id = models.IntegerField(blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=145, blank=True, null=True)
    prefix = models.CharField(unique=True, max_length=45, blank=True, null=True)
    description = models.CharField(max_length=345, blank=True, null=True)
    sys_project_id = models.CharField(max_length=45, blank=True, null=True)
    sys_project_param1 = models.IntegerField(blank=True, null=True)
    lot = models.AutoField(primary_key=True)
    token_key = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=445, blank=True, null=True)
    check1 = models.IntegerField(blank=True, null=True)
    check2 = models.IntegerField(blank=True, null=True)
    check3 = models.IntegerField(blank=True, null=True)
    check4 = models.IntegerField(blank=True, null=True)
    check5 = models.IntegerField(blank=True, null=True)
    check6 = models.IntegerField(blank=True, null=True)
    check7 = models.IntegerField(blank=True, null=True)
    check8 = models.IntegerField(blank=True, null=True)
    check9 = models.IntegerField(blank=True, null=True)
    check10 = models.IntegerField(blank=True, null=True)
    check11 = models.IntegerField(blank=True, null=True)
    check12 = models.IntegerField(blank=True, null=True)
    check13 = models.IntegerField(blank=True, null=True)
    check14 = models.IntegerField(blank=True, null=True)
    check15 = models.IntegerField(blank=True, null=True)
    check16 = models.IntegerField(blank=True, null=True)
    check17 = models.IntegerField(blank=True, null=True)
    check18 = models.IntegerField(blank=True, null=True)
    check19 = models.IntegerField(blank=True, null=True)
    check20 = models.IntegerField(blank=True, null=True)
    check21 = models.IntegerField(blank=True, null=True)
    check22 = models.IntegerField(blank=True, null=True)
    check23 = models.IntegerField(blank=True, null=True)
    check24 = models.IntegerField(blank=True, null=True)
    check25 = models.IntegerField(blank=True, null=True)
    check26 = models.IntegerField(blank=True, null=True)
    check27 = models.IntegerField(blank=True, null=True)
    check28 = models.IntegerField(blank=True, null=True)
    check29 = models.IntegerField(blank=True, null=True)
    check30 = models.IntegerField(blank=True, null=True)
    check31 = models.IntegerField(blank=True, null=True)
    check32 = models.IntegerField(blank=True, null=True)
    check33 = models.IntegerField(blank=True, null=True)
    check34 = models.IntegerField(blank=True, null=True)
    check35 = models.IntegerField(blank=True, null=True)
    check36 = models.IntegerField(blank=True, null=True)
    check37 = models.IntegerField(blank=True, null=True)
    check38 = models.IntegerField(blank=True, null=True)
    check39 = models.IntegerField(blank=True, null=True)
    check40 = models.IntegerField(blank=True, null=True)
    check41 = models.IntegerField(blank=True, null=True)
    check42 = models.IntegerField(blank=True, null=True)
    check43 = models.IntegerField(blank=True, null=True)
    check44 = models.IntegerField(blank=True, null=True)
    check45 = models.IntegerField(blank=True, null=True)
    check46 = models.IntegerField(blank=True, null=True)
    check47 = models.IntegerField(blank=True, null=True)
    check48 = models.IntegerField(blank=True, null=True)
    check49 = models.IntegerField(blank=True, null=True)
    check50 = models.IntegerField(blank=True, null=True)
    check51 = models.CharField(max_length=45, blank=True, null=True)
    check52 = models.IntegerField(blank=True, null=True)
    check53 = models.IntegerField(blank=True, null=True)
    check54 = models.IntegerField(blank=True, null=True)
    check55 = models.IntegerField(blank=True, null=True)
    check56 = models.IntegerField(blank=True, null=True)
    check57 = models.IntegerField(blank=True, null=True)
    check58 = models.IntegerField(blank=True, null=True)
    check59 = models.IntegerField(blank=True, null=True)
    check60 = models.IntegerField(blank=True, null=True)
    check61 = models.IntegerField(blank=True, null=True)
    check62 = models.IntegerField(blank=True, null=True)
    check63 = models.IntegerField(blank=True, null=True)
    check64 = models.IntegerField(blank=True, null=True)
    check65 = models.IntegerField(blank=True, null=True)
    check66 = models.IntegerField(blank=True, null=True)
    check67 = models.IntegerField(blank=True, null=True)
    check68 = models.IntegerField(blank=True, null=True)
    check69 = models.IntegerField(blank=True, null=True)
    check70 = models.IntegerField(blank=True, null=True)
    check71 = models.IntegerField(blank=True, null=True)
    check72 = models.IntegerField(blank=True, null=True)
    check73 = models.IntegerField(blank=True, null=True)
    check74 = models.IntegerField(blank=True, null=True)
    check75 = models.IntegerField(blank=True, null=True)
    check76 = models.IntegerField(blank=True, null=True)
    check77 = models.IntegerField(blank=True, null=True)
    check78 = models.IntegerField(blank=True, null=True)
    check79 = models.IntegerField(blank=True, null=True)
    check80 = models.IntegerField(blank=True, null=True)
    check350 = models.IntegerField(blank=True, null=True)
    param1 = models.CharField(max_length=45, blank=True, null=True)
    param2 = models.CharField(max_length=45, blank=True, null=True)
    param3 = models.CharField(max_length=45, blank=True, null=True)
    param4 = models.CharField(max_length=45, blank=True, null=True)
    param5 = models.CharField(max_length=45, blank=True, null=True)
    param6 = models.CharField(max_length=45, blank=True, null=True)
    param7 = models.CharField(max_length=45, blank=True, null=True)
    param8 = models.CharField(max_length=145, blank=True, null=True)
    param9 = models.CharField(max_length=45, blank=True, null=True)
    param10 = models.CharField(max_length=45, blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    date3 = models.DateField(blank=True, null=True)
    date4 = models.DateField(blank=True, null=True)
    date5 = models.DateField(blank=True, null=True)
    date6 = models.DateField(blank=True, null=True)
    date7 = models.DateField(blank=True, null=True)
    date8 = models.DateField(blank=True, null=True)
    date9 = models.DateField(blank=True, null=True)
    date10 = models.DateField(blank=True, null=True)
    sms_check = models.IntegerField(blank=True, null=True)
    sms_tel = models.CharField(max_length=45, blank=True, null=True)
    sms_login = models.CharField(max_length=45, blank=True, null=True)
    sms_pass = models.CharField(max_length=45, blank=True, null=True)
    yandex_map_key = models.CharField(max_length=100, blank=True, null=True)
    yandex_map_geocord1 = models.CharField(max_length=45, blank=True, null=True)
    yandex_map_geocord2 = models.CharField(max_length=45, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    uni_id = models.IntegerField(blank=True, null=True)
    uni_api = models.CharField(max_length=45, blank=True, null=True)
    f1 = models.CharField(max_length=30, blank=True, null=True)
    f2 = models.CharField(max_length=30, blank=True, null=True)
    logotip = models.CharField(max_length=45, blank=True, null=True)
    image_w = models.IntegerField(blank=True, null=True)
    image_h = models.IntegerField(blank=True, null=True)
    image_s = models.IntegerField(blank=True, null=True)
    image_o = models.CharField(max_length=1, blank=True, null=True)
    vod_znak = models.CharField(max_length=45, blank=True, null=True)
    vod_znak_place = models.CharField(max_length=15, blank=True, null=True)
    token = models.CharField(max_length=45, blank=True, null=True)
    hesh = models.CharField(max_length=45, blank=True, null=True)
    irr_check = models.IntegerField(blank=True, null=True)
    russianrealty_check = models.IntegerField(blank=True, null=True)
    rbc_check = models.IntegerField(blank=True, null=True)
    realestate_check = models.IntegerField(blank=True, null=True)
    idinaidi_check = models.IntegerField(blank=True, null=True)
    assis_check = models.IntegerField(blank=True, null=True)
    ged_check = models.IntegerField(blank=True, null=True)
    afy_check = models.IntegerField(blank=True, null=True)
    cian_check = models.IntegerField(blank=True, null=True)
    bpn_check = models.IntegerField(blank=True, null=True)
    yandex_check = models.IntegerField(blank=True, null=True)
    cat_h = models.IntegerField(blank=True, null=True)
    cat_w = models.IntegerField(blank=True, null=True)
    cat_c = models.IntegerField(blank=True, null=True)
    avito_check = models.IntegerField(blank=True, null=True)
    yandex2_check = models.IntegerField(blank=True, null=True)
    yandex3_check = models.IntegerField(blank=True, null=True)
    ged_partner_id = models.IntegerField(blank=True, null=True)
    sob_check = models.IntegerField(blank=True, null=True)
    winner_check = models.IntegerField(blank=True, null=True)
    eip_check = models.IntegerField(blank=True, null=True)
    chance_check = models.IntegerField(blank=True, null=True)
    piter_realtor_check = models.IntegerField(blank=True, null=True)
    bsn_check = models.IntegerField(blank=True, null=True)
    restate_check = models.IntegerField(blank=True, null=True)
    counter = models.CharField(max_length=2000, blank=True, null=True)
    kvmeter_check = models.IntegerField(blank=True, null=True)
    ws_port = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    cat_h2 = models.IntegerField(blank=True, null=True)
    cat_w2 = models.IntegerField(blank=True, null=True)
    cat_c2 = models.IntegerField(blank=True, null=True)
    timeout = models.IntegerField(blank=True, null=True)
    cian_tel = models.CharField(max_length=20, blank=True, null=True)
    avito_tel = models.CharField(max_length=20, blank=True, null=True)
    irr_tel = models.CharField(max_length=20, blank=True, null=True)
    ged_tel = models.CharField(max_length=20, blank=True, null=True)
    afy_tel = models.CharField(max_length=20, blank=True, null=True)
    yandex_tel = models.CharField(max_length=20, blank=True, null=True)
    yandex2_tel = models.CharField(max_length=20, blank=True, null=True)
    sob_tel = models.CharField(max_length=20, blank=True, null=True)
    winner_tel = models.CharField(max_length=20, blank=True, null=True)
    yandex3_tel = models.CharField(max_length=20, blank=True, null=True)
    imap_server = models.CharField(max_length=145, blank=True, null=True)
    imap_email = models.CharField(max_length=45, blank=True, null=True)
    imap_pass = models.CharField(max_length=45, blank=True, null=True)
    imap_port = models.CharField(max_length=4, blank=True, null=True)
    kvadrum_check = models.IntegerField(blank=True, null=True)
    kvadrum_tel = models.CharField(max_length=25, blank=True, null=True)
    cian_all_check = models.IntegerField(blank=True, null=True)
    avito_all_check = models.IntegerField(blank=True, null=True)
    afy_all_check = models.IntegerField(blank=True, null=True)
    kvadrum_all_check = models.IntegerField(blank=True, null=True)
    irr_all_check = models.IntegerField(blank=True, null=True)
    ged_all_check = models.IntegerField(blank=True, null=True)
    sob_all_check = models.IntegerField(blank=True, null=True)
    winner_all_check = models.IntegerField(blank=True, null=True)
    emls_check = models.IntegerField(blank=True, null=True)
    emls_all_check = models.IntegerField(blank=True, null=True)
    emls_tel = models.CharField(max_length=20, blank=True, null=True)
    yandex_all_check = models.IntegerField(blank=True, null=True)
    yandex2_all_check = models.IntegerField(blank=True, null=True)
    yandex3_all_check = models.IntegerField(blank=True, null=True)
    yandex2_name = models.CharField(max_length=15, blank=True, null=True)
    yandex3_name = models.CharField(max_length=15, blank=True, null=True)
    record_link = models.CharField(max_length=245, blank=True, null=True)
    asterisk_check = models.IntegerField(blank=True, null=True)
    email_reklama = models.CharField(max_length=40, blank=True, null=True)
    mango_check = models.IntegerField(blank=True, null=True)
    sber_check = models.IntegerField(blank=True, null=True)
    sber_login = models.CharField(max_length=50, blank=True, null=True)
    sber_pass = models.CharField(max_length=45, blank=True, null=True)
    sber_office_id = models.IntegerField(blank=True, null=True)
    avito_listingfee_enum = models.CharField(max_length=30, blank=True, null=True)
    mail_check = models.IntegerField(blank=True, null=True)
    mail_all_check = models.IntegerField(blank=True, null=True)
    mail_tel = models.CharField(max_length=20, blank=True, null=True)
    dop_check = models.IntegerField(blank=True, null=True)
    cian_replace = models.CharField(max_length=100, blank=True, null=True)
    cian_user_check = models.IntegerField(blank=True, null=True)
    domclick_check = models.IntegerField(blank=True, null=True)
    domclick_all_check = models.IntegerField(blank=True, null=True)
    domclick_tel = models.CharField(max_length=20, blank=True, null=True)
    domclick_apartment_check = models.IntegerField(blank=True, null=True)
    domclick_user_id_check = models.IntegerField(blank=True, null=True)
    tarif_type_conv = models.CharField(max_length=100, blank=True, null=True)
    tarif_cost = models.IntegerField(blank=True, null=True)
    tarif_type_value = models.IntegerField(blank=True, null=True)
    beeline_token = models.CharField(max_length=40, blank=True, null=True)
    yandex_logo_check = models.IntegerField(blank=True, null=True)
    wa_private_api_token = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_project'
        app_label = 'crm_build'


class SysRate(models.Model):
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.CharField(max_length=45, blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    valuta_type = models.IntegerField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)
    date_load = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_rate'
        app_label = 'crm_build'


class SysRole(models.Model):
    row_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=145, blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=845, blank=True, null=True)
    alias = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_role'
        app_label = 'crm_build'


class SysSequences(models.Model):

    class Meta:
        managed = False
        db_table = 'sys_sequences'
        app_label = 'crm_build'


class SysSequences1(models.Model):

    class Meta:
        managed = False
        db_table = 'sys_sequences1'
        app_label = 'crm_build'


class SysSession(models.Model):
    hash = models.CharField(max_length=225)
    name = models.CharField(max_length=225)
    last_time = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    user_ip = models.CharField(max_length=45, blank=True, null=True)
    exit_check = models.IntegerField(blank=True, null=True)
    http_user_agent = models.CharField(max_length=300, blank=True, null=True)
    login = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_session'
        app_label = 'crm_build'


class SysSite(models.Model):
    row_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=146, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    logo = models.CharField(max_length=145, blank=True, null=True)
    company = models.CharField(max_length=140, blank=True, null=True)
    tel = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    tel_header = models.CharField(max_length=1000, blank=True, null=True)
    addr = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    uslugi = models.TextField(blank=True, null=True)
    logo_style = models.CharField(max_length=100, blank=True, null=True)
    goglemaps_key = models.CharField(max_length=45, blank=True, null=True)
    script_text = models.TextField(blank=True, null=True)
    site_enum = models.CharField(max_length=20, blank=True, null=True)
    company_check = models.IntegerField(blank=True, null=True)
    header_text = models.TextField(blank=True, null=True)
    footer_text = models.TextField(blank=True, null=True)
    style_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_site'
        app_label = 'crm_build'


class SysStat(models.Model):
    name = models.CharField(max_length=245, blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    datetime1 = models.DateTimeField(blank=True, null=True)
    obj_id = models.IntegerField(blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    table_name = models.CharField(max_length=45, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    stat_enum = models.CharField(max_length=4, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_stat'
        app_label = 'crm_build'


class SysSticker(models.Model):
    sticker_id = models.AutoField(primary_key=True)
    sticker_user = models.IntegerField()
    sticker_text = models.TextField()
    sticker_top = models.CharField(max_length=10)
    sticker_left = models.CharField(max_length=10)
    sticker_width = models.CharField(max_length=10)
    sticker_height = models.CharField(max_length=10)
    sticker_color = models.CharField(max_length=20)
    sticker_font = models.CharField(max_length=10)
    sticker_date = models.DateTimeField(blank=True, null=True)
    sticker_sms = models.IntegerField(blank=True, null=True)
    sticker_email = models.IntegerField(blank=True, null=True)
    sticker_send = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_sticker'
        app_label = 'crm_build'


class SysSupport(models.Model):
    row_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=245, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status_enum = models.CharField(max_length=45, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    priority_enum = models.CharField(max_length=45, blank=True, null=True)
    lot = models.AutoField(primary_key=True)
    parent_id = models.IntegerField(blank=True, null=True)
    change_date = models.DateTimeField(blank=True, null=True)
    email_check = models.IntegerField(blank=True, null=True)
    date1 = models.DateTimeField(blank=True, null=True)
    date2 = models.DateTimeField(blank=True, null=True)
    date3 = models.DateTimeField(blank=True, null=True)
    param1 = models.CharField(max_length=45, blank=True, null=True)
    param2 = models.CharField(max_length=45, blank=True, null=True)
    param3 = models.CharField(max_length=945, blank=True, null=True)
    param4 = models.CharField(max_length=945, blank=True, null=True)
    param5 = models.IntegerField(blank=True, null=True)
    param6 = models.IntegerField(blank=True, null=True)
    param7 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_support'
        app_label = 'crm_build'


class SysType(models.Model):
    row_id = models.IntegerField(primary_key=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=145, blank=True, null=True)
    name_eng = models.CharField(max_length=45, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    is_group = models.CharField(max_length=1, blank=True, null=True)
    value = models.CharField(max_length=45, blank=True, null=True)
    order_by = models.IntegerField(blank=True, null=True)
    prefix = models.CharField(max_length=5, blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_type'
        app_label = 'crm_build'


class SysUpdate(models.Model):
    row_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    prefix_box = models.CharField(max_length=1000, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    update_check = models.IntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_status = models.CharField(max_length=45, blank=True, null=True)
    ok_check = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_update'
        app_label = 'crm_build'


class SysUpdateHist(models.Model):
    row_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    update_id = models.IntegerField(blank=True, null=True)
    part_id = models.IntegerField(blank=True, null=True)
    msg = models.CharField(max_length=2000, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    part_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_update_hist'
        app_label = 'crm_build'


class SysUpdatePart(models.Model):
    row_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    sys_date_create = models.DateTimeField(blank=True, null=True)
    sys_user_create = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    update_id = models.IntegerField(blank=True, null=True)
    part_sort = models.IntegerField(blank=True, null=True)
    part_enum = models.CharField(max_length=45, blank=True, null=True)
    part_text = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    file_md5 = models.CharField(max_length=45, blank=True, null=True)
    ok_check = models.IntegerField(blank=True, null=True)
    error_text = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_update_part'
        app_label = 'crm_build'


class SysUser(models.Model):
    row_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    role_types = models.CharField(max_length=100, blank=True, null=True)
    login = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    admin = models.IntegerField(blank=True, null=True)
    card_name = models.CharField(max_length=45, blank=True, null=True)
    comment = models.CharField(max_length=445, blank=True, null=True)
    prefix = models.CharField(max_length=5, blank=True, null=True)
    is_blocked = models.CharField(max_length=1, blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    order_by = models.IntegerField(blank=True, null=True)
    post = models.CharField(max_length=145, blank=True, null=True)
    social = models.CharField(max_length=345, blank=True, null=True)
    photo = models.CharField(max_length=145, blank=True, null=True)
    site_check = models.IntegerField(blank=True, null=True)
    param1_type = models.IntegerField(blank=True, null=True)
    param2_type = models.IntegerField(blank=True, null=True)
    param3 = models.CharField(max_length=145, blank=True, null=True)
    office_id = models.IntegerField(blank=True, null=True)
    fff = models.CharField(max_length=145, blank=True, null=True)
    iii = models.CharField(max_length=45, blank=True, null=True)
    ooo = models.CharField(max_length=145, blank=True, null=True)
    sex_enum = models.CharField(max_length=1, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    fio = models.CharField(max_length=445, blank=True, null=True)
    phone2 = models.CharField(max_length=45, blank=True, null=True)
    phone3 = models.CharField(max_length=45, blank=True, null=True)
    extension = models.CharField(max_length=65, blank=True, null=True)
    otdel = models.CharField(max_length=45, blank=True, null=True)
    ip_text = models.CharField(max_length=1000, blank=True, null=True)
    email_sign = models.CharField(max_length=1000, blank=True, null=True)
    imap_server = models.CharField(max_length=45, blank=True, null=True)
    imap_email = models.CharField(max_length=45, blank=True, null=True)
    imap_pass = models.CharField(max_length=45, blank=True, null=True)
    imap_port = models.IntegerField(blank=True, null=True)
    tel_reklama = models.CharField(max_length=20, blank=True, null=True)
    telega_user_id = models.BigIntegerField(blank=True, null=True)
    tarif_notice_check = models.IntegerField(blank=True, null=True)
    beeline_subscription_enum = models.CharField(max_length=42, blank=True, null=True)
    beeline_subscription_id = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user'
        app_label = 'crm_build'
