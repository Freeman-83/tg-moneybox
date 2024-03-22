import os

from dotenv import load_dotenv

from openapi_client import Configuration
from openapi_client.api.reports_api import ReportsApi
from openapi_client.api.expenses_api import ExpensesApi
from openapi_client.api.incomes_api import IncomesApi

from openapi_client.api_client import ApiClient


load_dotenv()


TOKEN: str = os.getenv('TOKEN')
API_TOKEN: str = os.getenv('API_TOKEN')

# ENDPOINT: str = 'http://moneybox.ddns.net/api/v1/report/'
HEADERS: dict = {'Authorization': f'Token {API_TOKEN}',
                 'Content-Type': 'application/json'}

report_url = 'http://moneybox.ddns.net'


def initialize_expenses_api():
    config = Configuration()
    config.access_token = f'Token {API_TOKEN}'
    config.host = report_url
    api_client = ApiClient(
        configuration=config, 
        header_name='Authorization', 
        header_value=HEADERS['Authorization'])
    expenses_api = ExpensesApi(api_client)
    return expenses_api


def initialize_reports_api():
    config = Configuration()
    config.access_token = f'Token {API_TOKEN}'
    config.host = report_url
    api_client = ApiClient(
        configuration=config,
        header_name='Authorization',
        header_value=HEADERS['Authorization']
    )
    reports_api = ReportsApi(api_client)
    return reports_api


def initialize_incomes_api():
    config = Configuration()
    config.access_token = f'Token {API_TOKEN}'
    config.host = report_url
    api_client = ApiClient(
        configuration=config, 
        header_name='Authorization', 
        header_value=HEADERS['Authorization'])
    invites_api = IncomesApi(api_client)
    return invites_api