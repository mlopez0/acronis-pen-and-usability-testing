import requests
import json
import pprint

import api_base

class Client(api_base.ApiBase):
    def __init__(self, base_url, login, password):
        super().__init__()
        self.base_url = base_url
        self.login = login
        self.password = password

    def get_creds(self):
        return (self.login, self.password)

    def get_server_url_by_account(self):
        url = 'https://cloud.acronis.com/api/1/accounts'
        params= {
            'login': self.login
        }

        result = self.get(url, params=params)
        server_url = result['server_url']
        server_url = f'{server_url}/api/2'

        return server_url

    def get_user_account(self):
        return super().get(f'{self.base_url}/users/me',
            auth=(self.login, self.password))

    def get(self, base_url, tenant_id):
        client_info = {
            'type': 'agent',
            'tenant_id': tenant_id,
            'token_endpoint_auth_method': 'client_secret_basic',
            'data': {'name': 'TestApp'},
        }
        client_info = json.dumps(client_info, indent=4)
        
        return super().post(f'{base_url}/clients',
            auth=self.get_creds(),
            headers={'Content-Type': 'application/json'},
            data=client_info
        )
