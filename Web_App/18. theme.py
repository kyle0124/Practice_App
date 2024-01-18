# 필요한 라이브러리를 불러온다.
import streamlit as st

# 위젯 다수와 Sidebar를 적용해 본다.
x1 = st.button( '클릭~', key = 1 )       

x2 = st.checkbox( '위 내용에 동의합니다!' )

x3 = st.radio( '다음 중 한가지 선택' , [ '부먹', '찍먹'] )

x4 = st.slider( '만족도 점수는?', min_value = 0, max_value = 10, value = 5, step = 1)

x5 = st.text_input( '당신의 이름은?' )

st.sidebar.title('사이드바 타이틀')
