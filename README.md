# 🎬 Amazon Prime TV Shows and Movies  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1m6o6KJ4gt0P7ddjwJ-Sch2cKqBbg6tUA?usp=sharing)

[Live Hosted](https://smart-amazon-prime-analystics.streamlit.app/)

---

## 📌 Project Overview  
The **Amazon Prime TV Shows and Movies** project focuses on analyzing Amazon Prime Video’s U.S. content library using two datasets containing detailed information about titles (movies and TV shows) and their associated cast and crew.  

The goal is to uncover patterns, trends, and insights related to:  
- Content diversity  
- Regional distribution  
- IMDb/TMDB ratings  
- Popularity  
- Cast and crew involvement  

This analysis supports **content strategy, personalized recommendations, and audience engagement insights** for streaming platforms.  

---

## Streamlit App Preview
[Hosted](https://smart-amazon-prime-analystics.streamlit.app/)

#### Light Theme
<img width="1919" height="1079" alt="Screenshot 2025-10-04 213440" src="https://github.com/user-attachments/assets/60636bdd-3d1b-4c44-b040-fa81ff5448df" />

#### Dark Theme
<img width="1919" height="992" alt="Screenshot 2025-10-04 220107" src="https://github.com/user-attachments/assets/2249c866-93a3-4b45-bcc1-2eb9f4ddc1a4" />


## 📂 Dataset Description  

The project uses two CSV datasets:  

1. **Titles Dataset (titles.csv)**  
   - 9,871 unique titles  
   - 15 attributes:  
     - `id` – Title ID on JustWatch  
     - `title` – Name of the title  
     - `type` – TV show or movie  
     - `description` – Brief description  
     - `release_year` – Year of release  
     - `age_certification` – Age rating  
     - `runtime` – Length of movie/episode  
     - `genres` – List of genres  
     - `production_countries` – Producing countries  
     - `seasons` – Number of seasons (if TV show)  
     - `imdb_id`, `imdb_score`, `imdb_votes`  
     - `tmdb_popularity`, `tmdb_score`  

<img width="1734" height="759" alt="Screenshot 2025-10-04 214813" src="https://github.com/user-attachments/assets/79f40df0-5651-4a3c-acc4-1934d8483d9a" />


2. **Credits Dataset (credits.csv)**  
   - 124,235 records of cast and crew  
   - 5 attributes:  
     - `person_id` – Unique person ID  
     - `id` – Title ID (to link with titles dataset)  
     - `name` – Actor/Director name  
     - `character` – Character name (if actor)  
     - `role` – ACTOR or DIRECTOR
    
<img width="1752" height="318" alt="Screenshot 2025-10-04 214824" src="https://github.com/user-attachments/assets/eabd9efa-f3ce-4037-84d2-8dec1e2924c8" />


✅ After **data cleaning, wrangling, handling null values, and outlier removal**, both datasets were merged into a single consolidated dataframe (**df**) for analysis.  

---

## 🎯 Business Objective  
To analyze Amazon Prime Video’s content library and generate actionable insights regarding:  
- Dominant genres and formats (TV vs Movies)  
- Regional production trends  
- Evolution of the catalog over time  
- Audience engagement through IMDb/TMDB ratings, votes, and popularity  
- Key actors and directors shaping Prime’s content library  

---

## 📊 Analysis & Visualizations  

The analysis was performed using **Google Colab** with Python libraries:  
**Pandas, NumPy, Seaborn, Matplotlib, Plotly**.  

### 🔹 Univariate Analysis  
- Histogram  
- Bar Plot  
- Pie Plot  
- Box Plot  

### 🔹 Bivariate Analysis  
- Bar Plot  
- Scatter Chart  
- Line Chart  
- Box Plot  
- Pie Chart  
- Bubble Plot  
- Violin Plot  
- Donut Chart  
- Treemap  

### 🔹 Multivariate Analysis  
- Correlation Heatmap  
- Pair Plot  

---

## ⚙️ Tech Stack  
- **Platform:** Google Colab, VS Code  
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Seaborn, Matplotlib, Plotly, Streamlit  

---

## ⚙️ Steps to Run the Project

1. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   .venv/Scripts/activate 
2. **Clone the Repository**  
   ```bash
   git clone https://github.com/sajalsangal/EDA_AmazonPrime.git
   cd EDA_AmazonPrime
3. **Install requirements.txt**
   ```bash
   pip install requirements.txt
4. **Run Streamlit App**
   ```bash
   streamlit run streamlit_dashboard.py
     
Open the Project in Google Colab

Click the Colab badge below:.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1m6o6KJ4gt0P7ddjwJ-Sch2cKqBbg6tUA?usp=sharing)


Ensure you have internet access for Python library installation.

Install Required Libraries (if running locally)

bash
Copy code
pip install pandas numpy matplotlib seaborn plotly
Access Dataset

All datasets are stored in the data/ folder:

data/titles.csv → Amazon Prime titles metadata

data/credits.csv → Cast & crew information


Run the Notebook

Execute each cell in order.

Visualizations include:

Univariate: Histogram, Bar Plot, Pie Plot, Box Plot

Bivariate: Bar Plot, Scatter Chart, Line Chart, Box Plot, Pie Chart, Bubble Plot, Violin Plot, Donut Chart, Treemap

Multivariate: Pair Plot, Correlation Heatmap

Explore Insights

Analyze trends in Amazon Prime’s content library 📊

Check genres, IMDb ratings, regional distribution, and actor/director analysis.

Use visualizations to draw conclusions about content diversity & audience preferences.


## ✅ Conclusion  
The project demonstrates how Amazon Prime’s content catalog has evolved over time, highlighting:  
- The balance between TV shows and movies  
- Genre dominance and diversity  
- Regional production insights  
- IMDb/TMDB ratings’ role in popularity  
- Actor and director contributions  

These insights can support **strategic decisions in content acquisition, personalization, and audience targeting**, enabling Amazon Prime to drive **growth and subscriber engagement**.  

---

Last auto-commit: Thu Jul  2 03:20:33 UTC 2026
