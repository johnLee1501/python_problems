import os
import time

from django.db import connection

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "polaris_cloud_monitoreo.settings")
import django

django.setup()
from monitoreo.models import MonitoringByMerchidModel

if __name__ == '__main__':
    inicio = time.time()
    cursor = connection.cursor()
    result_cql = cursor.execute("SELECT * FROM general_monitoring_by_merch_id "
                                "WHERE monitoring_merchi_date = '2021-04-28' AND monitoring_merchid = 'H98555'")
    list_h989024 = list(result_cql)
    fin = time.time()
    tiempo_ejecucion_cql = fin - inicio

    inicio = time.time()
    cursor = connection.cursor()
    result_cql = cursor.execute("SELECT * FROM general_monitoring_by_merch_id "
                                "WHERE monitoring_merchi_date = '2021-04-28' AND monitoring_merchid = 'H98555' ALLOW FILTERING ")
    list_h9890242 = list(result_cql)
    fin = time.time()
    tiempo_ejecucion_cql_allow = fin - inicio

    inicio = time.time()
    result_orm = MonitoringByMerchidModel.objects.filter(monitoring_merchi_date='2021-04-28',
                                                         monitoring_merchid='H98555')
    list_h989024_2 = list(result_orm)
    fin = time.time()
    tiempo_ejecucion_orm = fin - inicio
    # print(f'ORM: {tiempo_ejecucion_orm} VS CQL: {tiempo_ejecucion_cql}')
    pass
