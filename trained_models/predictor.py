from joblib import load, dump
from fastapi import Depends
import numpy as np
from database import get_db
from sqlalchemy.orm import Session
import models
import os
from typing import List

heartfile = './trained_models/best_model_heart_failure.joblib'
diabetesfile = './trained_models/best_diabetes_model.joblib'
obesityfile = './trained_models/best_model_obesity_analysis.joblib'
heart_model = load(filename=heartfile)
diabetes_model = load(filename=diabetesfile)
obesity_model = load(filename=obesityfile)

class prediction():
    
    def predict_heart_health(heart_details : List):
        np.random.seed(27)
        Heart_array = []
        Heart_array.append(heart_details)
        heart_probability = heart_model.predict_proba(np.array(Heart_array))
        proba = {
            "Heart Safety Probability" : heart_probability[0][0],
            "Heart Failure Probability" : heart_probability[0][1]
        }
        return proba
        

    def predict_diabetes(diabetes_details : List):
        diabetes_Array = []
        diabetes_Array.append(diabetes_details)
        diabetes_probability = diabetes_model.predict_proba(np.array(diabetes_Array))
        proba = {
            "Non - Diabetic Chances" : diabetes_probability[0][0],
            "Diabetic Chances" : diabetes_probability[0][1]
        }
        return proba
        
    def predict_obesity(obese_requirements : List):
        obesity_Array = []
        obesity_Array.append(obese_requirements)
        obesity_category = obesity_model.predict(np.array(obesity_Array))
        predict = {
            "Normal Weight" : obesity_category[0][0],
            "Overweight" : obesity_category[0][1],
            "Obese" : obesity_category[0][2],
            "Underweight" : obesity_category[0][3]
        }
        return predict
