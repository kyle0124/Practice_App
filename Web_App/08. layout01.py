import streamlit as st


# Layout : Sidebar 
# 1
st.sidebar.title('Title')
st.sidebar.header('Header')
st.sidebar.subheader('Subheader')
st.sidebar.write('''

---

''')


x = st.sidebar.selectbox('Select', ['Rice', 'Noodle'])
st.sidebar.write('SelcetBox : ', x)
st.sidebar.write('''

---

''')

c = st.sidebar.color_picker('Select Color')
st.sidebar.write('Color_picker : ', c)
st.sidebar.write('''

---

''')

# 2
# with st.sidebar :
#     st.title('Title')
#     st.header('Header')
#     st.subheader('Subheader')
#     ''
#     '---'
#     ''


#     x = st.selectbox('Select', ['Rice', 'Noodle'])
#     st.write('Selectbox : ', x)
#     ''
#     '---'
#     ''


#     c = st.color_picker('Select Color')
#     st.write('Color_picker : ', c)

# Layout : Column

col1, col2, col3 = st.columns(3)       # 3등분

with col1 :
    st.header(':red[Column_1]')
    st.image('https://static.streamlit.io/examples/cat.jpg')

with col2 :
    st.header(':blue[Column_2]')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with col3 :
    st.header(':green[Column_3]')
    st.image('https://static.streamlit.io/examples/owl.jpg')

''
'---'
''

col1, col2, col3 = st.columns([2, 6, 2])       # 비율로 분할

with col1 :
    st.header(':red[Column_1]')
    st.image('https://static.streamlit.io/examples/cat.jpg')

with col2 :
    st.header(':blue[Column_2]')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with col3 :
    st.header(':green[Column_3]')
    st.image('https://static.streamlit.io/examples/owl.jpg')

''
'---'
''

# Layout : Tabs

tab1, tab2, tab3 = st.tabs(['Cats', 'Dogs', 'Owls'])

with tab1 : 
    st.header('This is cat')
    st.image('https://static.streamlit.io/examples/cat.jpg')

with tab2 : 
    st.header('This is dog')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with tab3 : 
    st.header('This is owl')
    st.image('https://static.streamlit.io/examples/owl.jpg')

''
'---'
''

# Layout : Columns + Tabs


with tab1 : 
    col1, col2, col3 = st.columns(3)

    with col1 :
        st.header('This is cat')
        st.image('https://static.streamlit.io/examples/cat.jpg')

    with col2 :
        st.header('This is dog')
        st.image('https://static.streamlit.io/examples/dog.jpg')
    
    with col3 :
        st.header('This is owl')
        st.image('https://static.streamlit.io/examples/owl.jpg')

with tab2 : 
    col1, col2, col3 = st.columns([1, 1, 3])

    with col1 :
        st.header('This is cat')
        st.image('https://static.streamlit.io/examples/cat.jpg')

    with col2 :
        st.header('This is dog')
        st.image('https://static.streamlit.io/examples/dog.jpg')
    
    with col3 :
        st.header('This is owl')
        st.image('https://static.streamlit.io/examples/owl.jpg')












