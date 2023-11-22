import streamlit as st
import joblib
import numpy as np



def run_ML_app():
    st.subheader('Purchase price predict')

    # learning file read,
    # develope predict screen

    regressor = joblib.load('./model/regressor.pkl')

    gender = st.radio('Select sex',['Female', 'Male'])

    if gender == 'Female':
        gender = 0
    else :
        gender = 1 

    age = st.number_input('Input Age', 20, 100)

    salary = st.number_input ('Input Salary', 10000, 1000000)

    debt = st.number_input('Input Card debt', 0, 100000)

    worth = st.number_input('Input Worth', 1000, 1000000)

    if st.button('Predict purcahse price'):
        selected_data = np.array([gender, age, salary, debt, worth])
        shape_data = selected_data.reshape(1,5)
        y_pred = regressor.predict(shape_data)
        st.text(y_pred)
    else:
        pass
    