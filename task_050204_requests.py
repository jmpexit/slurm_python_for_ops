# pip3 install requests

import json

import requests


def main():
    base_url = 'https://httpbin.org' # httpbin.org - echo-service, responds with what we send in a body
    response = requests.get(base_url + '/get')
    print(response)
    print(response.status_code) # status_code is a getter of the response object
    print(response.text)  # text is also a getter. response body in text


    # ADDING QUERY PARAMS
    response1 = requests.get(base_url + '/get?param1=foo')
    print('RESPONSE 1: ', response1.status_code)
    print(response1.text) # we'll get "args": {"param1": "foo" in the response


    # ADDING QUERY PARAMS AND HEADERS: more convenient syntax, with dicts
    query_params = {
        'param1': 'foo',
        'param2': 'bar'
    }
    headers = {
        'User-Agent': 'Chrome',
        'Authorization': 'Bearer: stejhgoptrirpots'
    }
    response2 = requests.get(base_url + '/get', params=query_params, headers=headers)
    # note: path params (/get) can only be set in endpoint
    print('RESPONSE 2: ', response2.status_code)
    print(response2.text)

    # SENDING BODIES
    payload = {
        'id': 3333,
        'name': 'Python'
    }
    response3 = requests.post(base_url + '/get', params=query_params, headers=headers, data=payload)
    print('RESPONSE 3: ', response3.status_code) # gives 405
    print(response3.text) # gives 'Method Not Allowed' due to '/get'

    response4 = requests.post(base_url + '/post', params=query_params, headers=headers, data=payload)
    print('RESPONSE 4: ', response4.status_code) # gives 200
    print(response4.text)

    # SENDING FILES
    with open('txt.txt') as doc:  # context mngr

        files1 = {
            'image_file': doc # file descriptor as var from CM
        }
        # request is in a scope of the CM
        response5 = requests.post(url=base_url + '/post',
                                  params=query_params,
                                  headers=headers,
                                  data=payload,
                                  files=files1)

    # with open('toothbrush.jpg') as pic: - ERRORS
    #
    #     files2 = {
    #         'image_file': pic
    #     }
    #     response6 = requests.post(url=base_url + '/post',
    #                               params=query_params,
    #                               headers=headers,
    #                               data=payload,
    #                               files=files2)

    print('RESPONSE 5: ', response5.status_code)
    print(response5.text) # we'll get "image_file": "pam-pam" (doc's content) in the response

    # CONVERTING JSON RESPONSE
    print(response5.json())  # convert a json response into a dict
    print(type(response5.json()))

    # less convenient way to convert json with inner lib json
    print(json.loads(response5.text))
    print(type(json.loads(response5.text)))

    #or, in case, if the data is already a dict
    print(json.dumps(json.loads(response5.text))) # ( json string (dict) )
    print(type(json.dumps(json.loads(response5.text))))


    # print('RESPONSE 6: ', response6.status_code)
    #print(response6.text)

    # * - * - * - * - *
    # WHAT IF A RESOURCE ISN'T RESPONDING? WE CAN STOP CHECKING IT WITHIN TIMEOUT

    try:
        response7 = requests.post(url=base_url + '/post',
                                  timeout=1) # sec
        print('RESPONSE 7: ', response7.status_code)
        print(response7.text)
    # exception has to be specified as a requests exception,
    # because the error can be in non-request-related place (e.g. multiplication error)
    except requests.exceptions.ConnectTimeout:
        print('Timed-out! Resource is unavailable')


    # * - * - * - * - *
    # USING SESSION (so the transport level connection with a resource will be always open, no session re-initiating overhead)
    session = requests.Session()

    response8 = session.post(url=base_url + '/post')
    print('RESPONSE 8: ', response8.status_code)
    print(response8.text)

    # let's get timed-out in session
    try:
        response9 = session.post(url=base_url + '/post', timeout=0.01)
        print('RESPONSE 9: ', response9.status_code)
        print(response9.text)

        response10 = session.post(url=base_url + '/post', timeout=10)
        print('RESPONSE 10: ', response10.status_code)
        print(response10.text)

    except requests.exceptions.ConnectTimeout:
        print('Timed-out! Resource is unavailable')

    except requests.exceptions.ReadTimeout:
        print('Timed-out! Resource read timeout')



if __name__ == "__main__":
    main()
