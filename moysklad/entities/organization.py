import requests
from ..api_client import MoySkladAPIClient

class OrganizationClient(MoySkladAPIClient):
    def get_organizations(self):
        url = f"{self.BASE_URL}/entity/organization"
        response = requests.get(url, headers=self.get_headers())
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get organizations: {response.status_code}")

    def create_organization(self, name):
        url = f"{self.BASE_URL}/entity/organization"
        data = {
            "name": name
        }
        response = requests.post(url, headers=self.get_headers(), json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to create organization: {response.status_code}")

    def update_organization(self, organization_id, name=None):
        url = f"{self.BASE_URL}/entity/organization/{organization_id}"
        data = {}
        if name:
            data["name"] = name
        response = requests.put(url, headers=self.get_headers(), json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to update organization: {response.status_code}")

    def delete_organization(self, organization_id):
        url = f"{self.BASE_URL}/entity/organization/{organization_id}"
        response = requests.delete(url, headers=self.get_headers())
        if response.status_code == 200:
            return True
        else:
            raise Exception(f"Failed to delete organization: {response.status_code}")