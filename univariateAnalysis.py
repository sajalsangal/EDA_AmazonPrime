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

        filter_option = st.sidebar.radio(
            label= "**Filters**",
            options= ["Histogram", "Box Plot", "Count Plot", "Pie Plot"],
            key= "filterUnivariate",
            help= "Choose to display graph 📈",
            index= None
        )

        return filter_option
    
    def univariateBody(self):
        st.title("Univariate Analysis")
        st.write(
            f"""
            **Important KPI's :** `release year`, `runtime`, `imdb_score`, `tmdb_score`, `genre`, `production_counties`, `type`,
            `age_certification`, `role`, `name`, `character`, `imdb_votes`, `tmdb_popularity`
            
            ---
            """
        )
    
    def histogram_display(self):
        st.header("Histogram")
        cols = ['imdb_score', 'runtime', 'tmdb_score', 'release_year']

        #Histogram sidebar features
        #Show a sidebar multiselect to select display columns
        select_col = st.sidebar.multiselect(
            label= "Histogram",
            options= cols,
            key= "histogramColumns",
            placeholder= "Choose Columns"
            )
        st.sidebar.info(body= "Select multiple columns to display their graphs.", icon= "🎉")

        if not select_col:
            st.info("Choose which columns to display from the sidebar", icon= "ℹ️")   
        
        if select_col:
            for col in select_col:
                fig = px.histogram(self.__data, 
                                x= col, 
                                color= "type", 
                                color_discrete_sequence=px.colors.qualitative.Set2,
                                barmode= "overlay"
                                )
                # Slider for number of bins
                num_bins = st.slider("Select number of bins:", min_value=5, max_value=50, value=20, key= f"{col}")

                # Calculate bin width
                min_val = self.__data[col].min()
                max_val = self.__data[col].max()
                bin_width = (max_val - min_val) / num_bins

                fig.update_traces(
                    xbins=dict(size=bin_width),
                    marker_line_color = "black",
                    marker_line_width = 1,
                    hovertemplate= f"{col.replace('_', ' ').title()}: %{{x}}<br>Count: %{{y}}<extra></extra>"

                )
                fig.update_layout(
                    title_font_size=22,
                    title= f"Distribution of {col.replace('_', ' ').title()}"
                )

                fig.update_xaxes(title= f"{col.replace('_', ' ').title()}")
                fig.update_yaxes(title= "Count", tickformat= ",d")

                self.__display_graph(fig)

            #Display Graph Information and Findings
            st.write("### **What are the collective insights found ?**")
            st.write(
                """

                ---
                ##### **IMDb Score (imdb_score)**

                Most titles are rated 5–7 ⭐, showing generally good quality.
                Very few extremely low (<4) or very high (9–10) ratings 😮.
                Peak around 6 👍, indicating most content is above average.
                Movies vs TV shows (hue) may show slight differences.

                ---

                ##### **Runtime (runtime)**

                Two peaks:

                - Short runtimes (TV shows 📺)

                - Longer runtimes (Movies 🎬)

                `Hue shows TV shows tend to be shorter, movies longer ⏳.`

                ---

                ##### **TMDb Score (tmdb_score)**

                Similar to IMDb scores, clustering around 6–7 🎯.
                Shows content quality is generally good, few extreme scores 😅.

                ---

                ##### **Release Year (release_year)**

                Histogram shows production trends over time ⏰.
                Peaks indicate years with more content created 📈.
                Hue reveals whether Movies or TV shows dominated those years.

                ---

                ##### **Overall Insights**

                1) Most content is well-rated 👍

                2) Runtime and votes are skewed, showing most content is shorter and less voted ⏳.

                3) Movies vs TV shows differ in runtime, votes, and scores 📺🎬.

                4) Popularity is concentrated in a few hit titles 🌟.

                5) Production trends show booms in certain years ⏰.
                """
            )


        


        



        
