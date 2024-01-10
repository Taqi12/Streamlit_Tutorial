import streamlit as st

# title
st.title("Streamlit Removing Something from Streamlit")

# Remobing Footer
st.markdown("""
<style>
.st-emotion-cache-h5rgaw.ea3mdgi1 /*class name of the footer*/
{
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# Removing Deploy Button
st.markdown("""
<style>
.st-emotion-cache-ztfqz8.ef3psqc4 {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)