import streamlit as st

import time

# Expander

x = st.expander('Example 1')
x.write('Dogs')
x.image('https://static.streamlit.io/examples/dog.jpg', width=200)
''

with st.expander('Example 2') :
    st.write('Cats')
    st.image('https://static.streamlit.io/examples/cat.jpg', width=200)

''
'---'
''


# Empty

y = st.empty()
y.write('Click ***Start***')

c1, c2, c3 = st.columns([1, 1, 5])
start = c1.button('Start', key=1)
clear = c2.button('Clear', key=2)
c3.button('Reset', key=3)

if start :
    with y :
        for i in range(6) :
            t =  5 - i
            if t == 1 :
                st.write('Count Down : {0} second'.format(t))
            else : 
                st.write('Count Down : {0} seconds'.format(t))
            time.sleep(1)

if clear :
    y.empty()

''
'---'
''


# Container

z = st.container()
z.write('Click ***Start***')

d1, d2, d3 = st.columns([1, 1, 5])
start_ = d1.button('Start', key=4)
clear_ = d2.button('Clear', key=5)
d3.button('Reset', key=6)

if start_ :
    with z :
        for i in range(6) :
            t = 5 - i
            if t == 1 :
                st.write('Count Down : {0} second'.format(t))
            else :
                st.write('Count Down : {0} seconds'.format(t))

            time.sleep(1)

if clear_ :
    z.empty()



























