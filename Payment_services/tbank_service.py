import requests
import json

class TBankService:
    BASE_URL = "https://business.tbank.ru/openapi/sandbox"
    SANDBOX_TOKEN = "TBankSandboxToken"

    @staticmethod
    def perform_payment(payment_data):
        """
        Выполнение платежа через API Т-Банка.
        """
        url = f"{TBankService.BASE_URL}/secured/api/v1/payment/ruble-transfer/pay"
        headers = {
            "Authorization": f"Bearer {TBankService.SANDBOX_TOKEN}",
            "Content-Type": "application/json",
        }
        try:
            response = requests.post(url, headers=headers, data=json.dumps(payment_data))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении платежа: {e}")
            return None

    @staticmethod
    def get_statement(account_number, from_date, to_date=None):
        """
        Получение выписки по счету.
        """
        url = f"{TBankService.BASE_URL}/api/v1/statement"
        headers = {
            "Authorization": f"Bearer {TBankService.SANDBOX_TOKEN}",
            "Content-Type": "application/json",
        }
        params = {
            "accountNumber": account_number,
            "from": from_date,
        }
        if to_date:
            params["to"] = to_date

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении выписки: {e}")
            return None