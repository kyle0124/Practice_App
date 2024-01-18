import streamlit as st
import requests
import time
import json
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


# URL 에서 Lottie Json을 받아오는 함수
def load_lottieurl(url) :
    response = requests.get(url)
    if response.status_code != 200 :
        return None
    return response.json()


# Local에서 Lottie Json을 읽어오는 함수
def load_lottielocal(path) :
    f = open(path, 'r')
    response = json.load(f)
    f.close()
    return response

# 다음 사이트에서 무료 Lottie animation URL을 가져올 수 있다.
# json 형태로 다운도 가능
# https://lottiefiles.com/featured

url1 = 'https://assets8.lottiefiles.com/packages/lf20_fWd36IjnsR.json'
url2 = 'https://assets4.lottiefiles.com/packages/lf20_fL5QbCnATl.json'

json1 = load_lottieurl(url1)
json2 = load_lottieurl(url2)
json3 = load_lottielocal('./rocket_launch.json')

# Lottie 삽입

st_lottie(json1, speed=3, loop=True, width=400, height=400)


# Lottie Spinner
if st.button('Start') :
    with st_lottie_spinner(json2, speed=3, loop=True) :
        time.sleep(5)
    st.balloons()





# 참고 사이트
# https://pypi.org/project/streamlit-lottie/
# https://github.com/andfanilo/streamlit-lottie



















