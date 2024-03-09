from sqlalchemy import String,Integer,ForeignKey,Column,Float
from database import Base
from pydantic import EmailStr

class User(Base):

    __tablename__ = "users"

    username = Column(String(20),primary_key=True)
    name = Column(String(30))
    password = Column(String(20))
    email = Column(String(50))
    Phone = Column(String(10))
    Gaurdian = Column(String(30))
    Gaurdian_phn = Column(String(10))


class UserMedical(Base):

    __tablename__ = "usermedical"

    umid = Column(String(30),primary_key=True)
    username = Column(String(20))
    age = Column(Integer)
    male = Column(Integer)
    female = Column(Integer)
    chestpaintype = Column(String(10))
    restingBP = Column(Integer)
    cholesterol = Column(Integer)
    fastingBS = Column(Integer)
    restingECG = Column(String(20))
    maxHR = Column(Integer)
    exerciseAngina  = Column(String(10))
    oldpeak = Column(Float)
    st_slope = Column(String(10))
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
    heartPred = Column(Float)
    obesityPred = Column(Float)
    diabeticPred = Column(Float)