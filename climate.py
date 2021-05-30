from requests.api import request
import streamlit as st
import pandas as pd
import base64
import geocoder
import matplotlib.pyplot as plt
import seaborn as sns
import requests 
from PIL import Image
import urllib.request
import numpy as np

st.title('All in One Application')


st.sidebar.header('User Input Features')

url = 'http://numbersapi.com/random/year'

st.header('Here is a fun fact about a random number')
random= st.button('learn about a random number', key="1")
if random:
    st.write(requests.get(url).text)


url2 = 'http://numbersapi.com/random/year'

st.markdown('''**Here is a fun fact about a number of your choosing**''')

num = st.text_input('Please enter a number you wish to learn about')

number = st.button('Learn about',key="2")
if number:
    st.write(requests.get(f'http://numbersapi.com/{num}/trivia').text)



st.write('---------------------------------------------')

st.header('Take a Break with a Funny Joke')

joke_body = requests.get('https://official-joke-api.appspot.com/random_joke').json()

# joke_body

set_up_joke = joke_body['setup']
punch_line = joke_body['punchline']

jokes= st.button('Random Joke', key="3")
if jokes:
    st.write(set_up_joke)
    st.write(punch_line)
    
st.write('---------------------------------------------')

st.header('Enjoy these Art pieces')

art_number = 79
art_url= f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{art_number}'

art = requests.get(art_url).json()

art_image = art['primaryImage']

st.image(
            art_image,
            width=400, # Manually Adjust the width of the image as per requirement
        )