import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import time
import homepage #Custom class which handles homepage data
import univariateAnalysis #Customer class for univariate analysis
import warnings
warnings.filterwarnings("ignore", category= UserWarning, module= "matplotlib")


homePageObj = homepage.HomePage() #An instance of HomePage Class inside homepage module
univariateObj = univariateAnalysis.Univariate() #Instance of Univariate class

sns.set_theme(style= "whitegrid") #Set theme for graphs

#Navigation Bar Properties
sidebarCol1, sidebarCol2 = st.sidebar.columns([.7,.3], vertical_alignment="center") # 70% and 30% width
with sidebarCol1:
    st.title("Page Options")

with sidebarCol2:
    theme = st.checkbox(label=":material/nightlife:", key= "theme")
    if theme:
        st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #121212;
        color: #E0E0E0;
    }

    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #1E1E1E;
        color: #E0E0E0;
    }

    /* Sidebar text */
    section[data-testid="stSidebar"] * {
        color: #E0E0E0 !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
    }

    /* Streamlit widgets (labels, radio, selectbox etc.) */
    label, .stText, .stSelectbox, .stRadio, .stCheckbox {
        color: #E0E0E0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

#SideBar Page Selection Pannel
page = st.sidebar.selectbox(
    label= "Select Page", 
    options= ["Home Page", "Univariate Analysis", "Bi-Variate Analysis", "MultiVariate Analysis"], 
    index= 1, 
    key= "navigationSelectBox",
    help= """
    **Navigate through different pages**

    Select an option
    """
    )

#Page Properties
if page == "Home Page":

    #Load HomePage Navigation Content
    homePageObj.homePageNavigation()

    #Load HomePage Body Content
    homePageObj.homePageBody()
elif page == "Univariate Analysis":

    #Load Univariate Navigation Content
    filter = univariateObj.univariateFilters()

    #Load Univariate Body Content
    univariateObj.univariateBody()
    if not filter:
        st.info("Toggle Filter Options to Display Graph !", icon="ℹ️")

    #Display graphs based on checkbox
    if filter == "Histogram":
        univariateObj.histogram_display()
        
    

