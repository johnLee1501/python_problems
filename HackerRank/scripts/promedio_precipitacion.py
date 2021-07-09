import pandas as pd

months = ['Nombre Estación', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre',
          'Octubre', 'Noviembre',
          'Diciembre']
precipitation = pd.read_csv("excel.csv")
summary_precipitation = precipitation[['NombreEstacion', 'Fecha', 'Valor']]
summary_precipitation['Month'] = pd.DatetimeIndex(summary_precipitation['Fecha']).month
summary_precipitation = summary_precipitation.groupby(['NombreEstacion', 'Month']).Valor.sum().reset_index()
summary_precipitation = summary_precipitation.pivot(index=['NombreEstacion'], columns='Month',
                                                    values='Valor').reset_index()
summary_precipitation.columns = months
summary_precipitation.to_csv('precipitacion.csv', index=False, encoding="utf-8")
