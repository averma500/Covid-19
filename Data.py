import streamlit as st
import numpy as np
import pandas as pd

def app():
    with st.container():
        st.title('Covid-19 Data of India')
    with st.container():
        st.write("---")
    with st.container():
        df = pd.read_csv('D:\\W O R K S\\P R O J E C T S\\P Y T H O N\\Corona Report\\covid_dataset\\complete.csv')
        st.write(df)

        st.write("""This is Covid-19 Data. This data is only belongs to India.""")
