import streamlit as st

def run_home_app():
    st.subheader('Welcome')
    st.text('This application is info of customers and purchase of car data')
    st.text('If you enter cuntomer info, predict the car price')

    st.text('This application is batch to AWS')
    
    img_url = 'https://i.namu.wiki/i/GoDVTVuVcwHAYGcfhH5KqqOufFI0qRU74zL5pk74rWV-visTlr5PlullVzh4HvqyJ02T4T5ArxMfyr17b-SItQ.webp'

    st.image(img_url)