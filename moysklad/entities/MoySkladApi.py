from moysklad.api_client import MoySkladBaseClient

class CounterpartyClient(MoySkladBaseClient):
    def __init__(self, login, password, base_url, verify_ssl=True):
        super().__init__(login, password, base_url, "counterparty", verify_ssl)

class ProductClient(MoySkladBaseClient):
    def __init__(self, login, password, base_url, verify_ssl=True):
        super().__init__(login, password, base_url, "product", verify_ssl)

class InvoiceClient(MoySkladBaseClient):
    def __init__(self, login, password, base_url, verify_ssl=True):
        super().__init__(login, password, base_url, "invoiceout", verify_ssl)

class PurchaseOrderClient(MoySkladBaseClient):
    def __init__(self, login, password, base_url, verify_ssl=True):
        super().__init__(login, password, base_url, "purchaseorder", verify_ssl)

class StoreClient(MoySkladBaseClient):
    def __init__(self, login, password, base_url, verify_ssl=True):
        super().__init__(login, password, base_url, "store", verify_ssl)

class OrganizationClient(MoySkladBaseClient):
    def __init__(self, login, password, base_url, verify_ssl=True):
        super().__init__(login, password, base_url, "organization", verify_ssl)


class CustomerOrderClient(MoySkladBaseClient):
    def __init__(self, login, password, base_url, verify_ssl=True):
        super().__init__(login, password, base_url, "customerorder", verify_ssl)

    def create_customer_order(self, organization, agent, positions):
        data = {
            "organization": {"meta": {"href": organization}},
            "agent": {"meta": {"href": agent}},
            "positions": positions
        }
        return super().post(data)