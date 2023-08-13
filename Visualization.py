import numpy as np 
import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt 

st.set_page_config(
    page_title='Turbine Performance Predictor',
    page_icon='🌀'
)

st.title('Data Visualization')

data = pd.read_csv('data//turbine.csv')

parameters_1 = ['Active Power','Wind Direction']
parameters_2 = ['Wind Speed', 'Theoretical Power Curve']
firstparameter = st.sidebar.selectbox('Choose Parameter', parameters_1,  index=0)
secondparameter = st.sidebar.selectbox('Choose Parameter', parameters_2, index=0)

if firstparameter == parameters_1[0]:
    if secondparameter == parameters_2[0]:
        fig, ax = plt.subplots(1,1)
        ax.scatter(data['Wind Speed (m/s)'], data['LV ActivePower (kW)'])
        ax.set_title('Active Power vs Wind Speed')
        ax.set_xlabel('Wind Speed (m/s)')
        ax.set_ylabel('Active Power (KW)')
        st.pyplot(fig)
if firstparameter == parameters_1[1]:
    if secondparameter == parameters_2[0]:
        fig, ax = plt.subplots(1,1)
        ax.scatter(data['Wind Direction (°)'], data['Wind Speed (m/s)'])
        ax.set_title('Wind Speed vs Wind Direction')
        ax.set_xlabel('Wind Direction (°)')
        ax.set_ylabel('Wind Speed (m/s)')
        st.pyplot(fig)
if firstparameter == parameters_1[0]:
    if secondparameter == parameters_2[1]:
        fig, ax = plt.subplots(1,1)
        ax.scatter(data['Theoretical_Power_Curve (KWh)'], data['LV ActivePower (kW)'])
        ax.set_title('Active Power vs Theoretical Power')
        ax.set_xlabel('Theoretical Power (KWh)')
        ax.set_ylabel('Active Power (KW)')
        st.pyplot(fig)
if firstparameter == parameters_1[1]:
    if secondparameter == parameters_2[1]:
        fig, ax = plt.subplots(1,1)
        ax.scatter(data['Wind Direction (°)'], data['Theoretical_Power_Curve (KWh)'])
        ax.set_title('Theoretical Power vs Wind Direction')
        ax.set_xlabel('Wind Direction (°)')
        ax.set_ylabel('Theoretical Power (KWh)')
        st.pyplot(fig)









