from pydantic import BaseModel
from pydantic import EmailStr


class user(BaseModel):

    username : str
    name : str
    password : str
    email : EmailStr
    phone : str
    gaurdian : str
    gaurdian_phone : str