import streamlit as st
import pandas as pd
import time
from sklearn.neighbors import KNeighborsClassifier


@st.cache_resource
def initML() :
    df = pd.read_csv('../data_web/data_train.csv')
    X = df.drop(columns='19').values.astype('float32')
    y = df[['19']].values.astype('float32')

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X, y)
    time.sleep(5)
    return knn

if st.button('Run', key=1) :
    knn = initML()
    st.write('Success')

if st.button('Clear Cache', key=2) :
    initML().clear()
    st.cache_resource.clear()





    