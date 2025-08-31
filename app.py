import streamlit as st
import pickle
import numpy as np

with open('model.pkl','rb') as fp:
  model=pickle.load(fp)

with open('encoder.pkl','rb') as fp:
  encoder=pickle.load(fp)

st.title('Obesity Prediction')
age=st.number_input('Enter age: ')
gender=st.selectbox('Select gender: ',['Male','Female'])
height=st.number_input('Enter height (cm): ')
weight=st.number_input('Enter weight (kg): ')
bmi=st.number_input('Enter BMI value: ')
physical=st.number_input('Enter physical activity level: ')
button=st.button('Predict')

if button:
  gender=encoder['Gender'].transform([gender])[0]
  features=np.array([[age,gender,height,weight,bmi,physical]])
  prediction=model.predict(features)[0]
  prediction_label=encoder['ObesityCategory'].inverse_transform([prediction])[0]
  st.text(f'Your obesity category: {prediction_label}',)