from home_page import show_home_page
from predict_page import predict_class
from streamlit_option_menu import option_menu
from PIL import Image
import streamlit as st

img = Image.open("cancer_logo.jpg")
page_config = {"page_title": "Personalised Cancer Diagnosis", "page_icon": img, "layout": "centered"}
st.set_page_config(**page_config)

page = option_menu(
    menu_title=None,
    options=["Home", "Predict", "Code"],
    icons=["house-fill", "motherboard", "file-earmark-code"],
    default_index=0,
    orientation="horizontal",
    styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "15px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "red"}
            }
)

# Home page
if page == "Home":
    show_home_page()

# Prediction page
if page == "Predict":

    st.text("")
    st.text("")
    st.markdown("""**This Machine Learning application allows you to classify a given genetic mutation/variation and
                     it's clinical literature into one of the 9 classes.**
                """)
    st.markdown("**The model returns the probability of a data-point belonging to each of the 9 classes.**")
    st.text("")
    st.markdown("Please enter the details of the Genetic Mutation:")

    # User input
    gene = st.text_input('Enter Gene:', '')
    variation = st.text_input('Enter Variation:', '')
    text = st.text_area('Enter Clinical Literature:', '')
    no_features = st.slider('Select Top features:', 100, 500, 100)

    if st.button("Predict"):
        predict_class(gene, variation, text, no_features)

# Code page
if page == "Code":

    st.text("")
    st.write("###### If you are more interested in the code you can directly jump into these repositories :")
    st.text("")
    st.caption("**DEPLOYMENT** : [link](https://github.com/sangoleshubham20/CancerDiagnosis_deployment)")
    st.caption("**MODELLING** : [link](https://github.com/sangoleshubham20/PersonalisedCancerDiagnosis_ModellingCode)")
