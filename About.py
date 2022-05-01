import streamlit as st

def app():
    with st.container():
        st.title("About Covid-19 Research")
    with st.container():
        st.write("---")
    with st.container():
        st.info("Analysis and Evaluation of COVID-19 Web Applications for Health Professionals: Challenges and Opportunities")
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("""The multidisciplinary nature of the work required for studies within the 
            COVID-19 pandemic has created new demanding situations for health experts within the warfare against the virus. 
            They need daily be prepared with novel gear, packages, and resources—which have emerged at some stage in the 
            pandemic—everyday gain get right of entry to everyday leap forward findings; recognize the modern day tendencies; 
            and day-to-day deal with their unique wishes for speedy records acquisition, analysis, evaluation, and reporting. 
            Because of the complicated nature of the virus, healthcare structures international are severely impacted as the 
            remedy and the vaccine for COVID-19 disease are not but observed. This leads to frequent modifications in regulations 
            and regulations by using governments and worldwide organizations. Our analysis suggests that given the abundance of facts assets, 
            locating the maximum suitable application for evaluation, evaluation, or reporting, is considered one of such demanding situations. 
            but, fitness experts and coverage-makers need get admission to everyday the maximum applicable, dependable, trusted, 
            and every day records and applications that may be used in their tasks of COVID-19 
            research and analysis. In this newsletter, we gift our evaluation of diverse novel and crucial web-daily """) 
        with right_column:
            st.write("""programs 
            which have been specifically evolved for the duration of the COVID-19 pandemic and that can be utilized by the 
            health experts network every day help in advancing their analysis and studies. these applications contain seek 
            portals and their associated information reposievery dayries for literature and scientific trials, statistics 
            resources, tracking dashboards, and forecasting fashions. We gift a listing of the minimally critical on-line, 
            internet-based applications daily serve a large number of functions, from hundreds of those developed in view that 
            the start of the pandemic. A crucial analysis is furnished for the selected packages primarily based on 17 features 
            that can be useful for researchers and analysts for their reviews. these features make up our assessment framework 
            and feature not been used previously for analysis and evaluation. consequently, expertise of these programs will now 
            not only boom productivity however can even allow us daily discover new dimensions for the usage of current applications 
            with more manage, higher control, and extra final results in their research. further, the features used in our framework 
            can be implemented for future opinions of similar packages and fitness professionals can adapt them for assessment of 
            different programs now not included on this analysis.""")
    with st.container():
        st.write("---")
    
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.title("Our Crew")
            st.write("Aman Verma")
            st.write("Nepal") 
            st.write("+91-620524041")         


        with col2:
            st.title("Details")
            st.write("Rk University")
            st.write("4CEB")
            st.write("Python Programming II")
        with col3:
            st.text_input("Name :")
            st.text_input("Email :")
            st.slider("Age :", min_value = 10, max_value = 100)
            st.button("Submit")