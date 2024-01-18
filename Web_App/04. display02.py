import streamlit as st
import pandas as pd

st.write('Image')
st.image('../data_web/Kawi.png', width=200)

# Magic Command

''
'---'
''

# Audio

with open('../data_web/clock-bells-hour-signal.wav', 'rb') as f :
    audio = f.read()

st.write('Bells')
st.audio(audio, format='audio/wav')

''
'---'
''

# Video

with open('../data_web/video.mov', 'rb') as f :
    video = f.read()

st.write('Video')
st.video(video)











