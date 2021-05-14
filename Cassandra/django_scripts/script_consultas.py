import os
import time

from django.db import connection

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "polaris_cloud_monitoreo.settings")
import django

django.setup()
from monitoreo.models import MonitoringByMerchidModel
import datetime

if __name__ == '__main__':
    # today = datetime.datetime.now().date()
    # # terminales = list(MonitoringByMerchidModel.objects.filter(monitoring_merchi_date=today,
    # #                                                           monitoring_merchid='H989024'))
    #
    # inicio = time.time()
    # trx = MonitoringByMerchidModel.objects.filter(
    #     monitoring_merchi_date=today, monitoring_merchi_transaction_type='CONSULTAS').values_list(
    #     'monitoring_merchi_approved', flat=True)
    #
    # consultas_procesadas = sum(list(trx))
    # fin = time.time()
    # tiempo_ejecucion = fin - inicio
    # consultas_rechazadas = sum(list(trx_consultas.values_list('monitoring_merchi_rejected', flat=True)))
    # trx_retiros = trx.filter(monitoring_merchi_transaction_type='RETIROS')
    # retiros_procesadas = sum(list(trx_retiros.values_list('monitoring_merchi_approved', flat=True)))
    # retiros_rechazadas = sum(list(trx_retiros.values_list('monitoring_merchi_rejected', flat=True)))
    # trx_giros = trx.filter(monitoring_merchi_transaction_type='GIROS')
    # giros_procesadas = sum(list(trx_giros.values_list('monitoring_merchi_approved', flat=True)))
    # giros_rechazadas = sum(list(trx_giros.values_list('monitoring_merchi_rejected', flat=True)))
    # trx_depositos = trx.filter(monitoring_merchi_transaction_type='DEPOSITOS')
    # depositos_procesadas = sum(list(trx_depositos.values_list('monitoring_merchi_approved', flat=True)))
    # depositos_rechazadas = sum(list(trx_depositos.values_list('monitoring_merchi_rejected', flat=True)))
    inicio = time.time()
    cursor = connection.cursor()
    result_cql = cursor.execute(
        "SELECT * FROM general_monitoring_by_merch_id WHERE monitoring_merchi_date = '2021-04-28' AND monitoring_merchid = 'H989024'")
    list_h989024 = list(result_cql)
    fin = time.time()
    tiempo_ejecucion_cql = fin - inicio

    inicio = time.time()
    result_orm = MonitoringByMerchidModel.objects.filter(monitoring_merchi_date='2021-04-28',
                                                         monitoring_merchid='H989024')
    list_h989024_2 = list(result_orm)
    fin = time.time()
    tiempo_ejecucion_orm = fin - inicio
    pass
