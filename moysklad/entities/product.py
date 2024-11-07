import requests
from ..api_client import MoySkladAPIClient

class ProductClient(MoySkladAPIClient):
    def get_products(self):
        url = f"{self.BASE_URL}/entity/product"
        response = requests.get(url, headers=self.get_headers())
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get products: {response.status_code}")

    def create_product(self, name, code=None, description=None):
        url = f"{self.BASE_URL}/entity/product"
        data = {
            "name": name,
            "code": code,
            "description": description
        }
        response = requests.post(url, headers=self.get_headers(), json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to create product: {response.status_code}")

    def update_product(self, product_id, name=None, code=None, description=None):
        url = f"{self.BASE_URL}/entity/product/{product_id}"
        data = {}
        if name:
            data["name"] = name
        if code:
            data["code"] = code
        if description:
            data["description"] = description
        response = requests.put(url, headers=self.get_headers(), json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to update product: {response.status_code}")

    def delete_product(self, product_id):
        url = f"{self.BASE_URL}/entity/product/{product_id}"
        response = requests.delete(url, headers=self.get_headers())
        if response.status_code == 200:
            return True
        else:
            raise Exception(f"Failed to delete product: {response.status_code}")