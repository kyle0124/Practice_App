import streamlit_authenticator as stauth

password = ['123', '456']

hashedPassword = stauth.Hasher(password).generate()

print(hashedPassword)







