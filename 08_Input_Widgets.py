import streamlit as st

# title
st.title("Streamlit Input Widgets")

# Button Widget
st.markdown("## Button Widget")
clicked = st.button(label = "Click Me!")
if clicked:
    st.write("Button clicked!")
else:
    st.write("Please click the button")

st.markdown("---")
st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.markdown("---")

# Download Button
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

st.markdown("---")

# Link Button
st.link_button("Go to streamlit gallery", "https://streamlit.io/gallery")

st.markdown("---")

# Toggle Button
on = st.toggle('Activate feature')
if on:
    st.write('Feature activated!')
else:
    st.write('Feature deactivated!')
off = st.toggle('Deactivate feature')
if off:
    st.write('Feature activated!')
else:
    st.write('Feature deactivated!')

# Checkbox Widget
clicked = st.checkbox("I agree")
if clicked:
    #st.write("You agreed.")
    st.markdown("You agreed.")
else:
    #st.write("You must agree to continue.")
    st.warning("You must agree to continue.")
st.markdown("---")

# Radio Button Widget
radio = st.radio("Choose one", ["Option 1", "Option 2", "Option 3"])
if radio == "Option 1":
    st.write("You chose Option 1.")
elif radio == "Option 2":
    st.write("You chose Option 2.")
elif radio == "Option 3":
    st.write("You chose Option 3.")

st.markdown("---")

# Selectbox Widget
selectbox = st.selectbox("Choose one", ["Option 1", "Option 2", "Option 3"])
if selectbox == "Option 1":
    st.write("You chose Option 1.")
elif selectbox == "Option 2":
    st.write("You chose Option 2.")
elif selectbox == "Option 3":
    st.write("You chose Option 3.")

st.markdown("---")

# Multiselect Widget
multiselect = st.multiselect("Choose one or more", ["Option 1", "Option 2", "Option 3"])
if "Option 1" in multiselect:
    st.write("You chose Option 1.")
elif "Option 2" in multiselect:
    st.write("You chose Option 2.")
elif "Option 3" in multiselect:
    st.write("You chose Option 3.")

st.markdown("---")

# Slider Widget
slider = st.slider("Choose a number", 0, 10)
st.write(slider)

st.markdown("---")

# Text Input Widget
text_input = st.text_input("Enter something")
st.write(text_input)

st.markdown("---")

# Text Area Widget
text_area = st.text_area("Enter something")
st.write(text_area)

st.markdown("---")

# Date Input Widget
date_input = st.date_input("Choose a date")
st.write(date_input)

st.markdown("---")

# Time Input Widget
time_input = st.time_input("Choose a time")
st.write(time_input)

st.markdown("---")

# Color Input Widget
color_input = st.color_picker("Choose a color")
st.write(color_input)

st.markdown("---")

# File Input Widget
file_input = st.file_uploader("Choose a file")
st.write(file_input)

st.markdown("---")

# Image Input Widget
image_input = st.file_uploader("Choose an image file")
if image_input is not None:
    st.image(image_input)
else:
    st.write("No image selected")

st.markdown("---")

# Video Input Widget
video_input = st.file_uploader("Choose a video file", type=["mp4", "avi"])
if video_input is not None:
    st.video(video_input)
else:
    st.write("No video selected")

st.markdown("---")

# Audio Input Widget
audio_input = st.file_uploader("Choose an audio file", type=["mp3", "wav"])
if audio_input is not None:
    st.audio(audio_input)
else:
    st.write("No audio selected")

st.markdown("---")

# Selector Slider
color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

st.markdown("---")

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)

st.markdown("---")

# Number Input
number = st.number_input('Insert a number', value=0)
st.write('The number is', number)

st.markdown("---")

number = st.number_input('Insert a number', min_value=-15, max_value=10)
st.write('The number is', number)

st.markdown("---")

number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
st.write('The current number is ', number)

st.markdown("---")

# Camera Input
#picture = st.camera_input("Take a picture")

#if picture:
#    st.image(picture)

#st.markdown("---")

# Progress Bar
import time

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.button("Progress Bar")

st.markdown("---")
# another example for progress bar
pro_bar = st.progress(0)
for i in range(10):
    pro_bar.progress(i + 1)


st.markdown("---")

