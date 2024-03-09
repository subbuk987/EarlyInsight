from sqlalchemy import String,Integer,ForeignKey,Column,Float
from database import Base
from pydantic import EmailStr

class User(Base):

    __tablename__ = "users"

    username = Column(String(20),primary_key=True)
    name = Column(String(30))
    password = Column(String(200))
    email = Column(String(50))
    phone = Column(String(10))
    gaurdian = Column(String(30))
    gaurdian_phone = Column(String(10))


class UserMedical(Base):

    __tablename__ = "usermedical"

    umid = Column(String(30),primary_key=True)
    username = Column(String(20))
    age = Column(Integer)
    male = Column(Integer)
    female = Column(Integer)
    chestpaintype_asy = Column(Integer)
    chestpaintype_ata = Column(Integer)
    chestpaintype_nap = Column(Integer)
    chestpaintype_ta = Column(Integer)
    restingBP = Column(Integer)
    cholesterol = Column(Integer)
    fastingBS_0 = Column(Integer)
    fastingBS_1 = Column(Integer)
    restingECG_lvh = Column(Integer)
    restingECG_normal = Column(Integer)
    restingECG_st = Column(Integer)
    maxHR = Column(Integer)
    exerciseAngina_n  = Column(Integer)
    exerciseAngina_y  = Column(Integer)
    oldpeak = Column(Float)
    st_slope_down = Column(Integer)
    st_slope_flat = Column(Integer)
    st_slope_up = Column(Integer)
    height  = Column(Float)
    weight = Column(Float)
    bmi = Column(Float)
    physical_activity_lv_1 = Column(Integer)
    physical_activity_lv_2 = Column(Integer)
    physical_activity_lv_3 = Column(Integer)
    physical_activity_lv_4 = Column(Integer)
    pregnancies = Column(Integer)
    glucose = Column(Integer)
    skinThickness = Column(Integer)
    insulin = Column(Integer)
    diabetesPedigree = Column(Float)

class UserPreds(Base):

    __tablename__ = "userpreds"

    pid = Column(String(20),primary_key=True)
    username = Column(String(20))
    heartPred_0 = Column(Float)
    heartPred_1 = Column(Float)
    obesityPred = Column(Float)
    diabeticPred_0 = Column(Float)
    diabeticPred_1 = Column(Float)