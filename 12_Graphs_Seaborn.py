import streamlit as st
import seaborn as sns

# title
st.title("Streamlit Graphs With Seaborn")

# sidebar
st.sidebar.title("Graphs")

# load data
df = sns.load_dataset("tips")
st.write(df.head())

option = st.sidebar.selectbox(
    "Choose a graph",
    ("Scatter", "Line", "Bar", "H_Bar", "Violin"))

if option == "Scatter":
    st.markdown("<h1 style='text-align: center;'>Scatter Graph</h1> ", unsafe_allow_html=True)
    fig = sns.scatterplot(x="total_bill", y="tip", data=df)
    st.pyplot(fig.get_figure())

elif option == "Line":
    st.markdown("<h1 style='text-align: center;'>Line Graph</h1> ", unsafe_allow_html=True)
    fig = sns.lineplot(x="total_bill", y="tip", data=df)
    st.pyplot(fig.get_figure())

elif option == "Bar":
    st.markdown("<h1 style='text-align: center;'>Bar Graph</h1> ", unsafe_allow_html=True)
    fig = sns.barplot(x="total_bill", y="tip", data=df)
    st.pyplot(fig.get_figure())

elif option == "H_Bar":
    st.markdown("<h1 style='text-align: center;'>Horizontal Bar Graph</h1> ", unsafe_allow_html=True)
    fig = sns.barplot(x="total_bill", y="tip", data=df, orient='h')
    st.pyplot(fig.get_figure())

elif option == "Violin":
    st.markdown("<h1 style='text-align: center;'>Violin Graph</h1> ", unsafe_allow_html=True)
    fig = sns.violinplot(x="total_bill", y="tip", data=df)
    st.pyplot(fig.get_figure())

