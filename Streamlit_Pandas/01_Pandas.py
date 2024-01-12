# import libararies
import streamlit as st
import pandas as pd
import seaborn as sns

# Title
st.title("Streamlit Pandas")

# Load data
df = sns.load_dataset("titanic")


# Sidebar
st.sidebar.title("Sidebar")
selectbox = st.sidebar.selectbox("Choose Function", ["Data", "Data Describe", "Data Columns", "Null Values", "Null Values Percentage", 
                                        'Null Values Ascending', 'Null Values Descending', "Data Types"])

# Create a selectbox

# selectbox = st.selectbox("Choose one", ["Data", "Data Describe", "Data Columns", "Null Values", "Null Values Percentage", 
                      #                  'Null Values Ascending', 'Null Values Descending', "Data Types"])


def data_function():
    if selectbox == "Data":
        st.write(df.head())
    elif selectbox == "Data Describe":
        st.write(df.describe())
    elif selectbox == "Data Columns":
        st.write(df.columns)
    elif selectbox == "Null Values":
        st.write(df.isnull().sum())
    elif selectbox == "Null Values Percentage":
        st.write(df.isnull().sum() / len(df))
    elif selectbox == 'Null Values Ascending':
        st.write(df.isnull().sum().sort_values())
    elif selectbox == 'Null Values Descending':
        st.table(df.isnull().sum().sort_values(ascending=False))
    elif selectbox == "Data Types":
        st.table(df.dtypes)


data_function()
