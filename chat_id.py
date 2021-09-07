from prettyprinter import pprint
import requests
import json

def chat_id(token):
    response = requests.get(f"https://api.telegram.org/bot{token}/getUpdates")

    if response.status_code == 409:
        print("\nyour telegram bot is using webhook\n")

    else:
        res = response.json()
        message = response.json()['result'][0]['message']['chat']['id']
        print(f"\nyour telegram chat id is : {message}\n")

tok = input("\ninput your telegram token: ")

chat_id(tok)
