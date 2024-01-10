import streamlit as st

# title
st.title("Streamlit Sidebar")

# sidebar
with st.sidebar:
    st.markdown("# Sidebar")

# Using "with" notation
st.sidebar.checkbox("Show Sidebar")
st.sidebar.radio("Choose an option", ("Option 1", "Option 2", "Option 3"))
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
import time
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")