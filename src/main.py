import requests
import json
import pprint

from client import Client

def main():
    login = 'b.zhetpisbaev@innopolis.university'
    password = 'ASDert12@!3'
    base_url = 'https://dev-cloud.acronis.com/api/2'

    client = Client(base_url, login, password)
    user_account = client.get_user_account()
    tenant_id = user_account['tenant_id']

    client = client.get_client(base_url, tenant_id)
    client_creds = client['client_id'], client['client_secret']

    # base_url = get_server_url_by_account(login)

    # user_account = auth.get_user_account(base_url, (login, password))
    # tenant_id = user_account['tenant_id']

    # client_info = {
    #     'type': 'agent',
    #     'tenant_id': tenant_id,
    #     'token_endpoint_auth_method': 'client_secret_basic',
    #     'data': {'name': 'TestApp'},
    # }
    # client_info = json.dumps(client_info, indent=4)
    # pprint.pprint(client_info)

    # client = auth.get_client(base_url, (login, password), client_info)
    # client_creds = client['client_id'], client['client_secret']
    
    # token_info = auth.get_token_info(base_url, client_creds)
    # auth = {'Authorization': 'Bearer ' + token_info['access_token']}
    # pprint.pprint(auth)

    # print(f'f:{tenant_id}')
    # users = auth.get_tenant_users(base_url, auth, tenant_id)
    # pprint.pprint(users)

    # user = auth.get_user(base_url, auth, users['items'][0])
    # pprint.pprint(user)

    # tenant = auth.get_tenant(base_url, auth, )
    # pprint.pprint(tenant)

    # tenant_usages = auth.get_tenants_usages(base_url, [tenant_id], auth)
    # pprint.pprint(tenant_usages)

main()