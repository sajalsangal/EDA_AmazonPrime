import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

class MultiVariate:
    def __init__(self):
        self.__data = pd.read_csv("merged_dataset.csv")

    def __display_graph(self, fig):
        st.plotly_chart(fig, use_container_width= True)

    def multivariateFilters(self):
    
        filter_option = st.sidebar.radio(
            label= "**Filters**",
            options= ["Heatmap", "Pair Plot"],
            key= "filterMultivariate",
            help= "Choose to display graph 📈",
            index= None
        )

        return filter_option
    
    def multivariateBody(self):
        st.title("Multi-Variate Analysis")
        st.write(
            f"""
            **Important KPI's :** `Correlation Coefficient` , `Pair Wise Analysis`
            
            ---
            """
        )

    
