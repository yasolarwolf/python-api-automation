import os
import pytest
from api_client import ApiClient
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def api_client():
  base_url = os.getenv("BASE_URL","https://jsonplaceholder.typicode.com") 
  return ApiClient(base_url)

