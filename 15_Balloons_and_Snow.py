import streamlit as st

# title
st.title("Streamlit Balloons")

# Balloons Function
def balloons():
    st.balloons()

def snow():
    st.snow()

# Ballons Button
#ballon = st.button("Balloons", on_click=balloons) 

# Snow Button
#snow = st.button("Snow", on_click=snow)

col1, col2 = st.columns(2)
col1.button("Balloons", on_click=balloons)
col2.button("Snow", on_click=snow)