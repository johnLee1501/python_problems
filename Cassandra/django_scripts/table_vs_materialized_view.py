import os
import time

from django.db import connection

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "polaris_cloud_monitoreo.settings")
import django

django.setup()

from monitoreo.models import MonitoringByMerchidModel, MonitoringByTrxModel


def promedio_por_consulta(cql, repeticiones):
    inicio = time.time()
    for x in range(repeticiones):
        cursor = connection.cursor()
        sum_tabla_principal = cursor.execute(
            cql)
    fin = time.time()
    tiempo = fin - inicio
    return tiempo / repeticiones


if __name__ == '__main__':
    tiempo_tabla_principal = promedio_por_consulta(
        "SELECT sum (monitoring_merchi_approved) FROM general_monitoring_by_merch_id "
        "WHERE monitoring_merchi_date = '2021-04-28' "
        "AND monitoring_merchi_transaction_type = 'CONSULTAS' ALLOW FILTERING",
        100)
    tiempo_vista_materializada = promedio_por_consulta(
        "SELECT sum (monitoring_merchi_approved) FROM general_merch_all "
        "WHERE monitoring_merchi_date = '2021-04-28' "
        "AND monitoring_merchi_transaction_type = 'CONSULTAS'",
        100)
    inicio = time.time()
    for x in range(100):
        suma_orm_tabla_principal = sum(list(MonitoringByMerchidModel.objects.filter(
            monitoring_merchi_date='2021-04-28', monitoring_merchi_transaction_type='CONSULTAS').limit(None).values_list(
            'monitoring_merchi_approved', flat=True)))
    fin = time.time()
    tiempo_orm_tabla_principal = (fin - inicio) / 100

    inicio = time.time()
    for x in range(100):
        suma_orm_vista_materializada = sum(list(MonitoringByTrxModel.objects.filter(
            monitoring_merchi_date='2021-04-28', monitoring_merchi_transaction_type='CONSULTAS').values_list(
            'monitoring_merchi_approved', flat=True)))
    fin = time.time()
    tiempo_orm_vista_materializada = (fin - inicio) / 100
    pass
