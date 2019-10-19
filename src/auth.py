import requests
import json
import pprint


def get_token_info(base_url, client_creds):
    response = requests.post(
        f'{base_url}/idp/token',
        auth=client_creds,
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        data={'grant_type': 'client_credentials'}
    )

    if not response.status_code == 200:
        raise Exception(f'Response: {response.status_code} | {response.json()}')

    return response.json()

def get_tenants_usages(base_url, tenant_ids, auth):
    params = {
        'tenants': ','.join(tenant_ids)
    }
    auth = {'Authorization': 'Bearer ' + 'gAAAAABdqqvwWNO1-tJx_AM3CEg6_Ys0-97JLS-VV8wyaB9yZh9kufbwhFMEvi0qkXRi0ZAeuTVpO-n9lfGL5VuWYKV8_bGGInXCaVqHMqQ6Jq_cXOxcQzboOQqEihTH-oitDWBgHx6HxK-UDOSqCO2qXf6q4ioEQw=='}
    response = requests.get(f'{base_url}/tenants/usages', headers=auth, params=params)

    if not response.status_code == 200:
        raise Exception(f'Response: {response.status_code} | {response.json()}')

    return response.json()

def get_tenants_usages_by_cookies(base_url, tenant_ids, auth):
    params = {
        'tenants': ','.join(tenant_ids)
    }
    cookies = {
        'AUTH_SERVER_SECURE' : '"gAAAAABdqj8H7DF-CAWIqy8t1_wX1KlDM62TWcXRS1yB-ybk-CLJohZ8zHyUmNOBKJPyxqZQVMjweBIzwHMDZj8K2I53LvHTXR5JAyXOZ-Ub_WcU86VNk6fmAlK1Xf5gzyzWx2SktR4GEeza7YOvJoJvm4XjdjqfKw=="'
    }
    response = requests.get(f'{base_url}/tenants/usages', params=params, cookies=cookies)

    if not response.status_code == 200:
        raise Exception(f'Response: {response.status_code} | {response.json()}')

    return response.json()

def get_tenant(base_url, auth, tenant_id):
    response = requests.get(f'{base_url}/tenants/{tenant_id}', headers=auth)

    if not response.status_code == 200:
        raise Exception(f'Response: {response.status_code} | {response.json()}')

    return response.json()

def get_tenant_users(base_url, auth, tenant_id):
    response = requests.get(f'{base_url}/tenants/{tenant_id}/users', headers=auth)

    if not response.status_code == 200:
        raise Exception(f'Response: {response.status_code} | {response.json()}')

    return response.json()

def get_user(base_url, auth, uuid):
    response = requests.get(f'{base_url}/users/{uuid}', headers=auth)

    if not response.status_code == 200:
        raise Exception(f'Response: {response.status_code} | {response.json()}')

    return response.json()
