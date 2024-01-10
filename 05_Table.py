import streamlit as st
import pandas as pd

# title
st.title("Streamlit Table")

# Table
table = pd.DataFrame(
    {
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40],
        "third column": [100, 200, 300, 400]
    }
)


st.table(table)

# Table - 3 columns
col1, col2, col3 = st.columns(3)
col1.table(table)
col2.table(table)
col3.table(table)


# Table - 2 columns
col1, col2 = st.columns(2)
col1.table(table)
col2.table(table)

# With Write methos
st.write(table)

# With Pandas
st.dataframe(table)