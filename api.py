import requests

API = 'https://api.vk.com/method/'

def call_api(method, **kwargs):
    try:
        resp = requests.get(API + method , kwargs)
        if resp.ok:
            return resp.json()['response']
    except Exception as e:
        print e.message

#for user in users:
#    pass