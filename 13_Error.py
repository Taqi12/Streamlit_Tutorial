# import libraries
import streamlit as st

# title
st.title("Streamlit Error")

# Error
st.error("This is an error")

# Exception
st.exception(Exception("This is an exception"))

# warning
st.warning("This is a warning")

# info
st.info("This is an info")

# success
st.success("This is a success")

# help
st.help("This is an help")
st.help(range)