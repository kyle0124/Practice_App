import streamlit as st

# widget : button

def sample(*args) :
    result = 0
    for x in args :
        result += x
    st.write('Result : ', result)

st.button('Click_1', key=1)
st.button('Click_2', key=2, help='This is :violet[Tooltip]')
st.button('CLick_3', key=3, on_click=sample, args=[1, 2, 3, 4, 5])
x = st.button('Click_x', key=4)

if x :
    st.write(':smile:')
else :
    st.write(':sleepy:')

''
'---'
''

# Widget : checkbox
st.checkbox('I agree')

''
'---'
''

# Widget : radio
y = st.radio('Select', ['rice', 'noodle'])
st.write('Radio', y)

# Widget : selectbox
z = st.selectbox('Select', ['rice', 'noodle'])
st.write('SelectBox', z)

# Widget : multiselect
w = st.multiselect('Select', ['tiramisu', 'icecream', 'salad', 'coffee', 'tea'])
st.write('MultiSelect', w)

# Widget : color_picker
c = st.color_picker('Select Color')
st.write('Color_Picker', c)












