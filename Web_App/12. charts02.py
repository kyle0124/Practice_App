import streamlit as st
import numpy as np

data = {'lat':[37.56668], 'lon':[126.9784]}  

# Add Random location (100)

for _ in range(100) :
    data['lat'].append(data['lat'][0] + np.random.randn() / 50)
    data['lon'].append(data['lon'][0] + np.random.randn() / 50)


# Map
st.map(data=data, zoom=10)
st.button('Reset')







