import streamlit as st
import FinanceDataReader as fdr
import mplfinance as mpf
import json
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
from datetime import datetime, timedelta

def LoadJson(path) :
    f = open(path, 'r')
    response = json.load(f)
    f.close()
    return response

col1, col2 = st.columns([1, 3])
with col1 :
    lottie = LoadJson('lottie-stock-candle-loading.json')
    st_lottie(lottie, speed=1, loop=True, width=150, height=150)

with col2 :
    ''
    ''
    st.title('Visualization of Finance')

kor = ['KOSPI', 'KOSDAQ']


@st.cache_data
def readData(code, start, end) :
    df = fdr.DataReader(code, start, end)
    if 'Change' in df.columns :
        df.drop(columns='Change', inplace=True)
    return df

@st.cache_data
def getNames(market) :
    
#    usa = ['NASDAQ', 'S&P500']
    df = fdr.StockListing(market)
    if market in kor :
        return df.sort_values(by='Marcap', ascending=False)[['Code', 'Name', 'Market']]
    else :
        df['Market'] = market
        df.rename(columns={'Symbol':'Code'}, inplace=True)
        return df[['Code', 'Name', 'Market']]
    



start = (datetime.today() - timedelta(days=30)).date()
end = datetime.today().date()

if 'days' not in st.session_state :
    st.session_state['days'] = 30

if 'code' not in st.session_state :
    st.session_state['code'] = 0

if 'volume' not in st.session_state :
    st.session_state['volume'] = True

if 'chart_style' not in st.session_state :
    st.session_state['chart_style'] = 'default'

if 'market_list' not in st.session_state :
    st.session_state['market_list'] = 'KOSPI'


with st.sidebar.form(key='selectSetting', clear_on_submit=True) :
    st.header('Chart Setting')
    ''
    ''
    market_list = ['KOSPI', 'KOSDAQ', 'NASDAQ', 'S&P500']
    market_kor = ['KOSPI', 'KOSDAQ']
    market_usa = ['NASDAQ', 'S&P500']
    market = st.selectbox(label='Market', options=market_list, 
                          index=market_list.index(st.session_state['market_list']))

    ''
    ''
    names = getNames(market)
    choices = zip(names['Code'], names['Name'], names['Market'])
    choices = [' : '.join(x) for x in choices]
    choice = st.selectbox(label='종목 : ', options=choices, index=st.session_state['code'])
    code_index = choices.index(choice)
    code = choice.split()[0]
    ''
    ''

    days = st.slider(
        label='기간 (days)',
        min_value=5,
        max_value=365,
        value=st.session_state['days'],
        step=1
    )
    ''
    ''
    chart_styles = ['default', 'binance', 'blueskies', 'brasil', 'charles', 'checkers', 
                   'classic', 'yahoo', 'mike', 'nightclouds', 'sas', 'starsandstripes']
    chart_style = st.selectbox(label='Chart Style', options=chart_styles, 
                               index=chart_styles.index(st.session_state['chart_style']))
    ''
    ''
    volume = st.checkbox('거래량', value=st.session_state['volume'])
    ''
    ''
    if st.form_submit_button(label='OK') :
        st.session_state['market_list'] = market
        st.session_state['days'] = days
        st.session_state['code'] = code_index
        st.session_state['chart_style'] = chart_style
        st.session_state['volume'] = volume
        st.experimental_rerun()


# Candle Chart

def plotChart(data) :
    chart_style = st.session_state['chart_style']
    marketcolors = mpf.make_marketcolors(up='red', down='blue')
    mpf_style = mpf.make_mpf_style(base_mpf_style=chart_style, marketcolors=marketcolors)

    fig, ax = mpf.plot(
        data,
        volume=st.session_state['volume'],
        type='candle',
        style=mpf_style,
        figsize=(10, 7),
        fontscale=1.1,
        mav=(5,10,30),
        mavcolors=('red', 'green', 'blue'),
        returnfig=True

    )
    st.pyplot(fig)

# Plot Data

start = (datetime.today() - timedelta(days=st.session_state['days'])).date()
end = (datetime.today()).date()
df = readData(code, start, end)
chart_title = choices[st.session_state['code']]
st.markdown(f'<h3 style="text-align: center; color: red;">{chart_title}</h3>', unsafe_allow_html=True)
plotChart(df)
''
''
st.write('##### 이동평균선: :red[5일] , :green[10일], :blue[30일].')


























