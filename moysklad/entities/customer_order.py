import requests
from ..api_client import MoySkladAPIClient

class CustomerOrderClient(MoySkladAPIClient):
    def get_customer_orders(self):
        url = f"{self.BASE_URL}/entity/customerorder"
        response = requests.get(url, headers=self.get_headers())
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get customer orders: {response.status_code}")

    def create_customer_order(self, organization, agent, positions):
        url = f"{self.BASE_URL}/entity/customerorder"
        data = {
            "organization": {"meta": {"href": organization}},
            "agent": {"meta": {"href": agent}},
            "positions": positions
        }
        response = requests.post(url, headers=self.get_headers(), json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to create customer order: {response.status_code}")

    def update_customer_order(self, order_id, organization=None, agent=None, positions=None):
        url = f"{self.BASE_URL}/entity/customerorder/{order_id}"
        data = {}
        if organization:
            data["organization"] = {"meta": {"href": organization}}
        if agent:
            data["agent"] = {"meta": {"href": agent}}
        if positions:
            data["positions"] = positions
        response = requests.put(url, headers=self.get_headers(), json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to update customer order: {response.status_code}")

    def delete_customer_order(self, order_id):
        url = f"{self.BASE_URL}/entity/customerorder/{order_id}"
        response = requests.delete(url, headers=self.get_headers())
        if response.status_code == 200:
            return True
        else:
            raise Exception(f"Failed to delete customer order: {response.status_code}")