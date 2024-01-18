import streamlit as st

# Widget : select_slider
x = st.select_slider('만족도', ['매우 불만족', '불만족', '보통', '만족', '매우 만족'])
st.write('만족도 : ', x)

''
'---'
''

# Widget : slider

y = st.slider('만족도', min_value=0, max_value=10, value=5, step=1)
st.write('만족도 : ', y)

''
'---'
''

# Widget : number_input
z = st.number_input('시험 점수', min_value=0, max_value=10, value=10, step=2)
st.write('시험 점수 : ', z)


# Widget : text_input
name = st.text_input('Input name : ')
date = st.date_input('Input Date : ')
time = st.time_input('Input Time : ')
st.write('Name : {0}, Date : {1}, Time : {2}'.format(name, date, time))

























