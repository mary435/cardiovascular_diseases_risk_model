import bentoml
from bentoml.io import JSON
from pydantic import BaseModel

class PatientProfile(BaseModel):
    age: int               #years of age
    gender: int             #1 - women, 2 - men
    height: int             #cm
    weight: int             #kg
    ap_high: int            #systolic blood pressure
    ap_low: int             #diastolic blood pressure
    cholesterol: int        #1: normal, 2: above normal, 3: well above normal
    glucose: int            #1: normal, 2: above normal, 3: well above normal
    smoke: int              #0: no, 1: yes
    alcohol: int            #0: no, 1: yes
    physical_activity: int  #0: no, 1: yes


model_ref = bentoml.xgboost.get("cardiovascular_diseases_risk_model:latest")

dv = model_ref.custom_objects['dictVectorizer']

model_runner = model_ref.to_runner()

svc = bentoml.Service("cardiovascular_risk_classifier", runners=[model_runner])

@svc.api(input=JSON(pydantic_model=PatientProfile), output=JSON())
async def classify(application_data):

    patient_data = application_data.dict()

    vector = dv.transform(patient_data)
    prediction = await model_runner.predict.async_run(vector)
    
    result = prediction[0]

    return {"result": result} 