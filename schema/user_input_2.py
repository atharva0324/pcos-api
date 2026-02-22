from pydantic import BaseModel,Field,computed_field,field_validator,model_validator
from typing import Literal,Annotated
class UserInput2(BaseModel):
       age:Annotated[int,Field(...,gt=20,lt=120,description="Enter your age")]
       weight:Annotated[float,Field(...,description='Enter your weight in kgs',examples=['69'])]
       height:Annotated[float,Field(...,description='Enter Your Height in metres',examples=['1.83'])]
       had_abortion:Annotated[int,Field(...,description='If you had abortion:1 and if you didnt then 0',examples=['0'])]
       blood_group:Annotated[Literal['O+','A+','B+','AB+','O-','A-','B-','AB-'],Field(...,description='Input your blood group',examples=['O+'])]
       cycle_type:Annotated[str,Field(...,description=('explain your cyclye type Regular or Irregular'),examples=['Regular'])]
       marriage_years:Annotated[float,Field(...,description="Enter how many years you have been married for ",examples=['1'])]
       pregnant:Annotated[int,Field(...,description='If you were pregnant enter 1 if not then 0',examples=['0'])]
       weight_gain:Annotated[int,Field(...,description='If you experienced weight gain enter 1 if not then 0',examples=['0'])]
       hair_growth:Annotated[int,Field(...,description='If you have proper hair growth enter 1 if not then 0',examples=['0'])]
       skin_darkening:Annotated[int,Field(...,description='If you experienced skin darkening on your body enter 1 if not then 0',examples=['0'])]
       hair_loss:Annotated[int,Field(...,description='If you experienced hair loss enter 1 if not then 0',examples=['0'])]
       pimples:Annotated[int,Field(...,description='If you experienced pimples enter 1 if not then 0',examples=['0'])]
       fast_food:Annotated[float,Field(...,description='If your diet includes fast food on frequent basis enter 1 if not then 0',examples=['0'])]
       regular_exercise:Annotated[int,Field(...,description='If you regularly exercise enter 1 if not then 0',examples=['0'])]
       pulse_rate:Annotated[int,Field(...,description='Enter your pulse rate in BPM',examples=['78'])]
       respiratory_rate:Annotated[int,Field(...,description='Enter your respiratory rate', examples=['44'])]
       hemoglobin: Annotated[float, Field(..., description="Enter Hemoglobin level (g/dL)", examples=["12.5"])]
       fsh: Annotated[float, Field(..., description="Enter FSH level (mIU/mL)", examples=["6.2"])]
       lh: Annotated[float, Field(..., description="Enter LH level (mIU/mL)", examples=["9.1"])]
       waist_hip_ratio: Annotated[float, Field(..., description="Enter Waist to Hip Ratio", examples=["0.85"])]
       tsh: Annotated[float, Field(..., description="Enter TSH level (µIU/mL)", examples=["2.3"])]
       amh: Annotated[float, Field(..., description="Enter AMH level (ng/mL)", examples=["4.5"])]
       prolactin: Annotated[float, Field(..., description="Enter Prolactin level (ng/mL)", examples=["18.2"])]
       vitamin_d3: Annotated[float, Field(..., description="Enter Vitamin D3 level (ng/mL)", examples=["32.0"])]
       progesterone: Annotated[float, Field(..., description="Enter Progesterone level (ng/mL)", examples=["1.5"])]
       random_blood_sugar: Annotated[float, Field(..., description="Enter Random Blood Sugar (mg/dL)", examples=["110"])]
       bp_systolic: Annotated[int, Field(..., description="Enter Systolic Blood Pressure (mmHg)", examples=["120"])]
       bp_diastolic: Annotated[int, Field(..., description="Enter Diastolic Blood Pressure (mmHg)", examples=["80"])]
       avg_follicle_size: Annotated[float, Field(..., description="Enter Average Follicle Size (mm)", examples=["14.5"])]
       total_follicles: Annotated[int, Field(..., description="Enter Total Number of Follicles", examples=["12"])]
       endometrium_thickness: Annotated[float, Field(..., description="Enter Endometrium Thickness (mm)", examples=["8.2"])]


       @computed_field
       @property
       def bmi(self)->float:
             bmi=self.weight/(self.height**2)
             return bmi
       
       @computed_field
       def lh_fsh_ratio(self)->float:
             lh_fsh_ratio=self.lh/self.fsh if self.fsh!=0 else 0.0 #bcoz if fsh = 0, it will crash
             return lh_fsh_ratio
                    
       @field_validator("blood_group",mode='before')
       @classmethod
       def blood_group(cls,value):
             return value.upper()
       
       @field_validator("cycle_type")
       @classmethod
       def cycle(cls,value):
             v=value.strip().title()
             return v
       