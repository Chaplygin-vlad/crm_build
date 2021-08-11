from django.db import models


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
    param3 = models.CharField(max_length=80, blank=True, null=True)  # Материал стен
    param4 = models.CharField(max_length=145, blank=True, null=True)
    param5 = models.CharField(max_length=45, blank=True, null=True)  # На разные стороны
    param6 = models.CharField(max_length=45, blank=True, null=True)  # Ремонт
    param7 = models.CharField(max_length=45, blank=True, null=True)
    param8 = models.CharField(max_length=45, blank=True, null=True)  # Санузел
    param9 = models.CharField(max_length=45, blank=True, null=True)  # Окна
    param10 = models.CharField(max_length=45, blank=True, null=True)
    param11 = models.CharField(max_length=45, blank=True, null=True)  # Тип квартиры
    param12 = models.CharField(max_length=45, blank=True, null=True)
    param13 = models.CharField(max_length=45, blank=True, null=True)  # Пол
    param14 = models.CharField(max_length=45, blank=True, null=True)
    param15 = models.CharField(max_length=45, blank=True, null=True)
    param16 = models.CharField(max_length=45, blank=True, null=True)
    param17 = models.CharField(max_length=345, blank=True, null=True)  # Двери
    param18 = models.CharField(max_length=45, blank=True, null=True)
    param19 = models.CharField(max_length=45, blank=True, null=True)  # Перепланировка
    param20 = models.CharField(max_length=45, blank=True, null=True)  # Распашонка
    param21 = models.CharField(max_length=45, blank=True, null=True)  # Вид комнат
    param22 = models.CharField(max_length=45, blank=True, null=True)  # Количество собственников
    param23 = models.CharField(max_length=45, blank=True, null=True)
    param24 = models.CharField(max_length=45, blank=True, null=True)
    param25 = models.CharField(max_length=45, blank=True, null=True)
    param26 = models.CharField(max_length=45, blank=True, null=True)
    param27 = models.CharField(max_length=45, blank=True, null=True)
    param28 = models.CharField(max_length=145, blank=True, null=True)
    param29 = models.CharField(max_length=60, blank=True, null=True)
    param30 = models.CharField(max_length=14, blank=True, null=True)  # Парковка
    param31 = models.CharField(max_length=37, blank=True, null=True)
    param100 = models.CharField(max_length=45, blank=True, null=True)  # Ключи от объекта
    param101 = models.CharField(max_length=45, blank=True, null=True)  # Когда возможен показ
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
    obl_rayon_auto = models.CharField(max_length=145, blank=True, null=True)  #
    np_rayon_auto = models.CharField(max_length=145, blank=True, null=True)  # Район города
    way_auto = models.CharField(max_length=45, blank=True, null=True)
    realty_id = models.IntegerField(blank=True, null=True)
    jk_id = models.IntegerField(blank=True, null=True)
    pos_enum = models.CharField(max_length=20, blank=True, null=True)  # Расположение
    okrug_type = models.IntegerField(blank=True, null=True)
    district_type = models.IntegerField(blank=True, null=True)
    metro1_type = models.IntegerField(blank=True, null=True)
    metro2_type = models.IntegerField(blank=True, null=True)
    metro3_type = models.IntegerField(blank=True, null=True)
    to_metro_w = models.IntegerField(blank=True, null=True)
    to_metro_t = models.IntegerField(blank=True, null=True)
    obl_auto = models.CharField(max_length=45, blank=True, null=True)  # Область
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
        ordering = ['-lot']


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
    kolichestvo_komnat = models.CharField(db_column='Kolichestvo_komnat', max_length=20, blank=True,
                                          null=True)  # Field name made lowercase.
    vid_obekta = models.CharField(db_column='Vid_obekta', max_length=40, blank=True,
                                  null=True)  # Field name made lowercase.
    plocshad = models.CharField(db_column='Plocshad', max_length=15, blank=True,
                                null=True)  # Field name made lowercase.
    etazh = models.CharField(db_column='Etazh', max_length=15, blank=True, null=True)  # Field name made lowercase.
    etazhej_v_dome = models.CharField(db_column='Etazhej_v_dome', max_length=20, blank=True,
                                      null=True)  # Field name made lowercase.
    plocshad_kuhni = models.CharField(db_column='Plocshad_kuhni', max_length=15, blank=True,
                                      null=True)  # Field name made lowercase.
    zhilaya_plocshad = models.CharField(db_column='ZHilaya_plocshad', max_length=15, blank=True,
                                        null=True)  # Field name made lowercase.
    srok_arendy = models.CharField(db_column='Srok_arendy', max_length=40, blank=True,
                                   null=True)  # Field name made lowercase.
    tip_doma = models.CharField(db_column='Tip_doma', max_length=45, blank=True,
                                null=True)  # Field name made lowercase.
    komnat_v_kvartire = models.CharField(db_column='Komnat_v_kvartire', max_length=20, blank=True,
                                         null=True)  # Field name made lowercase.
    komissiya = models.CharField(db_column='Komissiya', max_length=20, blank=True,
                                 null=True)  # Field name made lowercase.
    zalog = models.CharField(db_column='Zalog', max_length=20, blank=True, null=True)  # Field name made lowercase.
    razmer_komissii = models.CharField(db_column='Razmer_komissii', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.
    plocshad_uchastka = models.CharField(db_column='Plocshad_uchastka', max_length=20, blank=True,
                                         null=True)  # Field name made lowercase.
    plocshad_doma = models.CharField(db_column='Plocshad_doma', max_length=20, blank=True,
                                     null=True)  # Field name made lowercase.
    material_sten = models.CharField(db_column='Material_sten', max_length=30, blank=True,
                                     null=True)  # Field name made lowercase.
    rasstoyanie_do_goroda = models.CharField(db_column='Rasstoyanie_do_goroda', max_length=20, blank=True,
                                             null=True)  # Field name made lowercase.
    kategoriya_zemel = models.CharField(db_column='Kategoriya_zemel', max_length=40, blank=True,
                                        null=True)  # Field name made lowercase.
    ohrana = models.CharField(db_column='Ohrana', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tip_garazha = models.CharField(db_column='Tip_garazha', max_length=20, blank=True,
                                   null=True)  # Field name made lowercase.
    tip_mashinomesta = models.CharField(db_column='Tip_mashinomesta', max_length=45, blank=True,
                                        null=True)  # Field name made lowercase.
    klass_zdaniya = models.CharField(db_column='Klass_zdaniya', max_length=20, blank=True,
                                     null=True)  # Field name made lowercase.
    tip_obyavleniya = models.CharField(db_column='Tip_obyavleniya', max_length=20, blank=True,
                                       null=True)  # Field name made lowercase.
    plocshad_komnaty = models.CharField(db_column='Plocshad_komnaty', max_length=20, blank=True,
                                        null=True)  # Field name made lowercase.
    main_image = models.CharField(max_length=145, blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    check_check = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rl_parser4'
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
