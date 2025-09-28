# complete code
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")


# Set the default Seaborn theme
sns.set_theme(style="whitegrid")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Page:",
    ["Welcome", "Univariate Analysis", "Bivariate Analysis", "Multivariate Analysis"],
    key="navigation"
)

# Welcome Page
if page == "Welcome":
    st.title("Welcome to the Data Analysis Application 🎉")
    st.write(
        """
        This application is designed for dynamic data visualization and analysis using your uploaded dataset. It supports:

        - **Univariate Analysis:** Single-variable exploration.
        - **Bivariate Analysis:** Explore relationships between two variables.
        - **Multivariate Analysis:** Advanced insights involving multiple variables.

        ### Features include:
        - Interactive visualizations.
        - Seamless data upload and processing.
        - Advanced plots with custom options.

        Navigate through the sidebar options to begin your journey! 📊
        """
    )

# Upload dataset for analysis
if page != "Welcome":
    st.sidebar.title("Upload Dataset")
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file here", type=["csv"], key="uploader")

    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.sidebar.success("Dataset Loaded Successfully!")
    else:
        st.sidebar.info("Please upload a dataset to proceed.")
        st.stop()

    # Define numeric and categorical columns
    numeric_columns = data.select_dtypes(include="number").columns.tolist()
    categorical_columns = data.select_dtypes(include="object").columns.tolist()

    # Helper function to display plots
    def display_plot(fig):
        st.pyplot(fig)

# Univariate Analysis
if page == "Univariate Analysis":
    st.title("Univariate Analysis", anchor=False)
    st.header("Explore Single-Variable Trends")
    st.write("Explore univariate plots with dynamic column selection.")

    # Create a 2x2 subplot layout with increased figure width
    fig, axes = plt.subplots(2, 2, figsize=(22, 13))

    # Histogram
    hist_col = st.selectbox("Select column for Histogram:", numeric_columns, key="hist", index=0)
    sns.histplot(data[hist_col], kde=True, ax=axes[0, 0])
    axes[0, 0].set_title(f"Histogram of {hist_col}", fontsize=30, color="red", weight="bold")
    axes[0, 0].tick_params(axis='x', labelsize=15, rotation=90)




    # Countplot
    if categorical_columns:
        count_col = st.selectbox("Select column for Countplot (Categorical):", categorical_columns, key="countplot", index=0)
        sns.countplot(data=data, x=count_col, ax=axes[0, 1])
        axes[0, 1].set_title(f"Countplot of {count_col}", fontsize=30, color="red", weight="bold")
        axes[0, 1].tick_params(axis='x', labelsize=15, rotation=90)



    # Pie Chart
    if categorical_columns:
        pie_col = st.selectbox("Select column for Pie Chart:", categorical_columns, key="pie", index=0)
        top_categories = data[pie_col].value_counts().sort_values(ascending=False).head(5)
        top_categories.plot.pie(autopct='%1.1f%%', ax=axes[1, 0], textprops={'fontsize': 30})
        axes[1, 0].set_title(f"Pie Chart of Top 5 Categories in {pie_col}", fontsize=30, color="red", weight="bold")



    # Boxplot
    box_col = st.selectbox("Select column for Boxplot:", numeric_columns, key="box", index=0)
    sns.boxplot(data=data, x=box_col, ax=axes[1, 1])
    axes[1, 1].set_title(f"Boxplot of {box_col}", fontsize=30, color="red", weight="bold")
    axes[1, 1].tick_params(axis='x', labelsize=15, rotation=90)


    plt.tight_layout()
    display_plot(fig)

# Bivariate Analysis
elif page == "Bivariate Analysis":
    st.title("Bivariate Analysis", anchor=False)
    st.header("Explore Relationships Between Two Variables")
    st.write("Explore bivariate relationships with dynamic column selection.")

    # Create a 3x2 subplot layout with increased figure width
    fig, axes = plt.subplots(2, 2, figsize=(22, 13))

    # Line Plot 1
    line_x1 = st.selectbox("X for Line Plot 1:", numeric_columns, key="line_x1", index=0)
    line_y1 = st.selectbox("Y for Line Plot 1:", numeric_columns, key="line_y1", index=0)
    sns.lineplot(data=data, x=line_x1, y=line_y1, ax=axes[0, 0])
    axes[0, 0].set_title(f"Line Plot of {line_x1} vs {line_y1}", fontsize=30, color="red", weight="bold")
    axes[0, 0].tick_params(axis='x', labelsize=15, rotation=90)


    # Scatter Plot
    scatter_x = st.selectbox("X for Scatter Plot:", numeric_columns, key="scatter_x", index=0)
    scatter_y = st.selectbox("Y for Scatter Plot:", numeric_columns, key="scatter_y", index=0)
    sns.scatterplot(data=data, x=scatter_x, y=scatter_y, ax=axes[0, 1])
    axes[0, 1].set_title(f"Scatter Plot of {scatter_x} vs {scatter_y}", fontsize=30, color="red", weight="bold")
    axes[0, 1].tick_params(axis='x', labelsize=15, rotation=90)


    # Bar Plot
    if categorical_columns:
        bar_x = st.selectbox("X for Bar Plot (Categorical):", categorical_columns, key="bar_x", index=0)
        bar_y = st.selectbox("Y for Bar Plot (Numeric):", numeric_columns, key="bar_y", index=0)
        sns.barplot(data=data, x=bar_x, y=bar_y, ax=axes[1, 0])
        axes[1, 0].set_title(f"Bar Plot of {bar_x} vs {bar_y}", fontsize=30, color="red", weight="bold")
        axes[1, 0].tick_params(axis='x', labelsize=15, rotation=90)


    # Boxplot
    box_x = st.selectbox("X for Boxplot (Categorical):", categorical_columns, key="box_x_bi", index=0)
    box_y = st.selectbox("Y for Boxplot (Numeric):", numeric_columns, key="box_y_bi", index=0)
    sns.boxplot(data=data, x=box_x, y=box_y, ax=axes[1, 1])
    axes[1, 1].set_title(f"Boxplot of {box_x} vs {box_y}", fontsize=30, color="red", weight="bold")
    axes[1, 1].tick_params(axis='x', labelsize=15, rotation=90)


    plt.tight_layout()
    display_plot(fig)

# Multivariate Analysis
elif page == "Multivariate Analysis":
    st.title("Multivariate Analysis", anchor=False)
    st.header("Discover Patterns Across Multiple Variables")
    st.write("Generate Pairplot and Heatmap for multivariate analysis.")

    # Pairplot
    st.subheader("Pairplot")
    if numeric_columns:
        pairplot_cols = st.multiselect("Select columns for Pairplot:", numeric_columns, default=numeric_columns[:min(3, len(numeric_columns))])
        if pairplot_cols:
            pairplot_fig = sns.pairplot(data[pairplot_cols])
            st.pyplot(pairplot_fig)
        else:
            st.warning("Please select at least one column for the Pairplot.")
    else:
        st.error("No numeric columns available for Pairplot.")

    # Heatmap
    st.subheader("Heatmap")
    if numeric_columns:
        fig, ax = plt.subplots(figsize=(40, 30))
        sns.heatmap(data[numeric_columns].corr(), annot=True, cmap="coolwarm", ax=ax, annot_kws={"size": 30})
        ax.set_title("Correlation Heatmap", fontsize=40, color="red", weight="bold")
        ax.tick_params(axis='x', labelsize=40)
        ax.tick_params(axis='y', labelsize=40)
        display_plot(fig)
    else:
        st.error("No numeric columns available for Heatmap.")