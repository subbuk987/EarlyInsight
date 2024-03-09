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

class login(BaseModel):

    username : str
    password : str

class medicalData(BaseModel):

    umid : str
    username : str
    age : int
    male : int
    female : int
    chestpaintype_asy : int
    chestpaintype_ata : int
    chestpaintype_nap : int
    chestpaintype_ta : int
    restingBP : int
    cholesterol : int
    fastingBS_0 : int
    fastingBS_1 : int
    restingECG_lvh : int
    restingECG_normal : int
    restingECG_st : int
    maxHR : int
    exerciseAngina_n  : int
    exerciseAngina_y  : int
    oldpeak : float
    st_slope_down : int
    st_slope_flat : int
    st_slope_up : int
    height  : float
    weight : float
    bmi : float
    physical_activity_lv_1 : int
    physical_activity_lv_2 : int
    physical_activity_lv_3 : int
    physical_activity_lv_4 : int
    pregnancies : int
    glucose : int
    skinThickness : int
    insulin : int
    diabetesPedigree : float