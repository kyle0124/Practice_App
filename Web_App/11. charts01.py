import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = np.random.randn(30, 3)
df = pd.DataFrame(data=data, columns=['a', 'b', 'c'])

'Head of Dataframe : ', df.head()

# Streamlit Chart
# 1. Line chart

'line_chart'
st.line_chart(df)

# 2. Area chart

'area_chart'
st.area_chart(df)

# 3. Bar chart

'bar_chart'
st.bar_chart(df)


# Load Data

df = pd.read_csv('../data_web/data_iris.csv')
'Data : ', df.head()
''
''


# 1. Matplotlib
counts = df['Species'].value_counts()

fig1 = plt.figure(figsize=(7, 5))
plt.bar(x=counts.index, height=counts.values, color='orange')
plt.ylabel('Counts')
plt.title('Iris Flower Species Counts - 1')
st.pyplot(fig1)
''
''

# 2. Axes

fig2 = plt.figure(figsize=(7, 5))
ax2 = fig2.add_axes([0, 0, 1, 1])               # Left, Bottom, Width, Height
ax2.bar(x=counts.index, height=counts.values, color='green')
ax2.set_ylabel('Counts')
ax2.set_title('Iris Flower Sepcies Counts - 2')
st.pyplot(fig2)
''
''


# 3. Seaborn
fig3 = plt.figure(figsize=(7, 5))
sns.countplot(data=df, x='Species', hue='Species', palette='muted')
plt.legend(loc='lower right')
st.pyplot(fig3)
''
''

# 4. Seaborn ver2
fig4, ax4 = plt.subplots()
sns.countplot(data=df, x='Species', hue='Species', ax=ax4)
plt.legend(loc='lower right')
st.pyplot(fig4)








