from pydantic import BaseModel
from bson import ObjectId
from typing import List 

class Favourite(BaseModel):
    name: str
    address: str
    type: List[str]
    leisure_type: str
    photo_ref: List[str]
    lat: str
    lng: str
    rating: float
    place_id: str
    _id: str
    