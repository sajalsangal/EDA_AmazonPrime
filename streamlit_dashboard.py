import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import time
import homepage #Custom class which handles homepage data
import univariateAnalysis #Custom class for univariate analysis
import bivariateAnalysis #Custom class for bivariate analysis
import multivariateAnalysis #Customer class for multivariate analysis
import warnings
warnings.filterwarnings("ignore", category= UserWarning, module= "matplotlib")


homePageObj = homepage.HomePage() #An instance of HomePage Class inside homepage module
univariateObj = univariateAnalysis.Univariate() #Instance of Univariate class
bivariateObj = bivariateAnalysis.Bivariate() #Instance of Bivariate class
multivariateObj = multivariateAnalysis.MultiVariate()

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
    index= 3, 
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
    elif filter == "Box Plot":
        univariateObj.boxplot_display()
    elif filter == "Count Plot":
        univariateObj.countplot_display()
    elif filter == "Donut Plot":
        univariateObj.pieplot_display()

elif page == "Bi-Variate Analysis":
    
    filter = bivariateObj.bivariateFilters()

    #Display heading for bivariate analysis
    bivariateObj.bivariateBody()
    if not filter:
        st.info("Toggle Filter Options to Display Graph !", icon="ℹ️")

    if filter == "Line Plot":
        bivariateObj.linePlot()
    elif filter == "Bar Plot":
        bivariateObj.barplot()
    elif filter == "Violin Plot":
        bivariateObj.violinPlot()
    elif filter == "Bubble Chart":
        bivariateObj.bubblechart()
    elif filter == "TreeMap":
        bivariateObj.treemap()

elif page == "MultiVariate Analysis":
    filter = multivariateObj.multivariateFilters()

    multivariateObj.multivariateBody()
    if not filter:
        st.info("Toggle Filter Options to Display Graph", icon= "ℹ️")

    if filter == "Heatmap":
        multivariateObj.heatmap()

    
        
    

