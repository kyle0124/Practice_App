import streamlit as st
import pandas as pd


# Title
st.title('Title - *Big*')
st.header('Title - *Mid*')
st.subheader('Title - *Small*')


# Text
st.text('짧은 길이의 text, *Markdown* 인식 못함')

st.markdown('*Markdown*을 컴파일해서 출력')

st.write('텍스트 또는 다양한 python 변수/객체 출력')

##############################################################

x = 1
y = 2

sample = {'Column_1' : [11, 22, 33],
          'Column_2' : ['aa', 'bb', 'cc'],
          'Column_3' : [True, False, True]}

df = pd.DataFrame(data=sample)

st.write('x = ', x, 'and', 'y = ', y)

# Latex 수식 compile
st.latex('Area = \pi r^2')

# Code
test_code = '''
    total = 0
    for i in range(11) :
        total += i
    print(total)
'''

st.code(test_code)

# Caption
st.caption('Sample Caption')

























