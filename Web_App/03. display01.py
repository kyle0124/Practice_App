import streamlit as st
import pandas as pd

sample = {'Column_1' : [11, 22, 33],
          'Column_2' : ['aa', 'bb', 'cc'],
          'Column_3' : [True, False, True]}

df = pd.DataFrame(data=sample)

st.write(df)
st.dataframe(df)
st.table(df)

# Magic command

''
'----'
''



# JSON

dictionary = {'name' : 'Erling Haaland',
              'age' : 23,
              'gender' : 'male'}

st.json(dictionary)



''
'----'
''

# metric

st.metric(label='temperature', value='10 ºC', delta='2 ºC')
st.metric(label='samsung', value='61,900', delta='-300')


















