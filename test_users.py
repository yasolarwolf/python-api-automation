import pytest
import requests

def test_get_user_nested_address(api_client):
  response = api_client.get_user_by_id(1)
  assert response.status_code == 200
  data = response.json()

  assert data["id"] == 1
  assert data["username"] == "Bret"
  assert data["address"]["city"] == "Gwenborough"
  assert data["company"]["name"] == "Romaguera-Crona"