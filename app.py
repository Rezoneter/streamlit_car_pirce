import streamlit as st
from app_home import run_home_app
from app_EDA import run_EDA_app
from app_ML import run_ML_app

def main():
    st.title('-Car price predict Dashboard- ')
    menu = ['home', 'EDA', 'ML']

    choice = st.sidebar.selectbox('Select Menu', menu)

    if choice == menu[0]:
        run_home_app()
    elif choice == menu[1]:
        run_EDA_app()
    elif choice == menu[2]:
        run_ML_app()





if __name__ == '__main__':
    main()