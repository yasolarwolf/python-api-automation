import pytest
import allure
from schemas import PostSchema

@allure.epic("API JSONPlaceholder")
@allure.feature("Post management")
class TestPost:

  @allure.story("Retrieving posts")
  @allure.title("Get list of all posts")
  def test_get_status_code(self, api_client):
    with allure.step("Sending a GET request"):
     response = api_client.get_posts()
    with allure.step("Checking status code 200 OK"):
     assert response.status_code == 200

    with allure.step("Validating the list using a Pydantic schema"):
     posts = [PostSchema(**item) for item in response.json()]
     assert len(posts) > 0

  @allure.story("Retrieving posts")
  @allure.title("Retrieve post by ID")
  def test_get_single_post(self, api_client):
    with allure.step("Sending a GET request to /posts/1"):
     response = api_client.get_post_by_id(1)
    with allure.step("Checking status code 200 OK"):
     assert response.status_code == 200
    with allure.step("Validating the post using a Pydantic schema"):
     post = PostSchema(**response.json())
     assert post.id == 1

  @allure.story("Retrieving posts")
  @allure.title("Request for a non-existent post (404)")
  def test_request_non_existent_post(self, api_client):
    with allure.step("Sending a GET request for a non-existent ID=1999"):
     response = api_client.get_post_by_id(1999)
    with allure.step("Checking status code 404 Not Found"):
     assert response.status_code == 404

  @allure.story("Retrieving posts")
  @allure.title("Parameterized retrieval of posts by multiple IDs")
  @pytest.mark.parametrize("post_id", [1,2,3])
  def test_get_multiple_posts(self, api_client, post_id):
    with allure.step(f"Sending a GET request to /posts/{post_id}"):
     response = api_client.get_post_by_id(post_id)
    with allure.step("Checking status code 200 OK"):
     assert response.status_code == 200
    with allure.step("Validating the list using a Pydantic schema"):
     post = PostSchema(**response.json())
     assert post.id == post_id

  @allure.story("Creating a post")
  @allure.title("Successful creation of a new post")
  def test_create_post(self, api_client):
    create_post_data = {
      "title" : "new title 1",
      "body"  : "description of the title",
      "userId" : 1
    }
    with allure.step("Sending a POST request to create a post"):
     response = api_client.create_post(create_post_data)
    with allure.step("Checking status code 201 Created"):
     assert response.status_code == 201
    with allure.step("Verifying the fields of the created post"):
     created_post = PostSchema(**response.json())
     assert created_post.title == "new title 1"

  @allure.story("Post update")
  @allure.title("Full post update via PUT")
  def test_update_post_put(self, api_client):
    update_data = {
      "id" : 1,
      "title" : "updated title using PUT",
      "body"  : "updated body using PUT",
      "userId" : 1
    }
    with allure.step("Sending a PUT request for post ID=1"):
     response = api_client.update_post_put(1, update_data)
    with allure.step("Checking status code 200 OK"):
     assert response.status_code == 200
    with allure.step("Verifying the updated post body"):
     updated_post = PostSchema(**response.json())
     assert updated_post.title == "updated title using PUT"

  @allure.story("Post update")
  @allure.title("Partial post update via PATCH")
  def test_update_post_patch(self, api_client):
    update_data = {
      "body" : "updated body using PATCH"
    }
    with allure.step("Sending a PATCH request for post ID=1"):
     response = api_client.update_post_patch(1, update_data)
    with allure.step("Checking status code 200 OK"):
     assert response.status_code == 200
    with allure.step("Verifying the updated post body"):
     updated_post = PostSchema(**response.json())
     assert updated_post.body == "updated body using PATCH"

  @allure.story("Deleting a post")
  @allure.title("Successful post deletion by ID")
  def test_delete_post(self, api_client):
    with allure.step("Sending a DELETE request for the post with ID=1"):
     response = api_client.delete_post(1)
    with allure.step("Checking status code 200 OK"):
     assert response.status_code == 200






  