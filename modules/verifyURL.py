import csv
import requests
import urllib3
import json
import threading

urllib3.disable_warnings()

from datetime import datetime

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}

class ValidURL():
    def __init__(self):
        pass

    def execVerify(self, list_config):
        for list_config in list_config:
            system = (list_config[:list_config.find('=')]).strip()
            url = (list_config[list_config.find('=') + 1:]).strip()
            threading.Thread(target=self.validUrl,args=(url, system)).start()

    def validUrl(self, url, system):
        conterror = 3
        while (conterror > 0):
            try:
                if ('WSO2' in system):
                    params = {"date": ""+str(datetime.now().strftime('%m%Y'))+""}
                    result = requests.post(url, verify=False, timeout=10, data=json.dumps(params),headers=headers).status_code
                else:
                    result = requests.get(url, verify=False, timeout=10, headers=headers).status_code
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