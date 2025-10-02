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
            index= 2
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
            st.write("### **Detailed Insights From Each Column**")
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

    def boxplot_display(self):
        st.header("BoxPlot")
        cols = ['imdb_votes', 'tmdb_popularity']

        #Boxplot sidebar features
        #Show a sidebar multiselect to select display columns
        select_col = st.sidebar.multiselect(
            label= "BoxPlot",
            options= cols,
            key= "boxPlotColumns",
            placeholder= "Choose Columns"
            )
        st.sidebar.info(body= "Select multiple columns to display their graphs.", icon= "🎉")

        if not select_col:
            st.info("Choose which columns to display from the sidebar", icon= "ℹ️") 

        
        if select_col:
            for col in select_col:
                # Calculate slider range
                min_val = self.__data["release_year"].min()
                max_val = self.__data["release_year"].max()

                # Slider for range of year
                value_range = st.slider("Select Year Range", min_value=min_val, max_value=max_val, value=(min_val, max_val), key= f"{col}")

                fig = px.box(self.__data[(self.__data["release_year"] >= value_range[0]) & (self.__data["release_year"] <= value_range[1])], 
                    x = col, 
                    color= "type",
                    template="plotly_dark", # Sleek dark theme (can use "plotly_white" if preferred)
                    color_discrete_sequence=px.colors.qualitative.Pastel,  # Soft, pleasant colors
                    hover_data= ["title", "release_year", "age_certification"],
                    )

                fig.update_traces(
                    marker=dict(size=6, line=dict(width=1, color='DarkSlateGrey'))
                )

                fig.update_layout(
                    title_font_size=22,
                    title= f"Distribution of {col.replace('_', ' ').title()}"
                )

                fig.update_yaxes(title= f"{col.replace('_', ' ').title()}", showgrid = True)
                fig.update_xaxes(title= "Values", showgrid = True, tickformat= ",d")

                self.__display_graph(fig)

            st.write("### **Detailed Insights From Each Column**")

            st.write(
                """
                ---
                ##### **Distribution of Numeric Columns**  

                **imdb_votes**  
                Most ratings cluster in the mid-to-high range. Some extremely low or high scores appear as outliers, highlighting highly unpopular or extremely well-rated content.  

                **tmdb_popularity**  
                Highly skewed distribution: a few titles get massive attention (outliers), while most get moderate votes/popularity.  

                ---
                ##### **Skewness and Spread**   

                Columns like imdb_votes and tmdb_popularity are right-skewed, indicating most content has moderate attention, and few are extremely popular.  

                Columns like imdb_score might have a tighter spread, showing most content falls in a typical rating range.  

                """
            )

            st.write(
                """

                ---
                ### **Positive Business Impact**

                ##### Understanding Content Performance

                IMDB/TMDB scores and votes show which content is most liked and engaged with.

                **Actionable insight**: Invest more in content types or genres that consistently receive high scores and popularity. ""

                ---
                ##### Outlier Identification

                Extremely long or short content, or highly unpopular content, is visible as outliers.

                **Actionable insight**: Avoid producing extremely long content unless it’s proven to engage audiences; similarly, identify why some content fails to gain votes/popularity. ""

                ---
                ##### Skewed Popularity Metrics

                Columns like tmdb_popularity are right-skewed, showing that a few titles dominate attention.

                **Actionable insight:** Strategically promote underperforming but high-quality content to balance audience engagement. ""

                ---
                ### **Negative Impact**

                ##### Skewed Popularity Metrics

                **Observation:** Columns like imdb_votes and tmdb_popularity are highly right-skewed.

                **Negative impact:** Most content gets low engagement while only a few titles dominate popularity.

                **Risk:** Relying on the same top-performing content repeatedly could lead to over-dependence on a few hits, leaving most content underperforming.

                ---
                ##### Low Ratings

                **Observation:** Outliers with very low imdb_score or tmdb_score appear in the box plots.

                **Negative impact:**

                Low-rated content can damage brand perception if such content is frequent. May reduce subscriber retention or discourage engagement.

                """
            )

    def countplot_display(self):
        st.header("Count Plot")
        cols = ['genres', 'production_countries', 'name', 'character']

        #CountPlot Sidebar features
        #Show a sidebar multiselect to select display columns
        select_col = st.sidebar.multiselect(
            label= "CountPlot",
            options= cols,
            key= "CountPlotColumns",
            placeholder= "Choose Columns"
            )
        st.sidebar.info(body= "Select multiple columns to display their graphs.", icon= "🎉")

        if not select_col:
            st.info("Choose which columns to display from the sidebar", icon= "ℹ️") 

        if select_col:
            for col in select_col:
                
                #Top N values in column
                top_n = 20

                #Slider to choose how many top values to display
                value_range = st.slider("Select Top(N) Elements", min_value=1, max_value=top_n, value= 15, key= f"{col}")
                filtered_data = self.__data[self.__data[col] != "Unknown"][col].value_counts().nlargest(value_range)

                fig = px.bar(filtered_data, 
                             x= filtered_data.index, 
                             y = filtered_data.values,
                             text=filtered_data.values,   # Show counts on bars
                             color=filtered_data.index,   # Different color for each category
                             color_discrete_sequence=px.colors.qualitative.Vivid  # Vibrant palette
                             )
                
                fig.update_layout(
                    title_font_size=22,
                    title= f"Distribution of {col.replace('_', ' ').title()}"
                )

                fig.update_traces(
                    texttemplate='%{text:,}',     # Add commas to big numbers
                    textposition='outside',       # Labels above bars
                    marker=dict(line=dict(width=1, color="DarkSlateGray"))  # Clean bar edges
                )

                fig.update_xaxes(title= f"{col.replace('_', ' ').title()}", showgrid = True)
                fig.update_yaxes(title= "# Of Values", tickformat= ",d")

                self.__display_graph(fig)

            st.write("#### Detailed Insights From Each Column")

            st.write(
                """

                ---
                ##### **Movies Dominate Shows**

                The dataset is heavily skewed toward movies across genres, actors, and roles.
                
                ---
                ##### **Genres – Drama Leads Strongly**

                Drama is the most common genre by a large margin, followed by comedy and documentaries.

                Multi-genre blends (Drama+Romance, Thriller+Drama, etc.) are also well-represented.

                ---
                ##### **Production – US-Centric**

                Nearly all productions are US-based (~48k), with India, UK, Canada, and France trailing far behind.

                Co-productions exist but are minimal in volume.

                ---
                ##### **Actors & Characters – Classic & Generic**

                Frequent actors are largely from classic Hollywood (e.g., Roy Rogers, Gene Autry).

                Character roles are often generic (Himself, Nurse, Sheriff, Waitress), pointing to many documentaries and background roles.
            """
            )

            st.write(
                """
                    ---
                    #### Positive Impact

                    ##### **Focus on high-demand categories 🌟**

                    *   **Observation:** The tallest bars indicate the most frequent or popular categories.
                    *   **Business impact:** You can invest more in popular genres, regions, or product types to maximize ROI, engagement, or sales.

                    ---
                    ##### **Explore underserved categories 🌱**

                    *   **Observation:** Short bars show underrepresented categories.
                    *   **Business impact:** These represent growth opportunities. Investing in niche or emerging categories can capture untapped market segments.

                    ---
                    ##### **Early detection of issues ⚠️**

                    *   **Observation:** Tiny or unexpected categories can indicate data inconsistencies.
                    *   **Business impact:** Fixing data quality issues early prevents wrong business decisions based on flawed data.

                    ---
                    #### Negative Impacts

                    ##### **Over-reliance on dominant categories ⚠️**

                    *   **Observation:** Some categories dominate the dataset (very tall bars), while others are rare.
                    *   **Negative impact:** Focusing too much on the top categories may ignore emerging or niche markets. Competitors could capture these underserved segments, leading to missed growth opportunities.

                    ---
                    ##### **High-cardinality categories with insufficient focus 🔍**

                    *   **Observation:** Columns with many unique values (e.g., production countries, creators) may have some categories barely represented.
                    *   **Negative impact:** Without targeted strategies, these low-frequency categories may never gain traction, limiting expansion opportunities.

                    ---
                    ##### **Hidden data quality issues 🛑**

                    *   **Observation:** Unexpected or empty categories appear as tiny bars.
                    *   **Negative impact:** Poor data quality can mislead decision-making, causing investments in wrong areas, inefficiency, or reputational risk.

                    ---
                    ##### **Overcrowded focus on niche categories without ROI 💸**

                    *   **Observation:** Some rare categories are small but tempting to invest in.
                    *   **Negative impact:** Spending too much on very low-frequency categories may drain resources without sufficient return.
                    """
            )


                


        


        



        
