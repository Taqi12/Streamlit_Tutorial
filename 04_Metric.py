import streamlit as st

# title
st.title("Streamlit Metric")

# Metric
st.metric("Temperature", "70 °F", "1.2 °F")

st.metric(label="Temperature", value="40 °C", delta="-1.2 °F") # delta Indicator of how the metric changed

st.metric(label="Temperature", value="40 °C", delta="-1.2 °F", delta_color="off")

st.metric(label="Temperature", value="40 °C", delta="-1.2 °F", delta_color="normal")

st.metric(label="Temperature", value="40 °C", delta="-1.2 °F", delta_color="inverse")

st.markdown("### Metric - 3 columns")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.markdown("---")

st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")