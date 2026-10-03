import pytest
import requests

def test_get_status_code(base_url):
  response = requests.get(f"{base_url}/posts")
  assert response.status_code == 200

def test_create_post(base_url):
  create_post_data = {
    "title" : "new title 1",
    "body"  : "description of the title",
    "userId" : 1
  }

  response = requests.post(f"{base_url}/posts", json = create_post_data)

  assert response.status_code == 201
  data = response.json()
  assert data["title"] == "new title 1"
  assert "id" in data

def test_delete_post(base_url):
  response = requests.delete(f"{base_url}/posts/1")
  assert response.status_code == 200

def test_request_non_existent_post(base_url):
  response = requests.get(f"{base_url}/posts/1999")
  assert response.status_code == 404

@pytest.mark.parametrize("post_id", [1,2,3])
def test_get_multiple_posts(base_url, post_id):
  response = requests.get(f"{base_url}/posts/{post_id}")
  assert response.status_code == 200
  data = response.json()
  assert data["id"] == post_id
  