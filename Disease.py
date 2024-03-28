import pandas as pd 
import joblib
import warnings
warnings.filterwarnings('ignore')
import streamlit as st


st.markdown("<h1 style = 'color: #D71313; text-align: center; font-family: Courier'>Kidney disease Predictor</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #D71313; text-align: center; font-family: Courier '>Built by Adebayo </h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html= True)


st.sidebar.image('pngwing.com (13).png', caption = 'WELCOME USER >_<')

st.image('pngwing.com (10).png')

st.markdown("<br>", unsafe_allow_html = True)

st.header('Project Info', divider= True)
st.write("This machine learning program predicts the probability of an individual having heart disease based on a scset of medical parameters, with the goal of assisting healthcare professionals in diagnosing and treating patients more effectively through early identification and risk assessment.")

st.markdown("<br>", unsafe_allow_html = True)

sel = ['age', 'hemoglobin', 'blood urea', 'blood glucose random', 'serum creatinine', 'sodium', 'white blood cell count', 'packed cell volume', 'classes']

ds = pd.read_csv('kidney_disease (1).csv')
ds.rename(columns={'bp': 'blood_pressure', 'sg': 'specific gravity','al':'albumin','su':'sugar','rbc':'red blood cells',
                     'pc':'pus cell','pcc':'pus cell clumps','ba':'bacteria','bgr':'blood glucose random','bu':'blood urea',
                     'sc':'serum creatinine','sod':'sodium','pot':'potassium','hemo':'hemoglobin','pcv':'packed cell volume',
                     'wc':'white blood cell count','rc':'red blood cell count','htn':'hypertension','dm':'diabetes mellitus',
                     'cad':'coronary artery disease','appet':'appetite','pe':'pedal edema','ane':'anemia','classification':'classes'},inplace=True)

st.dataframe(ds)
ds['white blood cell count'] = pd.to_numeric(ds['white blood cell count'], errors = 'coerce')
ds['packed cell volume'] = pd.to_numeric(ds['packed cell volume'], errors = 'coerce')

st.sidebar.markdown("<br>", unsafe_allow_html = True)
st.sidebar.markdown("<br>", unsafe_allow_html = True)

st.sidebar.subheader('Input your Variables')

age = st.sidebar.number_input('Age', 16,90)
hem = st.sidebar.number_input('Hemoglobin', ds['hemoglobin'].min(), ds['hemoglobin'].max())
bu = st.sidebar.number_input('Blood urea', ds['blood urea'].min(), ds['blood urea'].max())
bgu = st.sidebar.number_input('Blood glucose random', ds['blood glucose random'].min(), ds['blood glucose random'].max())
sc = st.sidebar.number_input('Serum creatinine', ds['serum creatinine'].min(), ds['serum creatinine'].max())
sd = st.sidebar.number_input('Sodium', ds['sodium'].min(), ds['sodium'].max())
wc = st.sidebar.number_input('White blood cell count', ds['white blood cell count'].min(), ds['white blood cell count'].max())
pcv = st.sidebar.number_input('packed cell volume', ds['packed cell volume'].min(), ds['packed cell volume'].max())


input_var = pd.DataFrame()
input_var['age'] = [age]
input_var['hemoglobin'] = [hem]
input_var['blood urea'] = [bu]
input_var['blood glucose random'] = [bgu]
input_var['serum creatinine'] = [sc]
input_var['sodium'] = [sd]
input_var['white blood cell count'] = [wc]
input_var['packed cell volume'] = [pcv]


st.markdown("<br>", unsafe_allow_html= True)
# display the users input variable 
st.subheader('Users Input Variables')
st.dataframe(input_var)


model = joblib.load('Kidney_prediModel.pkl')
predicted = model.predict(input_var)

st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)

if st.button('Predict Staus'):
    if predicted == 0:
        st.error('Sorry to break it to you, You might have a kidney disease')
        st.image('pngwing.com (14).png')
    else:
        st.success('You do not have a kidney disease')
        st.balloons()

