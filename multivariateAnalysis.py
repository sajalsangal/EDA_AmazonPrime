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
        
    def pairplot(self):
        st.header("Pair Plot")

        numeric_cols = self.__data.select_dtypes(include= "number")

        fig = px.scatter_matrix(self.__data[self.__data != "Unknown"],
                                dimensions= numeric_cols,
                                color= "type",
                                title="🎨 Interactive Pair Plot of Numeric Columns",
                                color_discrete_sequence=px.colors.qualitative.Pastel,  # clean, soft colors
                                height=800,
                                width=900,
                                
                                 )                        
        # Update marker style for clarity
        fig.update_traces(
            marker=dict(size=4, opacity=0.8, line=dict(width=0.4, color='DarkSlateGrey')),
            diagonal_visible=False,
        )

        # Update layout for good look and feel
        fig.update_layout(
            dragmode='select',
            hovermode='closest',
            plot_bgcolor='white',
            title_font_size=20,
            margin=dict(l=50, r=50, t=80, b=50),
            xaxis=dict(showgrid=True, zeroline=False),
            yaxis=dict(showgrid=True, zeroline=False)
        )
        self.__display_graph(fig)

        st.write("""
                 
                 ---
                ### **Use Of Pair Plot**
                 
                #### **Bivariate Analysis Across All Numeric Columns 📊:**  
                The dataset has multiple numeric columns (imdb_score, imdb_votes, tmdb_popularity, tmdb_score, runtime, release_year).  
                A scatter matrix lets us visually inspect relationships between every pair of numeric variables at once 🔍.  

                 ---
                #### **Interactive Exploration 🖱️:**  
                Using Plotly makes it interactive: hover to see movie titles, zoom, pan, and select points.  
                Very useful for spotting patterns, outliers, or clusters in large datasets 🌟.  

                 ---
                #### **Hue for Categorical Separation 🎨:**  
                Adding type (Movies vs Shows) as hue lets us compare patterns within each category.  
                We can see if Movies and Shows differ in imdb_score, popularity, or runtime 🎬.  

                 ---
                #### **Compact and Informative 🗂️:**  
                Instead of multiple individual scatter plots, the scatter matrix combines all relationships into one grid, saving space and giving a complete view ✨.  

                 ---
                #### **Detect Correlations and Patterns Quickly 💡:**  
                Makes it easy to spot linear/non-linear relationships, clusters, or extreme values, which can inform further analysis or modeling decisions 🔑.  

                 ---
                #### **Interactive & Colorful 😎:**  
                Plotly’s interactivity and vibrant but clean colors make the visualization more appealing and insightful than static plots 🌈.

                 """)
        
        st.write("""
                 
                 ---
                 ### **Insights**

                #### **IMDb Scores vs Release Year 🎬**  

                - **Observation:** Older movies/shows tend to have a wide range of IMDb scores, while newer releases cluster in a narrower range.  
                - **Positive growth opportunity:** Shows may have slightly lower scores compared to movies in recent years.  
                > ✅ Positive impact: Helps plan content release strategies and monitor quality trends.  

                 ---
                #### **Votes vs Popularity 📊**  

                - **Observation:** imdb_votes and tmdb_popularity are positively correlated.  
                - **Positive growth opportunity:** Highly popular titles tend to receive more votes; outliers with extremely high votes/popularity stand out clearly 🌟.  
                > ✅ Positive impact: Identifies top-performing content for marketing and promotion focus.  

                 ---
                #### **Genre/Type Differences 🎨**   

                - **Observation:** Using type as hue (Movies vs Shows) reveals patterns: Movies generally have higher tmdb_popularity than Shows; certain clusters are dominated by one type.  
                - **Positive growth opportunity:** Target content type-specific strategies to enhance engagement.  
                > ✅ Positive impact: Guides type-specific production and promotion planning.  

                 ---
                #### **Score Relationships ⭐**  

                - **Observation:** imdb_score and tmdb_score are moderately correlated; some exceptions appear as outliers.  
                - **Positive growth opportunity:** Highly rated IMDb titles often also have high TMDB ratings.  
                > ✅ Positive impact: Supports content quality assessment and cross-platform consistency.  

                 ---
                #### **Runtime Patterns ⏱️**  

                - **Observation:** Movies have a wider range of runtimes; Shows cluster at shorter durations.  
                - **Positive growth opportunity:** Extreme runtime values can indicate anomalies or special content.  
                > ✅ Positive impact: Aids in content planning and audience targeting.  

                 ---
                #### **Outliers & Clusters 🔍**  

                - **Observation:** Outliers, such as movies with extremely high votes or unusually high/low scores, are easily spotted; clusters reveal common patterns in popular, well-rated content 🎉.  
                - **Positive growth opportunity:** Leverage insights from clusters for content recommendations and marketing.  
                > ✅ Positive impact: Enables identification of high-value content and trends.  

                 ---
                #### **Overall Insight**   

                > The scatter matrix allows visual exploration of relationships, detection of outliers, and observation of type-based patterns across multiple numeric features at once. It’s effective for spotting trends, anomalies, and correlations in the dataset 📽️✨.

                 """)





    
