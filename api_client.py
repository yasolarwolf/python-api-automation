import requests

class ApiClient:

 def __init__(self,base_url):
   self.base_url = base_url

 def get_posts(self):
        return requests.get(f"{self.base_url}/posts")

 def get_post_by_id(self, post_id):
  url = (f"{self.base_url}/posts/{post_id}")
  return requests.get(url)

 def create_post(self, payload):
  return requests.post(f"{self.base_url}/posts", json=payload)

 def update_post_put(self,post_id,payload):
  return requests.put(f"{self.base_url}/posts/{post_id}", json=payload)

 def update_post_patch(self,post_id,payload):
  return requests.patch(f"{self.base_url}/posts/{post_id}", json=payload)

 def delete_post(self,post_id):
  return requests.delete(f"{self.base_url}/posts/{post_id}")

 def get_user_by_id(self, user_id):
  return requests.get(f"{self.base_url}/users/{user_id}")
