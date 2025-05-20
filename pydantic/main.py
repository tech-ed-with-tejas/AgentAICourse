from pydantic import BaseModel,Field
from typing import Optional,List,Dict

class Address(BaseModel):
    city:str
    zipcode:str
    street:str
class Employee(BaseModel):
    id:int
    name:str
    salary:Optional[float]
    is_active :Optional[bool]
    address:Address

class Item(BaseModel):
    name:str =Field(min_lenght=2,max_lenght=100)
    price:int=Field(gt=0,le=10000)
    quantity:int =Field(ge=0,default=1) 


