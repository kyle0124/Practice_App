import streamlit as st
import streamlit.components.v1 as components

# Bootstrap 4의 collapse 예시.
# 참고: https://getbootstrap.com/docs/4.0/getting-started/introduction/


components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion">
      <div class="card">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Collapsible Group Item #1
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #1 content
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Collapsible Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            Collapsible Group Item #2 content
          </div>
        </div>
      </div>
    </div>
    """,
    height=200,
)

style = '''
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.egzxvld4 > div:nth-child(1) > div > div:nth-child(6) > div > div > p {color: red; font-weight:bolder; }

#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.egzxvld4 > div:nth-child(1) > div > div:nth-child(7) > div > div > p {color:blue; font-weight:bolder;}

.stMarkdown p { color: blue;  } 

#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.egzxvld4 > div:nth-child(1) > div > div:nth-child(8) > div > div > p {color:green; font-weight:bolder;}
'''



st.markdown('<style>{}</style>'.format(style), unsafe_allow_html=True)

st.button('One', key='one')
st.button('Two', key='two')
st.button('Three', key='three')

e1 = st.empty()
e2 = st.empty()
e3 = st.empty()


e1.write('Hello!')
e2.write('World!')
e3.write('Streamlit!')

with st.form(key='Form', clear_on_submit=False) :
    name = st.text_input('Input Name')
    age = st.slider('Select Age', 10, 90, 40)
    gender = st.radio('Select Gender', ['Male', 'Female'])
    submit = st.form_submit_button('Submit')



















