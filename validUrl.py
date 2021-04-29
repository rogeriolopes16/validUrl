from modules.verifyURL import *

vr = ValidURL()

if __name__ == '__main__':
    config = open('C:/Automations/validUrl/config/config.txt', 'r').readlines()
    list_config = []

    for n in config:
            list_config.append(n.rstrip())

    vr.execVerify(list_config)
