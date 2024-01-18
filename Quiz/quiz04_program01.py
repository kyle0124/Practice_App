import FinanaceDataReader as fdr
import mplfinance as mpf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

code = '005930'

start = (datetime.today() - timedelta(days=30)).date()
end = datetime.today().date()


# 캔들차트를 출력해 본다 (이동평균 없이).
chart_style = 'default'                                             # 'default', 'binance', 'classic', 'yahoo', 등 중에서 선택.
marketcolors = mpf.make_marketcolors(up='red', down='blue')         # 양봉/음봉 선택.
mpf_style = mpf.make_mpf_style(base_mpf_style=chart_style, marketcolors=marketcolors)

fig, ax = mpf.plot(
    data=df,                            # 받아온 데이터.      
    volume=False,                       # True 또는 False.                   
    type='candle',                      # 캔들 차트.
    style=mpf_style,                    # 위에서 정의.
    figsize=(10,7),
    fontscale=1.1,
    returnfig=True                      # Figure 객체 반환.
)

#
# 여기에서 예측선을 추가한다.
#

n = len(df)                 # 시계열의 길이.
pred_ndays = 10             # 미래 예측 기간.

# 그래프 출력에 유리한 형태로 데이터프레임 변환.
ser = df['Close'].reset_index(drop=True)      # Pandas의 Series 객체.

# ES 모델생성 및 학습.
model = ExponentialSmoothing(ser, trend='add', seasonal='add', seasonal_periods=5).fit() 

# 예측.
past = ser.iloc[-5:]
predicted = model.predict(start= n, end=n+pred_ndays-1) # 모형 예측.
predicted.rename('Close', inplace=True)                 # Name을 past의 'Close'와 같이 맞추어 준다.

# 과거 데이터와 예측을 이어붙인다.
joined = pd.concat([past, predicted],axis=0) 

# Axis에 추가.
ax[0].plot(joined, color = 'aqua', linestyle ='--', linewidth=1.5, label = 'ES')
ax[0].legend(loc='best')  

#print(ser.head())
#print(ser.tail())
#print(past)
#print(predicted)
#print(joined)

#
# 이제는 모든 것을 출력한다.
#

plt.show()



























