import os
import requests
import base64

# Отключение проверки SSL-сертификатов (не рекомендуется для производственного использования)
os.environ['CURL_CA_BUNDLE'] = ''

class MoySkladAPIClient:
    BASE_URL = "https://api.moysklad.ru/api/remap/1.2"

    def __init__(self, login, password, verify_ssl=True):
        self.login = login
        self.password = password
        self.access_token = None
        self.session = requests.Session()
        self.session.verify = verify_ssl  # Устанавливаем проверку SSL-сертификатов

    def get_basic_auth_header(self):
        credentials = f"{self.login}:{self.password}"
        encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        return {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/json"
        }

    def get_token_auth_header(self):
        if not self.access_token:
            raise Exception("Access token is not set")
        return {
            "Authorization": f"Bearer {self.access_token}"
        }

    def get_access_token(self):
        url = f"{self.BASE_URL}/security/token"
        headers = self.get_basic_auth_header()
        response = self.session.post(url, headers=headers)
        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data["access_token"]
            return self.access_token
        else:
            raise Exception(f"Failed to get token: {response.status_code}, {response.text}")

    def make_request(self, method, endpoint, headers=None, data=None):
        url = f"{self.BASE_URL}/{endpoint}"
        if not headers:
            headers = self.get_token_auth_header()
        response = self.session.request(method, url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Request failed: {response.status_code}, {response.text}")

    def get_counterparties(self):
        url = f"{self.BASE_URL}/entity/counterparty"
        response = self.session.get(url, headers=self.get_basic_auth_header())
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get counterparties: {response.status_code}, {response.text}")