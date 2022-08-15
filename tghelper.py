import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TG_TOKEN')
chat_id = os.getenv('CHAT_ID')
mi_chat_id = os.getenv('MI_CHAT_ID')

def mandarme_mensaje(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': {mi_chat_id}, 'text': message}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=params, headers=headers)
    return response.json()

def mandar_mensaje(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {'chat_id': {chat_id}, 'text': message}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=params, headers=headers)
    return response.json()

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    response = mandar_mensaje("Mensaje de prueba")
    print(response)