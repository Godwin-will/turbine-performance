import numpy as np 
import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

st.set_page_config(
    page_title='Turbine Performance Predictor',
    page_icon='🌀'
)

st.title('Predict Wind Turbine Performance')

data = pd.read_csv('data//turbine.csv')
X = data[['Wind Speed (m/s)', 'Theoretical_Power_Curve (KWh)', 'Wind Direction (°)']]
Y = data['LV ActivePower (kW)']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.23)

#Model
model = LinearRegression()
model.fit(X_train, Y_train)

speed = st.number_input('Wind Speed')
direction = st.number_input('Wind Direction')
curve = st.number_input('Theoretical Power')
prediction = model.predict([[speed, curve, direction]])

if st.button('Predict'):
    st.success(f'The predicted energy output of the wind turbine is {prediction} KW')    