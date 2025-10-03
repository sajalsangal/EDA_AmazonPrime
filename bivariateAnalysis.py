import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

class Bivariate:

    def __init__(self):
        self.__data = pd.read_csv("merged_dataset.csv")

    def __display_graph(self, fig):
        st.plotly_chart(fig, use_container_width= True)

    def bivariateFilters(self):

        filter_option = st.sidebar.radio(
            label= "**Filters**",
            options= ["Line Plot", "Bar Plot", "Bubble Chart", "Violin Plot", "TreeMap"],
            key= "filterBivariate",
            help= "Choose to display graph 📈",
            index= None
        )

        return filter_option
    
    def bivariateBody(self):
        st.title("Bi-Variate Analysis")
        st.write(
            f"""
            **Important KPI's :** `release year vs runtime`,`release year vs tmdb_popularity` , 
            `runtime vs age_certification`, `imdb score vs age_certification`, `release_year vs age_certification`,
            `imdb_votes vs age_certification`, `tmdb_popularity vs age_certification`, `tmdb_score vs age_certification`,
            `imdb_score vs tmdb_popularity`

            ---
            """
        )
