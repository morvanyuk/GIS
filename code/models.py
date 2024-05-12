from pydantic import BaseModel

# Points
class Point(BaseModel):
    lat: str
    long: str

class TwoPoints(BaseModel):
    first: Point
    second: Point

class Restaurant(BaseModel):
    restaurant_id: int
    restaurant_name: str
    coordinate: Point

class Order(BaseModel):
    coordinate: Point
    object_id: int
    restaurant_id: int