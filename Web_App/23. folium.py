import streamlit as st
from streamlit_folium import st_folium
import folium

import numpy as np

lat0 = 37.56668              # 서울 시청 위도.
lon0 = 126.9784              # 서울 시청 경도.

myMap = folium.Map(location=[lat0, lon0], zoom_start=10)

# Random Seed
if 'seed' not in st.session_state :
    st.session_state['seed'] = 1

if st.button('Reset') :
    st.session_state['seed'] += 1


# Create Random Marker

@st.cache_data
def randomCoords(n, lat, lon, seed=1234) :
    np.random.seed(seed)
    coords = []
    for _ in range(n) :
        coords.append([lat + np.random.randn()/20, lon + np.random.randn()/20])
    return coords


# Add Marker
for lat, lon in randomCoords(20, lat0, lon0, st.session_state['seed']) :
    marker = folium.Marker(location=[lat, lon],
                           icon=folium.Icon(color='green', icon='star'))
    myMap.add_child(marker)
    marker.add_to(myMap)    


# print map

st_folium(myMap, width=500, height=500)




























