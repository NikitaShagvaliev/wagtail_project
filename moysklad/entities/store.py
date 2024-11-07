import requests
from ..api_client import MoySkladAPIClient

class StoreClient(MoySkladAPIClient):
    def get_stores(self):
        url = f"{self.BASE_URL}/entity/store"
        response = requests.get(url, headers=self.get_headers())
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get stores: {response.status_code}")

    def create_store(self, name):
        url = f"{self.BASE_URL}/entity/store"
        data = {
            "name": name
        }
        response = requests.post(url, headers=self.get_headers(), json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to create store: {response.status_code}")

    def update_store(self, store_id, name=None):
        url = f"{self.BASE_URL}/entity/store/{store_id}"
        data = {}
        if name:
            data["name"] = name
        response = requests.put(url, headers=self.get_headers(), json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to update store: {response.status_code}")

    def delete_store(self, store_id):
        url = f"{self.BASE_URL}/entity/store/{store_id}"
        response = requests.delete(url, headers=self.get_headers())
        if response.status_code == 200:
            return True
        else:
            raise Exception(f"Failed to delete store: {response.status_code}")