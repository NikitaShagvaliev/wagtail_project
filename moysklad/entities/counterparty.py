import requests
from ..api_client import MoySkladAPIClient

class CounterpartyClient(MoySkladAPIClient):
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

    def update_counterparty(self, counterparty_id, name=None, phone=None, email=None):
        url = f"{self.BASE_URL}/entity/counterparty/{counterparty_id}"
        data = {}
        if name:
            data["name"] = name
        if phone:
            data["phone"] = phone
        if email:
            data["email"] = email
        response = requests.put(url, headers=self.get_headers(), json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to update counterparty: {response.status_code}")

    def delete_counterparty(self, counterparty_id):
        url = f"{self.BASE_URL}/entity/counterparty/{counterparty_id}"
        response = requests.delete(url, headers=self.get_headers())
        if response.status_code == 200:
            return True
        else:
            raise Exception(f"Failed to delete counterparty: {response.status_code}")