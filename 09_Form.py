import streamlit as st

# title
st.title("Streamlit Form")

# Form
with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")

st.markdown("---")

# Double Slider
form = st.form("my_nested_form")
form.slider("Inside the form")
st.slider("Outside the form")

# Now add a submit button to the form:
form.form_submit_button("Submit")

st.markdown("---")

# Form with multiple inputs
st.markdown("<h1>User Registration</h1>", unsafe_allow_html=True)
form = st.form("form1")
name = form.text_input("Username")
email = form.text_input("Email")
password =form.text_input("Password", type="password")
c_password =form.text_input("Confirm Password", type="password")
day, month, year = form.columns(3)
day.text_input("Day")
month.text_input("Month")
year.text_input("Year")
state = form.form_submit_button("Register")
#if state:
#    if name == "" and email == "":
#        form.warning("Please fill all the fields")
#    else:
#        form.success("All fields are filled")

st.markdown("---")

# Form with multiple inputs and columns
st.markdown("<h1 style='text-align: center;'>User Registration Form</h1>", unsafe_allow_html=True)
with st.form("form2"):
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Username")
    with col2:
        st.text_input("Email")
    st.text_input("Password", type="password")
    st.text_input("Confirm Password", type="password")
    st.form_submit_button("Register")

st.markdown("---")

# Form with multiple inputs and columns - 3 columns

with st.form("form3"):
    col1, col2, col3 = st.columns(3)
    col1.text_input("Username") # col1.st.text_input("Username")
    col2.text_input("Email") # col2.st.text_input("Email")
    col3.text_input("Password", type="password") # col3.st.text_input("Password(): # col3.st.text_input("Password", type="password")
    st.form_submit_button("Register")

st.markdown("---")