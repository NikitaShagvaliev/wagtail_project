import requests
import base64

class MoySkladClient:
    BASE_URL = "https://api.moysklad.ru/api/remap/1.2"

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.access_token = None

    def get_basic_auth_header(self):
        credentials = f"{self.login}:{self.password}"
        encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        return {
            "Authorization": f"Basic {encoded_credentials}"
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
        response = requests.post(url, headers=headers)
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
        response = requests.request(method, url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Request failed: {response.status_code}, {response.text}")


    def get_customer_orders(self):
        url = f"https://api.moysklad.ru/api/remap/1.2/entity/assortment"
        credentials = f"{self.login}:{self.password}"
        encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        headers = {
            "Authorization": f"Basic {encoded_credentials}"
        }
        response = requests.get(url, headers=headers)
        print(response)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get customer orders: {response.status_code}, {response.text}")
# Пример использования
login = "admin@egort123"
password = "egor86"

client = MoySkladClient(login, password)
try:
    access_token = client.get_customer_orders()
    print(f"Access Token: {access_token}")

    # Пример запроса с использованием токена доступа
    response = client.make_request("GET", "entity/customerorder")
    print(response)
except Exception as e:
    print(f"Error: {e}")