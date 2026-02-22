import streamlit as st
import requests 

api_personal="http://127.0.0.1:8000/predict_personal"
api_clinical="http://127.0.0.1:8000/predict_clinical"


st.title(" 🩺 Pcos risk detector")
st.caption("Personal mode uses basic information. Medical mode adds lab/clinical values.")

mode=st.radio("Choose prediction mode",["Personal (no lab reports needed)","Medical (need lab reports)"])
st.sidebar.header("Enter Your details here")


#inout fields
age= st.number_input("Age",min_value=10,max_value=119,value=30)
weight=st.number_input("Weight (Kgs)",min_value=10,max_value=130,value=67)
height=st.number_input("Height (Meters)",min_value=0.30,max_value=2.00,value=1.50)
had_abortion=st.selectbox("Have you had abortion?",options=['Yes','No'])
had_abortion=1 if had_abortion=='Yes' else 0
blood_group=st.selectbox("Blood Group",options=['O+','A+','B+','AB+','O-','A-','B-','AB-'])
cycle_type=st.selectbox("How are your period cycles?",options=['Regular','Irregular'])
marriage_years=st.number_input("How many years you have been married for?",value=0)
pregnant=st.selectbox("Have you ever been pregnant?",options=['Yes','No'])
pregnant=1 if pregnant=='Yes' else 0
weight_gain=st.selectbox("Have you experienced weight gain?",options=['Yes','No'])
weight_gain=1 if weight_gain=='Yes' else 0
hair_growth=st.selectbox("Do you have a normal hair growth?",options=['Yes','No'])
hair_growth=1 if hair_growth=='Yes' else 0
hair_loss=st.selectbox("Are you experiencing hair loss",options=['Yes','No'])
hair_loss=1 if hair_loss=='Yes' else 0
skin_darkening=st.selectbox("Are you experiencing unexplainable skin darkening on any part of you body",options=['Yes','No'])
skin_darkening=1 if skin_darkening=='Yes' else 0
pimples=st.selectbox("Is there any sudden growth of painful pimples",options=['Yes','No'])
pimples=1 if pimples=='Yes' else 0
fast_food=st.selectbox("Is fast food a major part of your daily diet (BE HONESTT YASHUU!!!)",options=['Yes','No'])
fast_food=1 if fast_food=='Yes' else 0
regular_exercise=st.selectbox("Do you exercise regularly?",options=['Yes','No'])
regular_exercise=1 if regular_exercise=='Yes' else 0
pulse_rate=st.number_input("Enter Pulse rate in BPM",value=80)
if mode == "Medical (I have lab reports)":
    respiratory_rate = st.number_input("Respiratory rate (breaths/min)", value=18)

    hemoglobin = st.number_input("Hemoglobin (g/dl)", value=12.5)
    fsh = st.number_input("FSH (mIU/mL)", value=6.2)
    lh = st.number_input("LH (mIU/mL)", value=9.1)

    waist_hip_ratio = st.number_input("Waist-Hip Ratio", value=0.85)
    tsh = st.number_input("TSH (mIU/mL)", value=2.3)
    amh = st.number_input("AMH (ng/mL)", value=4.5)
    prolactin = st.number_input("Prolactin (ng/mL)", value=18.2)
    vitamin_d3 = st.number_input("Vitamin D3 (ng/mL)", value=32.0)
    progesterone = st.number_input("Progesterone (ng/mL)", value=1.5)

    random_blood_sugar = st.number_input("Random Blood Sugar (mg/dl)", value=110.0)

    bp_systolic = st.number_input("BP Systolic (mmHg)", value=120)
    bp_diastolic = st.number_input("BP Diastolic (mmHg)", value=80)

    avg_follicle_size = st.number_input("Average Follicle Size", value=14.5)
    total_follicles = st.number_input("Total Follicles", value=12)
    endometrium_thickness = st.number_input("Endometrium Thickness (mm)", value=8.2)

if st.button("Predict Pcos risk"):
    input_data={'age':age,
                'weight':weight,
                'height':height,
                'had_abortion':had_abortion, 
                'blood_group':blood_group,
                'cycle_type':cycle_type,
                'marriage_years':marriage_years,
                'pregnant':pregnant,
                'weight_gain':weight_gain,
                'hair_growth':hair_growth,
                'skin_darkening':skin_darkening,
                'hair_loss':hair_loss,
                'pimples':pimples,
                'fast_food':fast_food,
                'regular_exercise':regular_exercise, 
                'pulse_rate':pulse_rate
                }
    if mode == "Medical (I have lab reports)":
        api_url = api_clinical
        input_data.update({
            "respiratory_rate": respiratory_rate,
            "hemoglobin": hemoglobin,
            "fsh": fsh,
            "lh": lh,
            "waist_hip_ratio": waist_hip_ratio,
            "tsh": tsh,
            "amh": amh,
            "prolactin": prolactin,
            "vitamin_d3": vitamin_d3,
            "progesterone": progesterone,
            "random_blood_sugar": random_blood_sugar,
            "bp_systolic": bp_systolic,
            "bp_diastolic": bp_diastolic,
            "avg_follicle_size": avg_follicle_size,
            "total_follicles": total_follicles,
            "endometrium_thickness": endometrium_thickness
        })
    else:
        api_url = api_personal
    try:
        response = requests.post(api_url, json=input_data, timeout=10)

        response.raise_for_status()   # forces HTTP errors to throw

        result = response.json()
        st.success(f"PCOS probability: {round(result['probability']*100,2)}%")

    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to FastAPI. Is uvicorn running on port 8000?")
    except requests.exceptions.Timeout:
        st.error("⏳ Request timed out. FastAPI might be stuck.")
    except requests.exceptions.HTTPError as e:
        st.error(f"❌ HTTP error: {e}")
    except Exception as e:
        st.error(f"❌ Unexpected error: {e}")
