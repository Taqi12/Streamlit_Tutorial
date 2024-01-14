import streamlit as st

# title
st.title("Streamlit Image")

# Image from url
st.image("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")

st.markdown("---")

# Image - 3 columns
col1, col2, col3 = st.columns(3)
col1.image("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")
col2.image("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")
col3.image("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")

st.markdown("---")

# Image from personal PC
st.image("resources/img1.jpeg", width=300, caption="Flower")
st.image("resources/img2.jpeg", width=500, caption="Tree")
st.image("resources/img3.jpeg", width=700, caption="Watches")

# images in 3 columns
col1, col2, col3 = st.columns(3)
col1.image("resources/img1.jpeg")
col2.image("resources/img2.jpeg")
col3.image("resources/img3.jpeg", caption="Watches")

st.markdown("---")

# Another way of displaying images
from PIL import Image
img = Image.open("resources/img1.jpeg")
st.image(img, width=300, caption="Flower")

# Audio

st.audio("resources/audio1.mp3")

st.audio("resources/audio2.mp3")

# Another way of displaying audio
audio_file = open("resources/audio1.mp3", "rb").read()
st.audio(audio_file, format="audio/mp3")

# Video

st.video("resources/video1.mp4")

st.video("resources/video2.mp4")

# Another way of displaying videos
video_file = open("resources/video1.mp4", "rb").read()
st.video(video_file)

