import streamlit as st

# title
st.title("Streamlit Raw Data")

# Raw Code
st.text("Display Raw Code")
st.code("Import math")
st.code("def sqrt(x):")

# Display Raw Data
with st.echo():
    # This will also show as a comment
    import seaborn as sns
    df = sns.load_dataset("titanic")

    