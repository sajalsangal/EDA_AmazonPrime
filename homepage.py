import pandas as pd
import streamlit as st

class HomePage:
    def __init__(self):
        self.__titleData = pd.read_csv("titles.csv")
        self.__creditsData = pd.read_csv("credits.csv")

    def homePageNavigation(self):
        #HomePage Navigation Settings
        st.sidebar.write(
            """
                **Welcome to my streamlit app**

                *Here we will take a look at Amazon Prime Dataset
                and vitualize it through interactive graphs. Watch the video to
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
            titleCSV = self.__titleData.to_csv().encode("utf-8")

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
            creditsCSV = self.__creditsData.to_csv().encode("utf-8")

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

    def homePageBody(self):
        #Home Page Main Area Properties
        st.title("Amazon Prime Analysis")

        #Add code video
        with open("../1fr.mp4", "rb") as videoFile: #Open video file
            videoData = videoFile.read()
        
        st.video( 
            data= videoData,
            format= "video/mp4",
        )

        #Body Content
        st.write(
            """
            The project `Amazon Prime TV Shows and Movies` focuses on conducting an in-depth analysis 
            of **Amazon Prime Video’s** content library, with the objective of uncovering meaningful 
            trends, patterns, and actionable insights related to its catalog of shows and movies.
            """
            )
        
        st.write("**Import Modules**")
        codeModule = """
    import streamlit as st
    import pandas as pd 
    import numpy as np 
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px
    import warnings

    warnings.filterwarnings("ignore", category= UserWarning, module= "matplotlib")
        """

        codeLoadDataset = """
    try:
        titles = pd.read_csv("titles.csv")
        credits = pd.read_csv("credits.csv")
    except:
        print("Error Loading Dataset")
        """

        st.code(body= codeModule, language= "python")
        st.write("**Load Dataset**")
        st.code(body= codeLoadDataset, language= "python")

        st.subheader("Dataset First View")

        #Titles Dataset
        st.write("- **Titles Dataset** `titles.head()`")
        st.write(self.__titleData.head())
        st.write(
            """
            > **Titles Dataset**, contains metadata for 9,871 titles with 15 attributes, 
            including title, type (movie or TV show), release year, age certification, runtime, 
            genres, production countries, and performance metrics such as IMDb and TMDB ratings, votes, and popularity.
        """
        )

        #Credits Dataset
        st.write("- **Credits Dataset** `credits.head()`")
        st.write(self.__creditsData.head())
        st.write(
            """
            > **Credits Dataset**, includes over 124,000 records detailing cast and crew members, 
            capturing information such as person name, role (actor/director), and character associations 
            with each title.
            """
        )

        st.subheader("Variable Description")

        desCol1, desCol2 = st.columns(2, border= True)

        desCol1.write(
            """
    **Titles Dataset (titles.csv)**

    > Contains metadata of TV shows and movies available on Amazon Prime.

    - id : Unique identifier of the title (`on JustWatch`).

    - title : Name of the movie or TV show.

    - type : Content type: Movie or TV Show.

    - description : Brief synopsis of the title.

    - release_year : Year in which the title was released.

    - age_certification : Age rating (`e.g., PG, R, 18+`).

    - runtime : Duration of the movie or average length of an episode (`in minutes`).

    - genres : List of genres (`Drama, Comedy, Action, etc.`).

    - production_countries : Countries involved in producing the title.

    - seasons : Number of seasons (`only for TV shows`).

    - imdb_id : Unique IMDb identifier.

    - imdb_score : IMDb rating score (`0–10`).

    - imdb_votes : Number of IMDb user votes.

    - tmdb_popularity : Popularity score from TMDB.

    - tmdb_score : TMDB rating score.
    """
        )

        desCol2.write(
            """
    **Credits Dataset (credits.csv)**

    > Contains cast and crew details for each title.

    - person_id : Unique identifier for an actor/director.

    - id : Title ID (`to link with titles dataset`).

    - name : Name of the person (`actor or director`).

    - character : Character played (`if actor`).

    - role : Role in the production (`ACTOR or DIRECTOR`).
    """
        )

        st.subheader("What Did You Learn About Dataset?")

        st.write(
            """
    > The dataset used in this project comes from Amazon Prime Video’s catalog, specifically for titles available in the United States. It was originally provided in two raw files, titles.csv and credits.csv and later merged, cleaned, and transformed into a consolidated dataset (df).


    *From exploring and analyzing the dataset, we observed the following:*

    ---
    #### **Dataset Size & Structure**

    - Titles dataset contained 9,871 unique shows and movies with 15 attributes.

    - Credits dataset contained 124,235 records of cast and crew with 5 attributes.

    `After cleaning and merging, the final dataframe (df) combined both, enabling title-level and person-level insights.`

    ---
    #### **Types of Variables**

    - `Categorical Variables:` Content type (Movie/Show), Age Certification, Genres, Production Countries, Role (Actor/Director).

    - `Numerical Variables:` Release Year, Runtime, Number of Seasons, IMDb/TMDB ratings, IMDb votes, TMDB popularity.

    - `Text Variables:` Title, Description, Name, Character.

    ---
    #### **Content Composition**

    - The catalog contains both movies and TV shows.

    - Genres are highly diverse, covering drama, comedy, action, thriller, and documentaries.

    - Content originates from multiple production countries, with the U.S. being dominant.

    ---
    #### **Ratings & Popularity**

    - Most titles have IMDb and TMDB ratings, which allowed us to assess audience reception.

    - Popularity scores from TMDB provide insights into trending content.

    ---
    #### **Cast & Crew Data**

    - Credits dataset enriches the analysis by linking actors and directors to titles.

    - This makes it possible to identify most featured actors, frequent directors, and collaboration patterns.

    ---
    #### **Data Quality & Cleaning**

    - The raw datasets contained missing values, outliers, and inconsistencies (e.g., missing runtimes, null age certifications, duplicate records).

    - Through data wrangling, these issues were addressed by:
    - Handling null values (imputation/removal).
    - Removing or capping outliers (e.g., extremely high runtimes, unrealistic ratings).
    - Standardizing categorical variables (genres, countries).
    - Merging duplicates and ensuring consistency across datasets.

    ---
    > ###### **This provides a comprehensive foundation for exploratory data analysis (EDA) and deriving business insights.**
    > Project By: @sajalsangal
    """
        )