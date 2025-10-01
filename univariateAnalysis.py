import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class Univariate:
    def __init__(self):
        self.__data = pd.read_csv("merged_dataset.csv")

    def univariateNavigation(self):
        st.sidebar.header("Filter", help= "Select checkbox to display graph")
