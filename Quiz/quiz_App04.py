import streamlit as st
import FinanceDataReader as fdr
import mplfinance as mpf
import json
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
from datetime import datetime, timedelta
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.linear_model import LinearRegression
import warnings
import pandas as pd
warnings.filterwarnings('ignore')

####################################################################################################

if 'market_name' not in st.session_state :
    st.session_state['market_name'] = 'KOSPI'

if 'code' not in st.session_state :
    st.session_state['code'] = 0

if 'days' not in st.session_state :
    st.session_state['days'] = 30

if 'volume' not in st.session_state :
    st.session_state['volume'] = False

if 'chart_style' not in st.session_state :
    st.session_state['chart_style'] = 'default'

if 'pred_days' not in st.session_state :
    st.session_state['pred_days'] = 10

if 'algorithm' not in st.session_state :
    st.session_state['algorithm'] = 'None'

####################################################################################################

def LoadJson(path) :
    f = open(path, 'r')
    result = json.load(f)
    return result

@st.cache_data
def getNames(market_name) :
    df = fdr.StockListing(market=market_name)
    df.rename(columns={'Symbol':'Code'}, inplace=True)
    if 'Market' not in df.columns :
        df['Market'] = market_name
    return df[['Code', 'Name', 'Market']]

@st.cache_data
def getStockData(code, start_date, end_date) :
    df = fdr.DataReader(code, start_date, end_date)
    if 'Change' in df.columns :
        df.drop(columns='Change', inplace=True)
    return df

def plotChart(data, pred_days, algorithm) :
    #algorithm = st.session_state['algorithm']
    chart_title = name_list[st.session_state['code']]
    chart_style = st.session_state['chart_style']
    market_colors = mpf.make_marketcolors(up='red', down='blue')
    mpf_style = mpf.make_mpf_style(base_mpf_style=chart_style, marketcolors=market_colors)

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
    st.markdown(f'<h3 style="text-align: center; color: red;">{chart_title}</h3>', unsafe_allow_html=True)
    if algorithm == 'AR(5)' :
        Ar5_predict(data, ax[0], pred_days)
    elif algorithm == 'ES' :
        Es_predict(data, ax[0], pred_days)
    elif algorithm == 'Both' :
        Ar5_predict(data, ax[0], pred_days)
        Es_predict(data, ax[0], pred_days)

    body.pyplot(fig)
    

def Ar5_predict(df, ax, pred_days) :
    
    df_ar = df.copy()
    ar_num = len(df_ar)
    df_ar = df_ar[['Close']]
    df_ar.reset_index(drop=True, inplace=True)
    num_list = [f'm{x+1}' for x in range(5)]
    for i in range(5) :
        df_ar[num_list[i]] = df_ar['Close'].shift(i+1)
    # df_ar['m1'] = df_ar['Close'].shift(1)                    # t-1 값.
    # df_ar['m2'] = df_ar['Close'].shift(2)                    # t-2 값.
    # df_ar['m3'] = df_ar['Close'].shift(3)                    # t-3 값.
    # df_ar['m4'] = df_ar['Close'].shift(4)                    # t-4 값.
    # df_ar['m5'] = df_ar['Close'].shift(5)

    df_ar = df_ar.iloc[5:]
    X = df_ar.drop(columns='Close')
    y = df_ar['Close']
    model = LinearRegression()
    model.fit(X, y)

    sr = df_ar['Close'][-5:]
    for step in range(pred_days) :
        past = pd.DataFrame(data={f'm{i}' : [sr.iloc[-i]] for i in range(1, 6)})
        pred = model.predict(past)[0]
        sr = pd.concat([sr, pd.Series({ar_num + step : pred})])
    


    ax.plot(sr, color = 'red', linestyle ='--', linewidth=1.5, label = 'AR(5)')
    ax.legend(loc='best') 
    print(sr)

def Es_predict(df, ax, pred_days) :
    df_es = df.copy()
    es_num = len(df_es)
    sr = df_es['Close'].reset_index(drop=True)
    model = ExponentialSmoothing(sr, trend='add', seasonal='add', seasonal_periods=5).fit()
    past = sr.iloc[-5:]
    pred = model.predict(start=es_num, end=es_num + pred_days - 1)
    pred.rename('Close', inplace=True)
    joined = pd.concat([past, pred], axis=0)
    
    ax.plot(joined, color='aqua', linestyle='--', linewidth=1.5, label='ES')
    ax.legend(loc='best')
    print(joined)


    
####################################################################################################

col1, col2 = st.columns([1, 3])
with col1 :
    lottie = LoadJson('lottie-stock-candle-loading.json')
    ''
    st_lottie(lottie, loop=True, speed=1, width=200, height=200)


with col2 :
    ''
    ''
    st.title('Regression for Stock')
    st.markdown("""
        <style>
        .custom-font {
        font-size:20px !important;
        float: right;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown('<p class="custom-font">by using AR/ES</p>', unsafe_allow_html=True)

####################################################################################################
    
with st.sidebar.form(key='setting_market', clear_on_submit=False) :
    st.header('Chart Setting')


    market_list = ['KRX', 'KOSPI', 'KOSDAQ', 'KONEX', 'KRX-MARCAP', 
                   'KRX-DESC', 'KOSPI-DESC', 'KOSDAQ-DESC', 'KONEX-DESC',
                   'KRX-DELISTING', 'KRX-ADMINISTRATIVE', 'KRX-MARCAP',
                   'NASDAQ', 'NYSE', 'AMEX', 'SSE', 'SZSE', 'HKEX', 'TSE',
                    'HOSE', 'S&P500', 'ETF/KR']

    market_name = st.selectbox(label='Select Market', 
                                options=market_list, 
                                index=market_list.index(st.session_state['market_name']))

    if st.form_submit_button('Submit') :
        st.session_state['market_name'] = market_name
        
####################################################################################################

with st.sidebar.form(key='setting', clear_on_submit=False) :
    # st.header('Chart Setting')


    # market_list = ['KRX', 'KOSPI', 'KOSDAQ', 'KONEX', 'KRX-MARCAP', 
    #     'KRX-DESC', 'KOSPI-DESC', 'KOSDAQ-DESC', 'KONEX-DESC',
    #     'KRX-DELISTING', 'KRX-ADMINISTRATIVE', 'KRX-MARCAP',
    #     'NASDAQ', 'NYSE', 'AMEX', 'SSE', 'SZSE', 'HKEX', 'TSE', 'HOSE',
    #     'S&P500', 'ETF/KR']
    
    # market_name = st.selectbox(label='Select Market', 
    #                            options=market_list, 
    #                            index=market_list.index(st.session_state['market_name']))
    # ''
####################################################################################################
    # ''
    names_df = getNames(market_name)
    name_list = zip(names_df['Code'], names_df['Name'], names_df['Market'])
    name_list = [' / '.join(x) for x in name_list]
    code = st.selectbox(label='Select Name', 
                        options=name_list,
                        index=st.session_state['code'])
    #st.write(code)
    code_index = name_list.index(code)
    code = code.split(' / ')[0]
    #st.write(code)
    #st.write(code_index)
    ''
######################################################################################################
    ''
    days = st.slider(
        label='Days',
        min_value=5,
        max_value=365,
        value=st.session_state['days'],
        step=5
    )
    ''
######################################################################################################
    ''
    pred_days = st.slider(
        label='Days for predict',
        min_value=5,
        max_value=15,
        value=st.session_state['pred_days'],
        step=1
    )
    ''
######################################################################################################
    ''
    algorithm_list = ['None', 'AR(5)', 'ES', 'Both']
    algorithm = st.radio(
        'Choose Algorithm',
        algorithm_list
    )
    ''
######################################################################################################
    ''
    chart_styles = ['default', 'binance', 'blueskies', 'brasil', 'charles', 'checkers', 
                   'classic', 'yahoo', 'mike', 'nightclouds', 'sas', 'starsandstripes']
    chart_style = st.selectbox(label='Chart Style', options=chart_styles, 
                               index=chart_styles.index(st.session_state['chart_style']))
    ''
######################################################################################################
    ''
    volume = st.checkbox('거래량', value=st.session_state['volume'])
    ''
######################################################################################################
    ''
    if st.form_submit_button('Submit') :
        #st.session_state['market_name'] = market_name
        st.session_state['code'] = code_index
        st.session_state['days'] = days
        st.session_state['chart_style'] = chart_style
        st.session_state['volume'] = volume
        st.session_state['pred_days'] = pred_days
        st.session_state['algorithm'] = algorithm
        st.experimental_rerun()


######################################################################################################
######################################################################################################
######################################################################################################
        
body = st.empty()


start = (datetime.today() - timedelta(days=30)).date()
end = datetime.today().date()
#st.write(code)
df = getStockData(code, start, end)


plotChart(df, st.session_state['pred_days'], st.session_state['algorithm'])

######################################################################################################
















