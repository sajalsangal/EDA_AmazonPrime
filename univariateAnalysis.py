import streamlit as st
import pandas as pd
import plotly.express as px

class Univariate:
    def __init__(self):
        self.__data = pd.read_csv("merged_dataset.csv")

    def __display_graph(self, fig):
        st.plotly_chart(fig, use_container_width= True)

    def univariateFilters(self):
        #st.sidebar.header("Filter", help= "Choose to display graph")

        self.filter_option = st.sidebar.radio(
            label= "**Filters**",
            options= ["Histogram", "Box Plot", "Count Plot", "Pie Plot"],
            key= "filterUnivariate",
            help= "Choose to display graph 📈",
            index= None
        )

        return self.filter_option
    
    def univariateBody(self):
        st.title("Univariate Analysis")
        st.write(
            f"""
            **Univariate analysis** is the study of a single variable in a dataset to understand its distribution,
            central tendency, and variability. It helps identify patterns, outliers, and data quality issues, 
            often using summary statistics, histograms, bar charts, or boxplots. This forms the foundation for 
            deeper analysis before exploring relationships between multiple variables.

            **Important KPI's :** `release year`, `runtime`, `imdb_score`, `tmdb_score`, `genre`, `production_counties`, `type`,
            `age_certification`, `role`, `name`, `character`, `imdb_votes`, `tmdb_popularity`
            
            ---
            """
        )
    
    def histogram_display(self):
        st.header("Histogram")

        fig = px.histogram(self.__data, x= "release_year")
        # Slider for number of bins
        num_bins = st.slider("Select number of bins:", min_value=5, max_value=50, value=20)

        # Calculate bin width
        min_val = self.__data["release_year"].min()
        max_val = self.__data["release_year"].max()
        bin_width = (max_val - min_val) / num_bins

        fig.update_traces(
            xbins=dict(size=bin_width),
            marker_color="teal",
            opacity= 0.7,
            marker_line_color = "black",
            marker_line_width = 1,
            hovertemplate="Year: %{x}<br>Count: %{y}<extra></extra>"

        )
        fig.update_layout(
            title_font_size=22,
            title= "Distribution of Movies with Release Year",
            hovermode="x unified" 
        )

        fig.update_xaxes(title= "Release Year")
        fig.update_yaxes(title= "Count Of Movies")
        

        self.__display_graph(fig)

        


        

        #self.__display_graph(fig_axes)


        
