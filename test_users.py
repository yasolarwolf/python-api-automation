import pytest
from schemas import UserSchema

def test_get_user_nested_address(api_client):
  response = api_client.get_user_by_id(1)
  assert response.status_code == 200
  user = UserSchema(**response.json())

  assert user.id == 1
  assert user.username == "Bret"
  assert user.address.city == "Gwenborough"
  assert user.company.name == "Romaguera-Crona"

def test_create_user(api_client):
  payload = {
     "name": "John Black",
      "username": "johnblack",
      "email": "johnblack@example.com",
  }
  response = api_client.create_user(payload)
  assert response.status_code == 201
  created_user = UserSchema(**response.json())
  assert created_user.name == "John Black"
  assert created_user.username == "johnblack"
  assert created_user.email == "johnblack@example.com"

def test_update_user(api_client):
  payload = {
    "name": "Updated Name",
    "username": "updated_user_name",
    "email": "updated_example.com",
  }
  response = api_client.update_user(1, payload)
  assert response.status_code == 200
  updated_user = UserSchema(**response.json())
  assert updated_user.name == "Updated Name"

def test_delete_user(api_client):
  response = api_client.delete_user(1)
  assert response.status_code == 200
