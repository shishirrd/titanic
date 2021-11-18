#!/usr/bin/env python
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import streamlit as st
import pickle

# In[2]:

def load_model():
    with open ('saved_steps_Titanic_DT.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

# In[3]:

data = load_model()

# In[4]:

loaded_model = data["model"]
le_sex = data['le_sex']
le_age = data['le_age']
le_pclass = data['le_pclass']

# In[5]:

def show_predict_page():
    st.title("Did this person survive the sinking of the Titanic?")
    
    st.write("""### We need some information to predict this!""")

show_predict_page()

gender = (
    'male','female')

age = ('<10','10-20','20-30', '30-40', 
'40-50','50-75', '>75'
    )
pclass = (
    '1st Class', '2nd Class', '3rd Class'
    )

# In[6]:

Gender = st.selectbox("Passenger's gender", gender)
Age = st.selectbox("Passenger's age group in years", age)
Passenger_class = st.selectbox("Passenger's seating class", pclass)

# In[7]:

OK = st.button("Predict")
if OK:
    X = np.array([[Gender,Age,Passenger_class]])
    X[:, 0] = le_sex.transform(X[:, 0])
    X[:, 1] = le_age.transform(X[:, 1])
    X[:, 2] = le_pclass.transform(X[:, 2])
    X = X.astype(float)
    
    prediction = loaded_model.predict(X)
    
    if prediction == 0:
        st.subheader("The passenger may not have survived :(.")
    else:
        st.subheader("Looks like the passenger may have survived!")
