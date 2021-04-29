import schedule
import time
import csv
import requests
import urllib3

urllib3.disable_warnings()

from datetime import datetime

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

def validUrl(url, system):
    conterror = 3
    while (conterror > 0):
        try:
            result = requests.get(url, verify=False, timeout=5, headers=headers).status_code
        except:
            result = 99999

        if (result == 200):
            result = 'DISPONIVEL'
            conterror = 0
        else:
            result = 'INDISPONIVEL'
            conterror -= 1

    # --------------------------- Grava Resultado no arquivo Local ---------------------------
    with open('C:/Automations/validUrl/results/resultValidUrl.csv', 'a+', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([system, str(datetime.now().strftime('%d/%m/%Y')), str(datetime.now().strftime('%H:%M')), result])
        file.close()


config = open('C:/Automations/validUrl/config/config.txt', 'r').readlines()
list_config = []
cont = len(config)

for n in config:
    list_config.append(n.rstrip())

#print(str(datetime.now().strftime('%d/%m/%Y - %H:%M')))
contin = 0
while (cont > contin):
    system = (list_config[contin][:list_config[contin].find('=')]).strip()
    url = (list_config[contin][list_config[contin].find('=') + 1:]).strip()
    validUrl(url, system)
    contin += 1
