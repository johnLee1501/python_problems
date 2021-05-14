from datetime import date

from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class MonitoringByMerchidModel(DjangoCassandraModel):
    _table_name = "general_monitoring_by_merch_id"
    monitoring_merchi_date = columns.Date(required=True, primary_key=True)
    monitoring_merchid = columns.Text(required=True, primary_key=True)
    monitoring_merchi_transaction_type = columns.Text(required=False, primary_key=True)
    monitoring_merchi_approved = columns.Integer(required=False)
    monitoring_merchi_rejected = columns.Integer(required=False)
    monitoring_merchi_printing_error = columns.Integer(required=False)
    monitoring_merchi_timeout = columns.Integer(required=False)

    class Meta:
        get_pk_field = 'monitoring_merchi_date'


class MonitoringByTrxModel(DjangoCassandraModel):
    _table_name = "general_merch_all"
    monitoring_merchi_date = columns.Date(required=True, primary_key=True)
    monitoring_merchi_transaction_type = columns.Text(required=False, primary_key=True)
    monitoring_merchid = columns.Text(required=True, primary_key=True)
    monitoring_merchi_approved = columns.Integer(required=False)
    monitoring_merchi_rejected = columns.Integer(required=False)
    monitoring_merchi_printing_error = columns.Integer(required=False)
    monitoring_merchi_timeout = columns.Integer(required=False)

    class Meta:
        get_pk_field = 'monitoring_merchi_date'


"""
class MonitoringByGroupModel(DjangoCassandraModel):
    _table_name = "general_monitoring_by_group"
    monitoring_group_date = columns.Date(required=True, primary_key=True, default=date)
    monitoring_group = columns.Text(required=True, primary_key=True)
    monitoring_group_merch_id = columns.Text(required=True, primary_key=True)
    monitoring_group_transaction_type = columns.Text(required=False)
    monitoring_group_approved = columns.Text(required=False)
    monitoring_group_rejected = columns.Text(required=False)
    monitoring_group_printing_error = columns.Text(required=False)
    monitoring_group_timeout = columns.Text(required=False)

    class Meta:
        get_pk_field = 'monitoring_group_date'


class MonitoringTerminalModel(DjangoCassandraModel):
    _table_name = "monitoring_terminal"
    monitoring_terminal_date = columns.Date(required=True, primary_key=True, default=date)
    monitoring_terminal_merch_id = columns.Text(required=True, primary_key=True)
    monitoring_terminal_ip_public = columns.Text(required=False)
    monitoring_terminal_ip_private = columns.Text(required=False)
    monitoring_terminal_coordinates = columns.Text(required=False)
    monitoring_terminal_network_interface = columns.Text(required=False)
    monitoring_terminal_serial = columns.Text(required=False)
    monitoring_terminal_bluetooth = columns.Boolean(required=False)
    monitoring_terminal_battery_level = columns.Text(required=False)
    monitoring_terminal_signal_level = columns.Text(required=False)
    monitoring_terminal_update_time = columns.Date(required=False)

    class Meta:
        get_pk_field = 'monitoring_terminal_date'

class monitoringDetailModel(DjangoCassandraModel):
    _table_name = "monitoring_detail"
    monitoring_detail_date = columns.Date(required=True, primary_key=True, default=date)
    monitoring_detail_merchid = columns.Text(required=True, primary_key=True)
    monitoring_detail_trx = columns.Text(required=False)
    monitoring_detail_status = columns.Text(required=False)
    monitoring_detail_start_time = columns.DateTime(required=False)
    monitoring_detail_end_time = columns.DateTime(required=False)
    monitoring_detail_duration = columns.BigInt(required=False)

    class Meta:
        get_pk_field = 'monitoring_detail_date'


class TerminalStatusModel(DjangoCassandraModel):
    _table_name = "terminal_status"
    terminal_status_datetime = columns.DateTime(required=True, primary_key=True)
    terminal_status_merch_id = columns.Text(required=False)

    class Meta:
        get_pk_field = 'terminal_status_datetime'
"""
