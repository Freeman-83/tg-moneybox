import os

from dotenv import load_dotenv

from openapi_client import Configuration
from openapi_client.api.reports_api import ReportsApi
from openapi_client.api_client import ApiClient


load_dotenv()


TOKEN: str = os.getenv('TOKEN')
API_TOKEN: str = os.getenv('API_TOKEN')

ENDPOINT: str = 'http://moneybox.ddns.net/api/v1/report/'
HEADERS: dict = {'Authorization': f'Token {API_TOKEN}'}


def initialize_reports_api():
    config = Configuration()
    config.access_token = f'Token {API_TOKEN}'
    config.host = ENDPOINT
    api_client = ApiClient(
        configuration=config,
        header_name='Authorization',
        header_value=HEADERS['Authorization']
    )
    reports_api = ReportsApi(api_client)
    return reports_api
