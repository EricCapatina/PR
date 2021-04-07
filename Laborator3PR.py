import requests
import json
from threading import *
import time
proxies = {
    "http": "http://Seleric199k:Y4f8LnL@191.96.60.13:45785",
    "https": "http://Seleric199k:Y4f8LnL@191.96.60.13:45785",
    "socks5": "http://Seleric199k:Y4f8LnL@191.96.60.13:45786",
}


def search_api_post():
    choice = input("Ce doriti sa faceti?\n"
                   "'1' - Search by keyword\n"
                   "'2' - Search by category\n"
                   "")
    if choice == "2":
        number = input("How many posts u wanna see?\n\t\t\t")
        category = input("Input category ( Ex: 'adventure' ):\n\t\t\t")
        session = requests.get('https://kitsu.io/api/edge/anime?page[limit]=' + number + '&filter[categories]='
                               + category, proxies=proxies)
        json_object = json.loads(session.text)
        for item in json_object['data']:
            print('Title: ' + item['attributes']['slug'])
            print('Description:\n' + item['attributes']['description'])
            print('Image link:\n' + item['attributes']['posterImage']['original'])
            print('-------====================-------')
    elif choice == "1":
        number = input("How many posts u wanna see?\n\t\t\t")
        word = input("Input keyword: \n\t\t\t")
        session = requests.get('https://kitsu.io/api/edge/anime?page[limit]=' + number + '&filter[text]='
                               + word, proxies=proxies)
        json_object = json.loads(session.text)
        for item in json_object['data']:
            print('Title: ' + item['attributes']['slug'])
            print('Description:\n' + item['attributes']['description'])
            print('Image link:\n' + item['attributes']['posterImage']['original'])
            print('-------====================-------')


def get():
    session = requests.get('https://kitsu.io/api/edge/anime?page[limit]=1', proxies=proxies)
    json_object = json.loads(session.text)
    json_formatted_object = json.dumps(json_object, indent=2)
    print(json_formatted_object)


def head():
    session = requests.head('https://utm.md/', proxies=proxies)
    print('Response header: ' + str(session.headers))


def options(thread_name):
    session = requests.options('https://kitsu.io', proxies=proxies)
    print(thread_name + ": " + 'Status code: ' + str(session.status_code))


def post():
    session = requests.post("http://bugs.python.org", data={'number': 12524, 'type': 'issue', 'action': 'show'},
                            proxies=proxies)
    print(session.status_code, session.reason)
    print(session.text[:555] + '...')


while True:
    select = input("\nSelect:\n"
                   "'1' - Search by parameters ( kitsu.io API )\n"
                   "'2' - Method GET\n"
                   "'3' - Method OPTIONS\n"
                   "'4' - Method HEAD\n"
                   "'5' - Method POST\n"
                   "'EXIT' - exit program\n\t\t\t")
    if select == '1':
        search_api_post()
    elif select == '2':
        get()
    elif select == '3':
        t1 = Thread(target=options, args=('Thread-1', ))
        t2 = Thread(target=options, args=('Thread-2', ))
        t1.start()
        t2.start()
        time.sleep(3)
    elif select == '4':
        head()
    elif select == '5':
        post()
    elif select == 'EXIT' or select == 'exit':
        exit()
    else:
        print("Wrong option!")
