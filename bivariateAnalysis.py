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
            options= ["Line Plot", "Bar Plot", "Violin Plot","Bubble Chart" , "TreeMap"],
            key= "filterBivariate",
            help= "Choose to display graph 📈",
            index= 2
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

    def linePlot(self):
        st.header("Line Plot")
        cols = ['release_year vs runtime', 'release_year vs tmdb_popularity']

        #CountPlot Sidebar features
        #Show a sidebar multiselect to select display columns
        select_col = st.sidebar.multiselect(
            label= "Line Plot",
            options= cols,
            key= "LinePlotColumns",
            placeholder= "Choose Columns"
            )
        st.sidebar.info(body= "Select multiple columns to display their graphs.", icon= "🎉")

        if not select_col:
            st.info("Choose which columns to display from the sidebar", icon= "ℹ️") 

        if select_col:
            for col in select_col:
                column_headings = [x.strip() for x in col.split(sep= "vs")]
                filtered_data = self.__data.groupby([column_headings[0],'type']).agg({column_headings[1] : 'mean'}).reset_index()
                fig = px.line(
                        filtered_data,
                        x=column_headings[0],
                        y=column_headings[1],
                        markers=True,  # adds points on line
                        title=f"Average {column_headings[1].replace('_', ' ').title()} over the years",
                        color= "type",
                        color_discrete_sequence=px.colors.qualitative.Set2  # nice blue tone
                    )

                # Beautify the chart
                fig.update_traces(
                        line=dict(width=3),
                        marker=dict(size=10, symbol="circle", line=dict(width=2, color="white")),
                        hovertemplate=f"<b>Year:</b> %{{x}}<br><b>{column_headings[1].replace('_', ' ').title()}:</b> %{{y}}"
                    )

                fig.update_layout(
                        title_font=dict(size=22, family="Arial, sans-serif"),
                        title_x=0.25,  # center the title
                        xaxis=dict(
                            title="Release Year",
                            showgrid=True,
                            gridcolor="rgba(200,200,200,0.3)",
                            zeroline=False
                        ),
                        yaxis=dict(
                            title=f"{column_headings[1].replace('_', ' ').title()}",
                            showgrid=True,
                            gridcolor="rgba(200,200,200,0.3)",
                            zeroline=False
                        ),
                        plot_bgcolor="white",
                        paper_bgcolor="white",
                        margin=dict(l=60, r=60, t=80, b=60),
                        hovermode="x unified",  # single hover box
                        font=dict(family="Arial, sans-serif", size=14)
                    )

                self.__display_graph(fig)
            
            st.write("""

                    ---               
                    #### **Use Of Line Charts 📈**   

                    The dataset includes **time variables** (e.g., `release_year`) and ordered categorical fields, making line charts ideal for showing trends and changes over time.  

                    ##### **Temporal Trends ⏳**  

                    - Line charts reveal how metrics like popularity, ratings, or runtime evolve across years.  
                    - Example: Tracking whether movies are getting longer ⏱️ or shorter, or whether audience popularity ❤️ for certain genres is increasing or declining.  

                    ##### **Comparison with Hue 🎨**  

                    - Adding hue (e.g., type = Movie 🎬 vs TV Show 📺) allows easy comparison of multiple trends at once.  
                    - Example: Determining which content type gained more attention after 2015.  

                    ##### **Easy Storytelling 📝**  

                    - Line charts are intuitive and allow stakeholders to quickly spot growth 📈, decline 📉, or stability ➖.  
                    - Perfect for communicating trends and making data-driven business decisions.  

                    ##### **Overall**  

                    Line charts are ideal for this dataset because they highlight **temporal patterns ⏳**, **ordered categorical progressions 📊**, and **trend-based business insights 🔑**.

                     """)
            
            st.write("""
                     
                    ---
                    #### **📊 Insights from Line Charts**

                    ##### **Content Growth Over Time 🎬📺**  
                    Number of movies 🎥 and TV shows 📺 released has increased significantly after 2010 🚀.  
                    This suggests the streaming boom and global content expansion 🌍.

                    ##### **Runtime Trends ⏱️**  
                    Average movie runtimes are increasing 📉, while TV shows maintain steady lengths ➖.

                    ##### **Score and Popularity** 
                    Score and popularity trends look consistent with time.

                    ##### ✨ **In short:**  
                    The dataset shows a clear surge in content production 📈, especially in recent years.  
                    Viewer preferences are shifting toward shorter, diverse, and family-friendly content 🎉.  
                    These trends can guide content strategy, marketing, and platform investments 💰.                
                     """)
            
    def barplot(self):
        st.header("Bar Plot")
        cols = ['runtime vs age_certification', 'imdb_score vs age_certification']

        #BarPlot Sidebar features
        #Show a sidebar multiselect to select display columns
        select_col = st.sidebar.multiselect(
            label= "Bar Plot",
            options= cols,
            key= "BarPlotColumns",
            placeholder= "Choose Columns"
            )
        st.sidebar.info(body= "Select multiple columns to display their graphs.", icon= "🎉")

        if not select_col:
            st.info("Choose which columns to display from the sidebar", icon= "ℹ️") 

        if select_col:
            for col in select_col:

                col_heading = [x.strip() for x in col.split(sep= "vs")]
                filtered_data = self.__data.groupby(col_heading[1]).agg({col_heading[0] : 'mean'}).reset_index()

                fig = px.bar(filtered_data[filtered_data[col_heading[1]] != "Unknown"],
                             x= col_heading[1],
                             y= col_heading[0],
                             color= col_heading[1],
                             color_discrete_sequence=px.colors.qualitative.Vivid,
                             opacity= 0.8,
                             text_auto=True   # Show values on bars
                             )
                fig.update_traces(
                    textfont_size=12,
                    textangle=0,
                    textposition="outside",
                    marker=dict(line=dict(width=1, color="white"))  # Clean white border
                )

                fig.update_layout(
                    title=dict(
                        text=f"Distribution of {col_heading[0].replace('_',' ').title()} by {col_heading[1].replace('_',' ').title()}",
                        x=0.35,  # center title
                        xanchor="center",
                        font=dict(size=22, family="Arial, sans-serif")
                    ),
                    xaxis=dict(
                        title=col_heading[1].replace("_", " ").title(),
                        showgrid=False,
                    ),
                    yaxis=dict(
                        title=col_heading[0].replace("_", " ").title(),
                        showgrid=True,
                        zeroline=False,
                        tickformat=",d"  # Add commas for large numbers
                    ),
                    plot_bgcolor="white",
                    bargap=0.3,  # spacing between bars
                    margin=dict(l=40, r=40, t=80, b=80),
                )
                
                self.__display_graph(fig)

            st.write("""

                    ---
                    #### **Insights From The Graphs**
                                        
                    ##### **Runtime by Age Certification ⏱️**  

                    - Different age certifications show distinct runtime distributions.  
                    - PG-13 and R-rated content tends to have longer runtimes, while lower-rated content (G, PG) is shorter.  
                    - This aligns with audience expectations for complex or mature content being longer.  

                    ---
                    ##### **IMDb Score by Age Certification 🔞**  

                    - TV-PG and TV-V7 content show slightly higher median scores, suggesting better reception for teen/adult-oriented content.  
                    - G-rated or PG content is fewer and may not be as widely rated.
                       
                     """)
            
    def violinPlot(self):
        st.header("Violin Plot")

        fig = px.violin(self.__data,
                        x= "type",
                        y= "imdb_score",
                        color= "type",
                        box=True,  # show embedded boxplot for median & IQR
                        color_discrete_sequence= px.colors.qualitative.Set1
                        )
        
        fig.update_traces(
            meanline_visible=True,  # show mean line inside violin
            scalemode="count",      # width depends on sample size
            jitter=0.5,             # spread points for visibility
            marker=dict(size=4, opacity=0.6, line=dict(width=0.5, color="white"))
        )
        fig.update_layout(
            title=dict(
                text="IMDb Score Distribution by Type",
                x=0.35,
                xanchor="center",
                font=dict(size=22, family="Arial, sans-serif")
            ),
            xaxis=dict(
                title="Type",
                showgrid=False,
                zeroline=False
            ),
            yaxis=dict(
                title="IMDb Score",
                showgrid=True,
                zeroline=False,
                rangemode="tozero"
            ),
            plot_bgcolor="white",
            margin=dict(l=60, r=40, t=80, b=60),
        )
        
        self.__display_graph(fig)

        st.write("""
                 
                ---
                #### **Use of Violin Plots**  

                                
                ##### **Shows Distribution Shape 🎨**   

                - Unlike a box plot, violin plots display the full distribution of the data using a kernel density estimate.  
                - Reveals skewness, multi-modality, and other patterns in numeric variables that boxplots alone might hide.  

                ---
                ##### **Summarizes Statistics 📊**  

                - Violin plots include median and interquartile ranges, combining the benefits of boxplots and density plots.  
                - Helps to quickly assess central tendency and spread.  

                 
                ---  
                ##### **Bivariate Comparison 🔍**  

                - When plotting a numeric variable against a categorical variable, you can see how the distribution changes across categories.  
                - Adding a hue allows comparison across a secondary categorical variable, giving deeper insights.  

                 
                ---  
                ##### **Compact and Visual 🖼️**  

                - Multiple violin plots can be displayed as subplots, making it easy to compare distributions across many numeric-categorical pairs in one figure.  

                 
                ---  
                ##### **Handles Unequal Sample Sizes Well ⚖️**  

                - Even if some categories have fewer samples, violin plots still show the density, making comparisons meaningful.  

                 
                ---  
                #### **Insights**  
                 
                ##### **IMDb Score by Type 🎬**  

                - Movies and TV shows have slightly different distributions.  
                - Movies tend to have a wider spread of scores, whereas TV shows are slightly more clustered.  
                - Median scores are roughly similar, indicating that both content types maintain comparable quality on average.  
                """)


            
    def bubblechart(self):
        st.header("Bubble Chart")


        

