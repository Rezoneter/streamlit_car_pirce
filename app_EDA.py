import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


def run_EDA_app():
    st.subheader('Analyzing Data')

    st.text('Check all data')
    df = pd.read_csv('./data/Car_Purchasing_Data.csv')

    st.dataframe(df)

    st.text('Check Basic statics data')
    if st.checkbox('Statics Data'):
        st.dataframe(df.describe())
    else:
        st.text('')
    
    st.text('Max / Min data Chaek')
    column_list = df.columns[4:]

    selected_column = st.selectbox('Select columns', column_list)

    st.text(selected_column +' _Minimum value')
    st.dataframe(df.loc[df[selected_column] == df[selected_column].max(),])
    st.text(selected_column +' _Maximum value')
    st.dataframe(df.loc[df[selected_column] == df[selected_column].min(),])

    st.text(selected_column +' _Histogram')
    fig1 = plt.figure()
    df[selected_column].hist(bins =20)
    st.pyplot(fig1)