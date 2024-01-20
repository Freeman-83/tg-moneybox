import os

from dotenv import load_dotenv

from openapi_client import Configuration
from openapi_client.api.reports_api import ReportsApi
from openapi_client.api_client import ApiClient

load_dotenv()

TOKEN = os.getenv('TOKEN')
API_TOKEN = os.getenv('API_TOKEN')

HEADERS = {'Authorization': f'Token {API_TOKEN}'}

url = 'http://moneybox.ddns.net'


def get_reports_api():
    config = Configuration()
    config.access_token = f'token {API_TOKEN}'
    config.host = url
    api_client = ApiClient(
        configuration=config,
        header_name='Authorization',
        header_value=HEADERS['Authorization']
    )
    reports_api = ReportsApi(api_client)
    return reports_api
