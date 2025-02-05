# pip3 install requests

import json

import requests


def main_get():
    base_url = 'https://httpbin.org/get'

    query_params = {
        'order': 'votes',
        'sort': 'desc'
    }
    headers = {
        'X-Shop-Token': 'vfhnsirf',
        'User-Agent': 'Mega-Browser'
    }

    response = requests.get(base_url, params=query_params, headers=headers)

    print(response.json())


def main_post():
    base_url = 'https://httpbin.org/post'

    payload = {
        'name': 'Alexey',
        'job': 'developer',
        'experience': 9
    }
    headers = {
        'X-Shop-Token': 'vfhnsirf',
        'User-Agent': 'Mega-Browser'
    }

    response = requests.post(base_url, headers=headers, data=payload)

    print(response.json())


if __name__ == "__main__":
    main_post()
