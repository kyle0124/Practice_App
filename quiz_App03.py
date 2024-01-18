import streamlit as st
import json
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
from PIL import Image
import pickle
from wordcloud import WordCloud
import bs4

def loadJson(path) :
    f = open(path, 'r')
    result = json.load(f)
    f.close()
    return result

if 'id' not in st.session_state :
    st.session_state['id'] = ''
 
if 'secret' not in st.session_state :
    st.session_state['secret'] = ''

def getRequest(keyword, amount, start) :
    url = f'https://openapi.naver.com/v1/search/news.json?query={keyword}&display={amount}&start={start}'
    headers = {'X-Naver-Client-Id' : st.session_state['id'],
               'X-Naver-Client-Secret' : st.session_state['secret']}
    response = requests.get(url, headers=headers)
    text = json.loads(response.text)
    return text['items']

@st.cache_data
def cleanText(text) :
    text = re.sub('\d|[a-zA-Z]|\W', ' ', text)
    text = re.sub('\s+', ' ',  text)
    return text


@st.cache_resource
def getTokenizer() :
    f = open('./resources/tokenizer01.model', 'rb')
    tokenizer = pickle.load(f)
    f.close()
    return tokenizer


def makeTable(tokens, nmin=2, nmax=5, ncut=1) :
    tokens_new = []

    for token in tokens :
        if len(token) >= nmin and len(token) <= nmax :
            tokens_new.append(token)
    
    sr = pd.Series(tokens_new)
    sr = sr.value_counts()
    sr = sr[sr >= ncut]
    return dict(sr.sort_values(ascending=False))

def plotChart(count, max_words_, container, back_mask=None) :
    path = './resources/background_'
    img = Image.open(path + '0.png')
    if back_mask == 'circle' :
        img = Image.open(path + '1.png')
    elif back_mask == 'bubble' :
        img = Image.open(path + '2.png')
    elif back_mask == 'heart' :
        img = Image.open(path + '3.png')

    background = np.array(img)

    # word cloud
    wc = WordCloud(font_path='./resources/NanumSquareR.ttf',
                   background_color='white',
                   contour_color='grey', 
                   contour_width=3,
                   max_words=max_words_,
                   mask=background)
    
    wc.generate_from_frequencies(count)
    fig = plt.figure(figsize=(10, 10))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    container.pyplot(fig)







col1, col2 = st.columns([1, 3])
with col1 :
    lottie = loadJson('./resources/lottie-full-movie-experience-including-music-news-video-weather-and-lots-of-entertainment.json')
    st_lottie(lottie, speed=1, width=150, height=150, loop=True)

with col2 :
    ''
    ''
    st.title('WordCloud for NEWS')


with st.sidebar.form(key='s1', clear_on_submit=True) :
    st.header('Set API')

    id = st.text_input('ID : ', value=st.session_state['id'])
    secret = st.text_input('Secret Code : ', value=st.session_state['secret'], type='password')

    if st.form_submit_button(label='Submit') :
        st.session_state['id'] = id
        st.session_state['secret'] = secret
        st.experimental_rerun()


# location for word_cloud
word_cloud = st.empty()

keyword_list = ['경제', '정치', '사회', '국제', '연예', 'IT', '문화']
cloud_type_list = ['None', 'circle', 'bubble', 'heart']

with st.form(key='f1', clear_on_submit=False) :
    keyword = st.selectbox('Keyword', keyword_list)
    amount = st.slider('Amount', min_value=1, max_value=5, step=1, value=2)
    cloud_type = st.radio('type', cloud_type_list)

    if st.form_submit_button('Submit') :
        word_cloud.info('Loading...')
        corpus = ''
        items = []

        for i in range(amount) :
            items.extend(getRequest(keyword, 100, 100 * i + 1))

        # NEWS Crawling
        for i in items :
            if 'n.news.naver' in i['link'] :
                new_url = i['link']
                response = requests.get(new_url, headers={'User-Agent' : 'Mozilla'})
                soup = bs4.BeautifulSoup(response.text, 'html.parser')
                news_tag = soup.select_one('#dic_area')
                if news_tag :
                    corpus += news_tag.text + '\n'
        

        # preprocessing & visualization
        if len(corpus) > 100 :
            word_cloud.info('Loading...')
            corpus = cleanText(corpus)
            tokenizer = getTokenizer()
            #tokens = tokenizer.tokenize(corpus, flatten=True)
            tokens = [t1 for t1, t2 in tokenizer.tokenize(corpus, flatten=False)]           # left token only
            dictionary = makeTable(tokens)
            plotChart(dictionary, 70, word_cloud, cloud_type)

        else :
            word_cloud.error(':red[Not Enough Data]')
        


















