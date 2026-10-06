from pydantic import BaseModel
from typing import Optional

class PostSchema(BaseModel):
  id: int
  title: str
  body: str
  userId: int

class GeoSchema(BaseModel):
  lat: str
  lng: str

class AddressSchema(BaseModel):
  street: str
  suite: str
  city: str
  zipcode: str
  geo : GeoSchema

class CompanySchema(BaseModel):
  name: str
  catchPhrase: str
  bs: str

class UserSchema(BaseModel):
  id: int
  name: str
  username: str
  email: str
  address: Optional[AddressSchema] = None
  phone: Optional[str] = None
  website: Optional[str] = None
  company: Optional[CompanySchema] = None
