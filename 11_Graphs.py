# import libararies
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


# title
st.title("Streamlit Graphs")

# create a table
table = pd.DataFrame(
    {
        "co1": [1, 2, 3, 4],
        "col2": [10, 20, 30, 40],
        "col3": [100, 200, 300, 400],
        "col4": [1000, 2000, 3000, 4000]
    }
)

# create data
X = np.linspace(0, 10, 100)
Y = np.sin(X)
Z = np.cos(X)
T = np.tan(X)

bar_x = np.array([1, 2, 3, 4, 5])
scatter_x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
scatter_y = np.array([-2, 0, 2, 4, 6, 8, -10, 12, -14, 16, 18, 20, 22, 24, 26, 28, -300, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60])
hist_x = np.random.normal(170, 10, 250)
# make sidebar
st.sidebar.title("Sidebar For Graphs")

# make graphs
option = st.sidebar.radio("Choose an option", ("Line", "Scatter", "Bar",'H_Bar', "Histogram"))
if option == "Line":
    st.markdown("<h1 style='text-align: center;'>Line Graph</h1> ", unsafe_allow_html=True)
    fig = plt.figure()
    plt.plot(X, Y)
    plt.plot(X, Z, '--')
    plt.plot(X, T, '-.')
    st.write(fig)
elif option == "Scatter":
    st.markdown("<h1 style='text-align: center;'>Scatter Graph</h1> ", unsafe_allow_html=True)
    fig = plt.figure()
    plt.scatter(scatter_x, scatter_x**2, marker='x')
    st.write(fig)
elif option == "Bar":
    st.markdown("<h1 style='text-align: center;'>Bar Graph</h1> ", unsafe_allow_html=True)
    fig = plt.figure()
    plt.bar(bar_x, bar_x**4)
    st.write(fig)
elif option == "H_Bar":
    st.markdown("<h1 style='text-align: center;'>Horizontal Bar Graph</h1> ", unsafe_allow_html=True)
    fig = plt.figure()
    plt.barh(bar_x, bar_x**4)
    st.write(fig)
elif option == "Histogram":
    st.markdown("<h1 style='text-align: center;'>Histogram</h1> ", unsafe_allow_html=True)
    fig = plt.figure()
    plt.hist(hist_x)
    st.write(fig)
