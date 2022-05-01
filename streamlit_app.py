import streamlit as st
import Home, Data, Data2, Dashboard, About
# import streamlit.components.v1 as components

st.set_page_config(page_title= 'Covid-19 India', page_icon = ":rocket:", layout = "wide")


pages = {
    "Home": Home,
    "Dashboard": Dashboard,
    "Data": Data,
    "Your Data": Data2,
    "About": About
    
}

st.sidebar.title('Menu')
selection = st.sidebar.radio("", list(pages.keys()))
page = pages[selection]
page.app()
st.sidebar.write("---")
st.sidebar.info("""This is web- application will serve to analyze, visualize, the spread of the novel coronavirus 2019""")

st.sidebar.info("Create by Aman Verma.")

st.sidebar.write("---")

st.sidebar.header("Contact Form")
with st.sidebar.form("form1", clear_on_submit=True):
    name = st.text_input("Name :")
    email = st.text_input("Email :")
    message = st.text_area("Message :")
    age = st.slider("Age :", min_value = 10, max_value = 100)
    st.write(age)
    submit = st.form_submit_button("Submit")

