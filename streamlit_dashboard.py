import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
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

#Home Page Properties
if page == "Home Page":

    #HomePage Navigation Settings
    st.sidebar.write(
        """
            **Welcome to my streamlit app**

            *Here we will take a look at Amazon Prime Dataset
            and vitualize it through interactive graphs, watch the video to
            get a better understanding of the code.*

            **Github Project** 🔗 : [Link](https://github.com/sajalsangal/EDA_AmazonPrime "sajalsangal/EDA_AmazonPrime")
        """
    )

    #SideBar columns to display file download buttons
    st.sidebar.subheader("Download Resources")
    #Columns for titles dataset
    titleCol1, titleCol2 = st.sidebar.columns(2, vertical_alignment="center")
    with titleCol1:
        st.write("*Titles Dataset:*")

    with titleCol2:
        titleData = pd.read_csv("titles.csv")
        titleCSV = titleData.to_csv().encode("utf-8")

        if st.download_button(
            label=":material/download:",
            data= titleCSV,
            file_name= "titles.csv",
            mime= "text/csv",
            key= "downloadTitlesCSV",
            
        ):
            st.sidebar.success("Done!", icon= "✅")

    #Columns for credit dataset
    creditCol1, creditCol2 = st.sidebar.columns(2, vertical_alignment="center")
    with creditCol1:
        st.write("*Credit Dataset:*")

    with creditCol2:
        creditsData = pd.read_csv("credits.csv")
        creditsCSV = creditsData.to_csv().encode("utf-8")

        if st.download_button(
            label= ":material/download:",
            data= creditsCSV,
            file_name= "credits.csv",
            mime= "text/csv",
            key= "creditsDatasetCSV",
            
        ):
            st.sidebar.success("Done!", icon= "✅")
    
    #Copyright Info
    st.sidebar.write("> *Project By*: @sajalsangal")
    st.title("Home Page")
