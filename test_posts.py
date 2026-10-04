import pytest
import requests

def test_get_status_code(api_client):
  response = api_client.get_posts()
  assert response.status_code == 200

def test_get_single_post(api_client):
  response = api_client.get_post_by_id(1)
  assert response.status_code == 200
  assert response.json()["id"] == 1

def test_request_non_existent_post(api_client):
  response = api_client.get_post_by_id(1999)
  assert response.status_code == 404

@pytest.mark.parametrize("post_id", [1,2,3])
def test_get_multiple_posts(api_client, post_id):
  response = api_client.get_post_by_id(post_id)
  assert response.status_code == 200
  assert response.json()["id"] == post_id

def test_create_post(api_client):
  create_post_data = {
    "title" : "new title 1",
    "body"  : "description of the title",
    "userId" : 1
  }

  response = api_client.create_post(create_post_data)
  assert response.status_code == 201
  data = response.json()
  assert data["title"] == "new title 1"
  assert "id" in data

def test_update_post_put(api_client):
  update_data = {
     "id" : 1,
     "title" : "updated title using PUT",
     "body"  : "updated body using PUT",
     "userId" : 1
  }
  response = api_client.update_post_put(1, update_data)
  assert response.status_code == 200
  assert response.json()["title"] == "updated title using PUT"

def test_update_post_patch(api_client):
  update_data = {
    "body" : "updated body using PATCH"
  }
  response = api_client.update_post_patch(1, update_data)
  assert response.status_code == 200
  assert response.json()["body"] == "updated body using PATCH"

def test_delete_post(api_client):
  response = api_client.delete_post(1)
  assert response.status_code == 200






  