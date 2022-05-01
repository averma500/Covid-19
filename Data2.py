import streamlit as st
import numpy as np
import pandas as pd

def app():
    with st.container():
        st.title("Upload your CSV file here")
    with st.container():
        st.write("---")

    with st.container():
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write(df)
    with st.container():
        st.write("---")