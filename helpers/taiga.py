# git clone https://github.com/kaleidos-ventures/taiga.git
# free alternative to Trello

# taiga - docker - docker-compose file
# cd \taiga\docker
# docker-compose up

import requests

api_base_url = 'http://localhost:9000/api/v1'
project_id = 1
username='admin'
user_password='admin'

def get_auth_token_user_id():
    user_data = {
        'password': user_password,
        'type': 'normal',
        'username': username
    }

    response = requests.post(f'{api_base_url}/auth', json=user_data)
    if response.status_code == 200:
        return response.json()['auth_token'], response.json()['id']
    raise Exception('Auth error')

def create_task(subj, description):
    auth_token, user_id = get_auth_token_user_id()
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    task_details = {
        'project': project_id,
        'subject': subj,
        'description': description,
        'status': 1,
        'assigned_to': user_id
    }

    response = requests.post(f'{api_base_url}/userstories', headers, json=task_details)

    if response.status_code == 201:
        print('Task is created')
    else:
        print('Failed to create task')


if __name__ == '__main__':
    create_task('my task', 'test')