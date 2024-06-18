import json

configInfo = json.load(open('config.json', 'r'))

def getAuthToken ():
    return configInfo.get('auth_token')

def getMenuChannel():
    return configInfo.get('menu_channel')