import streamlit as st
from PIL import Image
import base64

def app():
    # ---- HEADER SECTION ---- #
    with st.container():
        st.title("Novel Corona Virus Information")

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("""Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.""")
            st.write("""Most people infected with the virus will experience mild to moderate respiratory 
            illness and recover without requiring special treatment. However, some will become seriously ill and require medical attention. 
            Older people and those with underlying medical conditions like cardiovascular disease, diabetes, chronic respiratory disease, 
            or cancer are more likely to develop serious illness. Anyone can get sick with COVID-19 and become seriously ill or die at any age.""")
        with right_column:
            # """### gif from local file"""
            image2 = 'D:\\W O R K S\\P R O J E C T S\\P Y T H O N\\Corona Report\\Image\\gif\\cvirus.gif'
            file_ = open(image2, "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.markdown(
                f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
                unsafe_allow_html=True,
            )
    with st.container():
        st.write("---")

    
    # --- SYMPTOMS --- #
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown("## Symptoms")
            st.markdown(("* Fever\n"
            "* Cough\n"
            "* SHortness of breath of difficulty breathing\n"
            "* Headache\n"
            "* Loss of taste or smell\n"
            "* Sore throat\n"
            "* Congestion or runny nose\n"
            "* Nausea or vomiting\n"
            "* Diarrhea"))
        with right_column:
            image = Image.open('D:\\W O R K S\\P R O J E C T S\\P Y T H O N\\Corona Report\Image\\covid.png')
            st.image(image, width=400,  caption='')

    with st.container():
        st.write("---")

    # ---- Precuation ---- #
    with st.container():
        st.header("Precautions of Novel Corona Virus")
        st.write("""Protect yourself and others around you by knowing the facts and taking appropriate precautions. 
        Follow advice provided by your local health authority.""")

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:    
            st.write("""To prevent the spread of COVID-19:""")
            st.markdown(("* Maintain a safe distance from others (at least 1 metre), even if they don’t appear to be sick.\n"
            "* Wear a mask in public, especially indoors or when physical distancing is not possible.\n"
            "* Choose open, well-ventilated spaces over closed ones. Open a window if indoors.\n"
            "* Clean your hands often. Use soap and water, or an alcohol-based hand rub.\n"
            "* Get vaccinated when it’s your turn. Follow local guidance about vaccination.\n"
            "* Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.\n"
            "* Stay home if you feel unwell."))
        with right_column:
            # """### gif from local file"""
            image3 = 'D:\\W O R K S\\P R O J E C T S\\P Y T H O N\\Corona Report\\Image\\gif\\hand.gif'
            file_gif = open(image3, "rb")
            contents1 = file_gif.read()
            data_url1 = base64.b64encode(contents1).decode("utf-8")
            file_gif.close()

            st.markdown(
                f'<img src="data:image/gif;base64,{data_url1}" alt="cat gif">',
                unsafe_allow_html=True,
            )
    with st.container():
        st.write("---")

    with st.container():
        st.write("""If you have a fever, cough and difficulty breathing, seek medical attention. Call in advance 
        so your healthcare provider can direct you to the right health facility. This protects you, and prevents 
        the spread of viruses and other infections.""")

        url = "https://www.mohfw.gov.in/"
        st.write("""If you want more information regarding Novel Corona Virus. Visit Ministry of Health and 
        Welfare (Government of India) site. Please [Click Here](%s)""" % url)