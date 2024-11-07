import requests
from ..api_client import MoySkladAPIClient

class StockClient(MoySkladAPIClient):
    def get_stock_by_store(self):
        url = f"{self.BASE_URL}/report/stock/bystore"
        response = requests.get(url, headers=self.get_headers())
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get stock by store: {response.status_code}")

    def get_current_stock_by_store(self):
        url = f"{self.BASE_URL}/report/stock/bystore/current"
        response = requests.get(url, headers=self.get_headers())
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get current stock by store: {response.status_code}")