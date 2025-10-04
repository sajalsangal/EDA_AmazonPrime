import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

class MultiVariate:
    def __init__(self):
        self.__data = pd.read_csv("merged_dataset.csv")

    def __display_graph(self, fig):
        st.plotly_chart(fig, use_container_width=True)

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

    def heatmap(self):
        st.header("HeatMap")

        # Compute correlation matrix (numeric only)
        corr = self.__data.corr(numeric_only=True)

        # Create heatmap
        fig = px.imshow(
            corr,
            text_auto=".2f",           # show values with 2 decimal places
            color_continuous_scale="Viridis",
            aspect="auto"              # adjust aspect ratio
        )

        fig.update_layout(
            title="Correlation Heatmap",
            title_font_size=20,
            title_x=0.35,               # center title
            margin=dict(l=60, r=60, t=60, b=60)
        )

        self.__display_graph(fig)

        st.write("""
                  
                 ---
                 ### **Use of HeatMap**
                #### **Shows pairwise relationships clearly 🔍:**  
                With multiple numeric columns like imdb_score, imdb_votes, runtime, tmdb_popularity, and tmdb_score, a heatmap allows you to see how each variable relates to others at a glance.  

                 ---
                #### **Highlights strong correlations ⭐:**  
                Positive correlations (moving in the same direction) and negative correlations (moving in opposite directions) are immediately visible through color intensity.  

                 ---
                #### **Compact representation 📦:**  
                Instead of plotting multiple scatter plots for each pair, a heatmap summarizes all pairwise correlations in one concise visual.  

                 ---
                #### **Interactive exploration with Plotly 🖱️:**  
                Using hover, you can see exact correlation values, making it easier to interpret the data interactively.  
                Zooming and panning allow for better analysis when many variables are present.  

                 ---
                #### **Professional & clean look 🎨:**  
                With a sober color palette, it’s suitable for presentations, dashboards, or reports, making insights immediately understandable.  

                > ✅ In short: The correlation heatmap lets you quickly identify relationships, spot potential predictors, and understand how numerical features interact, which is essential for any data-driven decision-making process 😎✨.

                 """)
        
        st.write("""
                 
                 ---
                ### **Insights Found**
                #### **IMDb Score vs Other Metrics ⭐**  

                - **imdb_score and imdb_votes:** Usually a mild positive correlation, indicating that highly-rated titles tend to attract more votes, but some popular titles may not have high scores.  
                - **imdb_score and tmdb_score:** Strong positive correlation, meaning that ratings from IMDb and TMDB are generally aligned, reflecting consistent audience perception.  

                 ---
                #### **Popularity vs Engagement 🎯**  

                - **tmdb_popularity and imdb_votes:** Positive correlation, suggesting that titles that are popular on TMDB tend to get more votes on IMDb, indicating cross-platform engagement.  

                 ---
                #### **Runtime Patterns ⏱️**  
                 
                - **runtime correlations:** Usually low or negligible with other variables, implying that movie length does not strongly affect ratings or popularity.  

                 ---
                #### **TMDB Score Insights 🎬**  

                - **tmdb_score and tmdb_popularity:** Slight positive correlation, meaning higher-rated titles on TMDB are somewhat more popular, but there are exceptions.  

                 ---
                #### **General Observations 😎**  

                - Most correlations are moderate, no extreme negative relationships, meaning that features are fairly independent, which can be useful for modeling or predictive analytics.  
                - Highly correlated metrics (imdb_score & tmdb_score) can be combined or weighted in business insights.  


                 """)



    
