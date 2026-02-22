from fastapi import FastAPI,HTTPException

from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.user_input_2 import UserInput2
from model.predict import predict_output
from model_2.predict_2 import predict_output2



app=FastAPI()
#adding endpoint for homepage
@app.get('/')
def home():
      return {"Welcome to atharva's api"}

#adding our api's health checkpoint 
@app.get('/health')
def health():
      return {
            'status':'OK',
            'Last updated':'Feb 17th 2026'
      }
      
@app.post('/predict_personal')
def predict_pcos(data:UserInput):
      #now we want to input data in form of pandas Data Frame as our model is trained on it
      input_df={'age':data.age, 
                              'weight':data.weight,
                               'height':data.height, 
                               'bmi':data.bmi, 
                               'had_abortion':data.had_abortion, 
                               'blood_group':data.blood_group,
                               'cycle_type':data.cycle_type, 
                               'marriage_years':data.marriage_years, 
                               'pregnant':data.pregnant,
                               'weight_gain':data.weight_gain,
                               'hair_growth':data.hair_growth, 
                               'skin_darkening':data.skin_darkening, 
                               'hair_loss':data.hair_loss, 
                               'pimples':data.pimples, 
                               'fast_food':data.fast_food,
                               'regular_exercise':data.regular_exercise, 
                               'pulse_rate':data.pulse_rate}
      try:
           return predict_output(input_df)
      except Exception as e:
            return JSONResponse(status_code=500,content=str(e))
      
@app.post('/predict_clinical')
def predict_pcos_clinical (data:UserInput2):
      input_df={'age':data.age, 
                              'weight':data.weight,
                               'height':data.height, 
                               'bmi':data.bmi, 
                               'had_abortion':data.had_abortion, 
                               'blood_group':data.blood_group,
                               'cycle_type':data.cycle_type, 
                               'marriage_years':data.marriage_years, 
                               'pregnant':data.pregnant,
                               'weight_gain':data.weight_gain,
                               'hair_growth':data.hair_growth, 
                               'skin_darkening':data.skin_darkening, 
                               'hair_loss':data.hair_loss, 
                               'pimples':data.pimples, 
                               'fast_food':data.fast_food,
                               'regular_exercise':data.regular_exercise, 
                               'pulse_rate':data.pulse_rate,
                               'respiratory_rate': data.respiratory_rate,
                              'hemoglobin': data.hemoglobin,
                              'fsh': data.fsh,
                              'lh': data.lh,
                              'lh_fsh_ratio': data.lh_fsh_ratio,
                              'waist_hip_ratio': data.waist_hip_ratio,
                              'tsh': data.tsh,
                              'amh': data.amh,
                              'prolactin': data.prolactin,
                              'vitamin_d3': data.vitamin_d3,
                              'progesterone': data.progesterone,
                              'random_blood_sugar': data.random_blood_sugar,
                              'bp_systolic': data.bp_systolic,
                              'bp_diastolic': data.bp_diastolic,
                              'avg_follicle_size': data.avg_follicle_size,
                              'total_follicles': data.total_follicles,
                              'endometrium_thickness': data.endometrium_thickness}
      try:
            return predict_output2(input_df)
      except Exception as e:
            return JSONResponse(status_code=500,content=str(e))

     

      






