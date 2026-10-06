import allure
import pytest
from schemas import UserSchema

@allure.epic("API JSONPlaceholder")
@allure.feature("User management")

class TestUsers:

  @allure.story("Get a user")
  @allure.title("Successfully retrieving a user by ID with validation of nested fields")
  def test_get_user_nested_address(self, api_client):
    with allure.step("Sending a GET request to retrieve the user with ID=1"):
     response = api_client.get_user_by_id(1)
    with allure.step("Checking for status code 200 OK"):
     assert response.status_code == 200
    with allure.step("Response validation via a Pydantic schema"):
     user = UserSchema(**response.json())

    with allure.step("Validation of user data correctness"):
     assert user.id == 1
     assert user.username == "Bret"
     assert user.address.city == "Gwenborough"
     assert user.company.name == "Romaguera-Crona"

  @allure.story("Creating a user")
  @allure.title("Successful creation of a new user (POST)")
  def test_create_user(self, api_client):
    payload = {
      "name": "John Black",
        "username": "johnblack",
        "email": "johnblack@example.com",
    }
    with allure.step("Sending a POST request to create a user"):
     response = api_client.create_user(payload)
    with allure.step("Checking for status code 201 Created"):
     assert response.status_code == 201
    with allure.step("Response validation via a Pydantic schema"):
     created_user = UserSchema(**response.json())
    with allure.step("Validation of the created user's fields"):
     assert created_user.name == "John Black"
     assert created_user.username == "johnblack"
     assert created_user.email == "johnblack@example.com"

  @allure.story("User update")
  @allure.title("Successful user update (PUT)")
  def test_update_user(self, api_client):
    payload = {
      "name": "Updated Name",
      "username": "updated_user_name",
      "email": "updated_example.com",
    }
    with allure.step("Sending a PUT request to update data"):
     response = api_client.update_user(1, payload)
    with allure.step("Verify successful update"):
     assert response.status_code == 200
     updated_user = UserSchema(**response.json())
     assert updated_user.name == "Updated Name"

  @allure.story("User deletion")
  @allure.title("Successful user deletion by ID (DELETE)")
  def test_delete_user(self, api_client):
    with allure.step("Sending a DELETE request for user with ID=1"):
     response = api_client.delete_user(1)
    with allure.step("Checking status code 200 OK"):
     assert response.status_code == 200
