# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:24:37 2023

@author: Adarsh
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

heart_model = pickle.load(open('heart_model.sav','rb'))

with st.sidebar:
    selected = option_menu('Disease prediction using ML by /\|]/\ r $#',
                           ['HEART DISEASE'],
                           icons = ['activity'],
                           default_index=0)
                               
    
if(selected=='HEART DISEASE'):
    st.title('HEART DISEASE PREDICTION USING ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        age = float(age) if age else 0.0 
        
    with col2:
        sex = st.text_input('Sex, MALE=1,FEMALE=0')
        sex = float(sex) if sex else 0.0 
        
    with col3:
        cp = st.text_input('Chest Pain types')
        cp = float(cp) if cp else 0.0 
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        trestbps = float(trestbps) if trestbps else 0.0 
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        chol = float(chol) if chol else 0.0 
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        fbs = float(fbs) if fbs else 0.0 
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        restecg = float(restecg) if restecg else 0.0 
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        thalach = float(thalach) if thalach else 0.0 
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        exang = float(exang) if exang else 0.0 
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        oldpeak = float(oldpeak) if oldpeak else 0.0 
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        slope = float(slope) if slope else 0.0 
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        ca = float(ca) if ca else 0.0 
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        thal = float(thal) if thal else 0.0 
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)