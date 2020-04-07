import requests


def bot_post(user_text, user_date, user_time, inventory_type):
    method = 'wall.post'
    token = '0b4f1d46ca591427d72acd71469bfe026f177e0ab83935e608b2efa21d4e09442120df08460352320ef93'
    version = 5.103

    data = {
        'access_token': token,
        'owner_id': -191081370,
        'from_group': 1,
        'message': user_text + user_date + user_time + inventory_type,
        'signed': 0,
        'v': version}

    r = requests.post('https://api.vk.com/method/wall.post', data).json()

    print(r)
