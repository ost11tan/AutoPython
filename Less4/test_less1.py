import yaml
import requests
import conftest
import logging

S = requests.Session()
with open("testdata.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)
    username, password, address, address2 = data["username"], data["password"], data["address"], data["address2"]


def test_rest(user_login):
    return (S.get(url=address, headers={'X-Auth-Token': user_login}))


def test_newpost(user_login):
    n = S.post(address2, headers={'X-Auth-Token': user_login},
               data={'title': 'Новый пост',
                     'description': data['test_description'],
                     'content': 'текст поста'})
    if n:
        return n.json()
    else:
        logging.error('не создан')


def get_my_posts(user_login):
    logging.debug('Open posts page')
    g = requests.get(address2,
                     headers={'X-Auth-Token': user_login})
    if g:
        listcont = [i['description'] for i in g.json()['data']]
        return listcont
    else:
        logging.error('Страница с постами не открылась')


def test_3(user_login, my_post):
    assert data['test_description'] in get_my_posts(user_login)
