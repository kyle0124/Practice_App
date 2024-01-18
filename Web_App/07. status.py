import streamlit as st
import time

st.progress(value=30)


''
'---'
''

# 특수효과
# st.ballons()
# st.snow()


# status
st.error('Error Message', icon='😰')
st.warning('Warning Message', icon='⚠️')
st.info('Info Message', icon='ℹ')
st.success('Success', icon='😊')

''
'---'
''


# Spinner
with st.spinner(text='Loading...') :
    time.sleep(3)
    st.success('Finish!', icon='😊')






















