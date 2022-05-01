import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots
from datetime import datetime

def app():
    # ---- HEADER ---- #
    with st.container():
        st.header('Covid-19 Data Visualization India')
    with st.container():
        st.write("---")

    # ---> Load DataFrame <---
    with st.container():
        csv_file = 'D:\\W O R K S\\P R O J E C T S\\P Y T H O N\\Corona Report\\covid_dataset\\complete.csv'

        file = pd.read_csv(csv_file)
        st.multiselect(
        'Select the State :',
        (file['State']))

        st.warning("All Graph and Data is only for Confirm Case.")

    # ---- DataFrame ---- #
    with st.container():

        left_column, right_column = st.columns(2)

        with left_column:
            
            dict2 = {'State': file['State'],
                    'ConfirmCase': file['Confirm_Case']}

            st.header("Bar Graph of Covid-19, All State of India.")
            
            df2 = pd.DataFrame(dict2)
            fig = px.bar(        
                    df2,
                    x = "State",
                    y = "ConfirmCase"
                )
            st.plotly_chart(fig)

        with right_column:

            df = pd.DataFrame(dict(
            State = file['State'],
            ConfirmCase = file['Confirm_Case']
            ))

            st.header("Line Chart of Covid-19, All State of India.")
            fig2 = px.line(        
                df, #Data Frame
                x = "State", #Columns from the data frame
                y = "ConfirmCase",
            )
            fig2.update_traces(line_color = "red")
            st.plotly_chart(fig2)

    with st.container():

        left_column, right_column = st.columns(2)

        with left_column:
            state = file['State'] 
            total_case = file['Confirm_Case']

            fig = go.Figure(
            go.Pie(labels = state, values = total_case, hoverinfo = "label + percent", textinfo = "value"))

            st.header("Pie chart of Covid-19, All State of India.")
            st.plotly_chart(fig) 

        with right_column:
            st.write("")  

    






