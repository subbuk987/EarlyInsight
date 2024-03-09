from fastapi import FastAPI ,Depends ,HTTPException ,status
import models
from database import engine, sessionlocal ,get_db 
from schemas import user , login ,medicalData
from sqlalchemy.orm import Session
from hashing import Hash
from trained_models.predictor import prediction

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.post('/getuser')
def get_user(userid : str, db : Session = Depends(get_db)):
    username = db.query(models.User).filter(models.User.username==userid).first()
    return username

@app.post('/signup')
def create_user(user_details : user , db : Session = Depends(get_db)):
    usertest = db.query(models.User).filter(models.User.username==user_details.username).first()

    if usertest:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User already exists")
    else:
        users = models.User(username=user_details.username,
                        name = user_details.name,
                        password = Hash.encrypt(user_details.password),
                        email = user_details.email,
                        phone = user_details.phone,
                        gaurdian = user_details.gaurdian,
                        gaurdian_phone = user_details.gaurdian_phone)
        db.add(users)
        db.commit()
        db.refresh(users) 


    
   



@app.post('/login')
def login(login_details : login,db : Session = Depends(get_db)):
    usertest = db.query(models.User).filter(models.User.username==login_details.username).first()
    
    if not usertest:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Does Not Exist, Please register.")
    else:
        passcheck = Hash.verify(login_details.password,usertest.password)
        if passcheck:
            return "Login Successful"
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect Password")


@app.post('/getmedicaldata')
def getmedicals(medicals : medicalData , db :Session = Depends(get_db)):
    meds = models.UserMedical(umid = medicals.umid,
                              username = medicals.username,
                              age = medicals.age,
                              male = medicals.male,
                              female = medicals.female,
                              chestpaintype_asy = medicals.chestpaintype_asy,
                              chestpaintype_ata = medicals.chestpaintype_ata,
                              chestpaintype_nap = medicals.chestpaintype_nap,
                              chestpaintype_ta = medicals.chestpaintype_ta,
                              restingBP = medicals.restingBP,
                              cholesterol = medicals.cholesterol,
                              fastingBS_0 = medicals.fastingBS_0,
                              fastingBS_1 = medicals.fastingBS_1,
                              restingECG_lvh = medicals.restingECG_lvh,
                              restingECG_normal = medicals.restingECG_normal,
                              restingECG_st = medicals.restingECG_st,
                              maxHR = medicals.maxHR,
                              exerciseAngina_n  = medicals.exerciseAngina_n,
                              exerciseAngina_y  = medicals.exerciseAngina_y,
                              oldpeak = medicals.oldpeak,
                              st_slope_down = medicals.st_slope_down,
                              st_slope_flat = medicals.st_slope_flat,
                              st_slope_up = medicals.st_slope_up,
                              height  = medicals.height,
                              weight = medicals.weight,
                              bmi = medicals.bmi,
                              physical_activity_lv_1 = medicals.physical_activity_lv_1,
                              physical_activity_lv_2 = medicals.physical_activity_lv_2,
                              physical_activity_lv_3 = medicals.physical_activity_lv_3,
                              physical_activity_lv_4 = medicals.physical_activity_lv_4,
                              pregnancies = medicals.pregnancies,
                              glucose = medicals.glucose,
                              skinThickness = medicals.skinThickness,
                              insulin = medicals.insulin,
                              diabetesPedigree = medicals.diabetesPedigree
                              )
    db.add(meds)
    db.commit()
    db.refresh(meds)


@app.post('/getdiabeticinfo')
def getDiabeticInfo(username : str, db : Session = Depends(get_db)):
    user = db.query(models.UserMedical).filter(models.UserMedical.username==username).first()
    diabetes_requirements = []
    diabetes_requirements.append(user.pregnancies)
    diabetes_requirements.append(user.glucose)
    diabetes_requirements.append(user.restingBP)
    diabetes_requirements.append(user.skinThickness)
    diabetes_requirements.append(user.insulin)
    diabetes_requirements.append(user.bmi)
    diabetes_requirements.append(user.diabetesPedigree)
    diabetes_requirements.append(user.age)
    dia_predict = prediction.predict_diabetes(diabetes_requirements)
    return dia_predict

@app.post('/getobesityinfo')
def getObesityInfo(username : str, db :Session = Depends(get_db)):
    user = db.query(models.UserMedical).filter(models.UserMedical.username==username).first()
    obese_requirements = []
    obese_requirements.append(user.age)
    obese_requirements.append(user.height)
    obese_requirements.append(user.weight)
    obese_requirements.append(user.bmi)
    obese_requirements.append(user.female)
    obese_requirements.append(user.male)
    obese_requirements.append(user.physical_activity_lv_1)
    obese_requirements.append(user.physical_activity_lv_2)
    obese_requirements.append(user.physical_activity_lv_3)
    obese_requirements.append(user.physical_activity_lv_4)
    obesity_predict = prediction.predict_obesity(obese_requirements)

    return obesity_predict

@app.post('/gethearthinfo')
def getHeartInfo(username : str, db : Session = Depends(get_db)):
    user = db.query(models.UserMedical).filter(models.UserMedical.username==username).first()
    heart_requirements = []
    heart_requirements.append(user.age)
    heart_requirements.append(user.restingBP)
    heart_requirements.append(user.cholesterol)
    heart_requirements.append(user.maxHR)
    heart_requirements.append(user.oldpeak)
    heart_requirements.append(user.female)
    heart_requirements.append(user.male)
    heart_requirements.append(user.chestpaintype_asy)
    heart_requirements.append(user.chestpaintype_ata)
    heart_requirements.append(user.chestpaintype_nap)
    heart_requirements.append(user.chestpaintype_ta)
    heart_requirements.append(user.fastingBS_0)
    heart_requirements.append(user.fastingBS_1)
    heart_requirements.append(user.restingECG_lvh)
    heart_requirements.append(user.restingECG_normal)
    heart_requirements.append(user.restingECG_st)
    heart_requirements.append(user.exerciseAngina_n)
    heart_requirements.append(user.exerciseAngina_y)
    heart_requirements.append(user.st_slope_down)
    heart_requirements.append(user.st_slope_flat)
    heart_requirements.append(user.st_slope_up)

    heart_predictions = prediction.predict_heart_health(heart_requirements)

    return heart_predictions



