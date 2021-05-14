import json

import requests

data = """{
  "codigoProceso": "730010",
  "numeroSecuencia": "000001",
  "terminalId": "20013434",
  "merchId": "H373003",
  "informacionTerminal": {
    "networkInterface": "WIFI",
    "privateIp": "192.168.0.166",
    "latitude": "0",
    "longitude": "0",
    "signaLevel": "95",
    "batteryLevel": "85",
    "informacionRedCelular": "0,0,1548131,51941"
  },
  "monitoreo": {
    "GIROS": [
      {
        "COD": "185",
        "FECHA": "08/04/2021",
        "HORA_INICIO": "11:00:00",
        "HORA_FIN": "11:01:23"
      },
      {
        "COD": "185",
        "FECHA": "08/04/2021",
        "HORA_INICIO": "11:00:00",
        "HORA_FIN": "11:01:23"
      }
    ],
    "RETIROS": [
      {
        "COD": "185",
        "FECHA": "08/04/2021",
        "HORA_INICIO": "11:00:00",
        "HORA_FIN": "11:01:23"
      },
      {
        "COD": "185",
        "FECHA": "08/04/2021",
        "HORA_INICIO": "11:00:00",
        "HORA_FIN": "11:01:23"
      }
    ],
    "DEPOSITOS": [
      {
        "COD": "185",
        "FECHA": "08/04/2021",
        "HORA_INICIO": "11:00:00",
        "HORA_FIN": "11:01:23"
      },
      {
        "COD": "185",
        "FECHA": "08/04/2021",
        "HORA_INICIO": "11:00:00",
        "HORA_FIN": "11:01:23"
      }
    ],
    "CONSULTAS": [
      {
        "COD": "185",
        "FECHA": "08/04/2021",
        "HORA_INICIO": "11:00:00",
        "HORA_FIN": "11:01:23"
      },
      {
        "COD": "185",
        "FECHA": "08/04/2021",
        "HORA_INICIO": "11:00:00",
        "HORA_FIN": "11:01:23"
      }
    ]
  }
}"""
url = 'http://127.0.0.1:6090/json_receive/json_receive/'
json_data = json.loads(data)
json_endpoint = requests.post(url, json=json_data)
pass
