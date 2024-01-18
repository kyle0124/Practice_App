import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np


_, col, _ = st.columns([2, 6, 2])           # Centerizing
col.header('Streamlit Visualization')
''


# Load Data

df = sns.load_dataset('iris')
colors = {'setosa' : 'red', 
          'virginica' : 'green', 
          'versicolor' : 'blue'}

# Input by sidebar
with st.sidebar :
    x = st.selectbox('Select X', ["sepal_length", "sepal_width", "petal_length", "petal_width"])
    ''
    y = st.selectbox('Select Y', ["sepal_length", "sepal_width", "petal_length", "petal_width"])
    ''
    species = st.multiselect('Select type(:violet[Multi])', ['setosa', 'virginica', 'versicolor'])
    ''
    alpha = st.slider('Set Alpha', 0.1, 1.0, 0.5)


# Visualization
if species :
    fig = plt.figure(figsize=(7, 5))
    for sp in species :
        df_mod = df[df['species'] == sp]
        plt.scatter(x=df_mod[x], y=df_mod[y], color=colors[sp], alpha=alpha, label=sp)
    plt.legend(loc='lower right')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title('Iris Scatter Plot')
    st.pyplot(fig)
else :
    st.warning('Choose type of iris!')




















