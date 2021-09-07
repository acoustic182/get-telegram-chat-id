from prettyprinter import pprint
import requests

def chat_id(types):
    if types == 'group':
        token = input(f"\nyou choose to find your telegram {types} chat id\nnow input your token: ")
        gchat = requests.get(f"https://api.telegram.org/bot{token}/getUpdates")
        gid = gchat.json()['result'][1]['my_chat_member']['chat']['id']
        print(f"\nyour {types} chat id is : {gid}\n")

    elif types == 'private':
        token = input(f"\nyou choose to find your telegram {types} chat id\nnow input your token: ")
        pchat = requests.get(f"https://api.telegram.org/bot{token}/getUpdates")
        pid = pchat.json()['result'][0]['message']['chat']['id']
        print(f"\nyour {types} chat id is : {pid}\n")
    
    else:
        print(f"\nyour chat type {types} is not recognize\n")

chatype = input("\ntype of your chat (group/private): ")

chat_id(chatype)
