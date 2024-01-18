import streamlit as st
from streamlit_option_menu import option_menu



# Create Navigation Menu
# Icon names : https://icons.getbootstrap.com/


with st.sidebar :
    choice1 = option_menu(menu_title='Main', 
                          menu_icon='list',
                          options=['Home', 'Save', 'Settings'],
                          icons=['house', 'device-hdd', 'gear'],
                          orientation='vertical',
                          default_index=0)
    'Select : ', choice1

choice2 = option_menu(menu_title=None,
                      menu_icon=None,
                      options=['Home', 'Save', 'Contact'],
                      icons=['house', 'device-hdd', 'people'],
                      orientation='horizontal',
                      default_index=0,
                      styles={ 
                            "container": {"padding": "0", "background-color": "#fafafa"},
                            "icon": {"color": "green", "font-size": "25px"}, 
                            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "gray"},
                            }              
                      )

'Select : ', choice2


# 참고 사이트
# https://github.com/victoryhb/streamlit-option-menu















