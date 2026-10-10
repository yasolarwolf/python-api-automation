import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s [%(levelname)s] %(message)s" ,
  handlers=[logging.StreamHandler()],
)
logger = logging.getLogger("api_client")

class ApiClient:

 def __init__(self):
        self.base_url = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
        self.session = requests.Session()

 def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Unified entry point for sending HTTP requests with auto-logging."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"REQ: {method.upper()} {url}")

        if "json" in kwargs:
            logger.info(f"REQ BODY: {kwargs['json']}")

        response = self.session.request(method, url, **kwargs)

        logger.info(
            f"RESP STATUS: {response.status_code} | Time: {response.elapsed.total_seconds():.2f}s"
        )
        return response

 def get_posts(self):
        return self._request("GET", "/posts")

 def get_post_by_id(self, post_id):
  return self._request("GET", f"/posts/{post_id}")

 def create_post(self, payload):
  return self._request("POST", "/posts", json=payload)

 def update_post_put(self,post_id: int ,payload: dict):
  return self._request("PUT", f"/posts/{post_id}", json=payload)

 def update_post_patch(self,post_id: int,payload: dict):
  return self._request("PATCH", f"/posts/{post_id}", json=payload)

 def delete_post(self,post_id: int):
  return self._request("DELETE", f"/posts/{post_id}")

 def get_user_by_id(self, user_id: int):
  return self._request("GET", f"/users/{user_id}")

 def create_user(self, payload: dict):
   return self._request("POST", "/users", json=payload)

 def update_user(self,user_id: int, payload: dict):
  return self._request("PUT", f"/users/{user_id}", json=payload)
 
 def delete_user(self,user_id: int):
   return self._request("DELETE", f"/users/{user_id}")
