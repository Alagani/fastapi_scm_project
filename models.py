from pydantic import BaseModel, EmailStr
from datetime import datetime

class Users(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str ="user"
    created_at: datetime = datetime.now()


class Shipment(BaseModel):
    shipment_number: int 
    container_number: int
    goods_number: int 
    route: str
    goods_type: str
    device_id: int 
    expected_delivery_date:str
    po_number:int 
    delivery_number:int
    ndc_number:int
    batch_id:int
    shipment_description:str
    user_id:EmailStr



class Devicedata(BaseModel):
    device_id:int
    battery_level:float
    temperature:float
    route_to:str
    route_from:str