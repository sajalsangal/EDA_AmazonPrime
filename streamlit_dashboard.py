import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
import time
import homepage #Custom class which handles homepage data
import warnings
warnings.filterwarnings("ignore", category= UserWarning, module= "matplotlib")


sns.set_theme(style= "whitegrid") #Set theme for graphs

#Navigation Bar Properties
st.sidebar.title("Page Options")
page = st.sidebar.selectbox(
    label= "Select Page", 
    options= ["Home Page", "Univariate Analysis", "Bi-Variate Analysis", "MultiVariate Analysis"], 
    index= 0, 
    key= "navigationSelectBox",
    help= """
    **Navigate through different pages**

    Select an option
    """
    )

homePageObj = homepage.HomePage() #An instance of HomePage Class inside homepage module

#Home Page Properties
if page == "Home Page":

    #Load HomePage Navigation Content
    homePageObj.homePageNavigation()

    #Load HomePage Body Content
    homePageObj.homePageBody()
        
    

