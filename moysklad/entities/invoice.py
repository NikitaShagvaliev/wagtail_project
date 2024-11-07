import requests
from ..api_client import MoySkladAPIClient

class InvoiceClient(MoySkladAPIClient):
    def get_invoices(self):
        url = f"{self.BASE_URL}/entity/invoiceout"
        response = requests.get(url, headers=self.get_headers())
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get invoices: {response.status_code}")

    def create_invoice(self, organization, agent, positions):
        url = f"{self.BASE_URL}/entity/invoiceout"
        data = {
            "organization": {"meta": {"href": organization}},
            "agent": {"meta": {"href": agent}},
            "positions": positions
        }
        response = requests.post(url, headers=self.get_headers(), json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to create invoice: {response.status_code}")

    def update_invoice(self, invoice_id, organization=None, agent=None, positions=None):
        url = f"{self.BASE_URL}/entity/invoiceout/{invoice_id}"
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
            raise Exception(f"Failed to update invoice: {response.status_code}")

    def delete_invoice(self, invoice_id):
        url = f"{self.BASE_URL}/entity/invoiceout/{invoice_id}"
        response = requests.delete(url, headers=self.get_headers())
        if response.status_code == 200:
            return True
        else:
            raise Exception(f"Failed to delete invoice: {response.status_code}")