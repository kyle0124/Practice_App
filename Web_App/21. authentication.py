import streamlit as st
import streamlit_authenticator as stauth
import yaml
import time


# open Config
with open('config.yaml', 'r', encoding='utf8') as f :
    config = yaml.load(f, Loader=yaml.SafeLoader)

#print(config)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']

)

# Logout / Session out
def forceLogout() :
    authenticator.cookie_manager.delete(authenticator.cookie_name)
    st.session_state['logout'] = True
    st.session_state['name'] = None
    st.session_state['username'] = None
    st.session_state['authentication_status'] = None
    del st.session_state['clickedReset']

def hasClickedReset() :
    if 'clickedReset' in st.session_state.keys() and st.session_state['clickedReset'] :
        return True
    else :
        return False
    

# Login Form

name, status, username = authenticator.login('Login', 'main')

if not status :
    st.error('Incorrect Information, Please check your ID/Password')

if status is None :
    st.warning('Please input ID/Password')

# Success

if status :
    st.sidebar.write('Welcome :blue[{}]!'.format(name))
    st.write('You can use this Web Site :)')
    authenticator.logout('Logout', 'sidebar')

    # Reset password
    if hasClickedReset() :
        try :
            result = authenticator.reset_password(username, 'Reset Password', 'main')
            if result :
                time.sleep(1)
                with open('config.yaml', 'w') as f :
                    config['credentials'] = authenticator['credentials']
                    yaml.dump(config, f, sort_keys=False)
                forceLogout()
                time.sleep(1)
        except Exception as e :
            st.error(e)

    else :
        if st.sidebar.button('Reset Password') :
            st.session_state['clickedReset'] = True
            st.experimental_rerun()

















