import streamlit as st
import pandas as pd
import base64
import geocoder
import matplotlib.pyplot as plt
import seaborn as sns
import requests 

import numpy as np

st.title('All in One Application')


st.sidebar.header('User Input Features')

# g = geocoder.ip('me')

# latitude = g.latlng[0]
# longitude = g.latlng[1]


url = 'http://numbersapi.com/random/year'

st.markdown('''**Here is a fun fact about a random number**''')
random= st.button('learn about a random number', key="1")
if random:
    st.write(requests.get(url).text)


url2 = 'http://numbersapi.com/random/year'

st.markdown('''**Here is a fun fact about a number of your choosing**''')

num = st.text_input('Please enter a number you wish to learn about')

number = st.button('Learn about',key="2")
if number:
    st.write(requests.get(f'http://numbersapi.com/{num}/trivia').text)





