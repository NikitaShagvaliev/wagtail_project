import requests

class MoySkladAPIClient:
    BASE_URL = "https://online.moysklad.ru/api/remap/1.2"

    def __init__(self, access_token):
        self.access_token = access_token

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    def get_counterparties(self):
        url = f"{self.BASE_URL}/entity/counterparty"
        response = requests.get(url, headers=self.get_headers())
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get counterparties: {response.status_code}")

    def create_counterparty(self, name, phone=None, email=None):
        url = f"{self.BASE_URL}/entity/counterparty"
        data = {
            "name": name,
            "phone": phone,
            "email": email
        }
        response = requests.post(url, headers=self.get_headers(), json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to create counterparty: {response.status_code}")