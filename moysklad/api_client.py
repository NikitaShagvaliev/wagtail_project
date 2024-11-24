import requests
import base64

class MoySkladAPIClient:
    BASE_URL = "https://api.moysklad.ru/api/remap/1.2"

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def get_basic_auth_header(self):
        credentials = f"{self.login}:{self.password}"
        encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        return {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/json"
        }

    def get_counterparties(self):
        url = f"{self.BASE_URL}/entity/counterparty"
        response = requests.get(url, headers=self.get_basic_auth_header())
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get counterparties: {response.status_code}, {response.text}")

    def create_counterparty(self, name, phone=None, email=None):
        url = f"{self.BASE_URL}/entity/counterparty"
        data = {
            "name": name,
            "phone": phone,
            "email": email
        }
        response = requests.post(url, headers=self.get_basic_auth_header(), json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to create counterparty: {response.status_code}, {response.text}")

# Пример использования
login = "admin@egort123"
password = "egor86"

client = MoySkladAPIClient(login, password)
try:
    counterparties = client.get_counterparties()
    print(counterparties)

    new_counterparty = client.create_counterparty("New Counterparty", phone="123456789", email="new@example.com")
    print(new_counterparty)
except Exception as e:
    print(f"Error: {e}")