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
import random

st.set_page_config(layout="wide")
st.title('All in One Application')


# st.sidebar.header('User Input Features')

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

st.markdown('''**Move the slider to see an art piece** ''')

art_number = st.slider('Art Number', 1, 4000)
def SelectArt(art_id):
    art_id = str(art_id)
    art_url= f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{art_id}'

    art = requests.get(art_url).json()


    if not art['objectID']:
        st.error("Sorry Art Work with this ID is available")

    else:
        art_image = art['primaryImage']
        art_title = art['title']
        art_department = art['department']
        artist = art['artistDisplayName']
        art_culture = art['culture']

        if art_image:
            if art_image:
                st.image(
                            art_image,
                            width=300, # Manually Adjust the width of the image as per requirement
                        )
            if art_title: st.write('Title: ' +art_title)
            else: st.write('Title Unknown ')
            if art_department: st.write('Department: ' + art_department)
            else: st.write('Department Unknown ')
            if artist: st.write('Artist: ' + artist)
            else: st.write('Artist Unknown ')
            if art_culture: st.write('Culture: ' + art_culture) 
            else: st.write('Culture Unknown ')
        elif not art_image:
            st.error("Sorry no image available")
    
if art_number:
    SelectArt(art_number)

st.header('Search For An Art Work')
art_word = st.text_input("Enter a word of an art you would like to see")
search_art_url = f'https://collectionapi.metmuseum.org/public/collection/v1/search?q={art_word}'


# html_temp ='''
# <div style="width:80%">{gallery}</div>

# '''

# st.markdown(html_temp.format(), unsafe_allow_html=True)
if art_word:
    art_search_request = requests.get(search_art_url).json()
    total_art_pieces = art_search_request['total']

    searched_art_list = [] #ids of all the art from search 
    total_art_pieces
    for k,v in art_search_request.items():
        if v not in searched_art_list:
            searched_art_list.append(v)


    col1, col2, col3 = st.beta_columns(3)
    

    # ArtPieces(3689)
    # @st.cache
    def LearnMore(id):
        learn_more = st.checkbox("Learn More",key=id)
        if learn_more:
                if  art['artistDisplayName']: st.write('Artist: ' + art['artistDisplayName'])
                else: st.write('Artist Unknown ')
                if art['culture']: st.write('Culture: ' + art['culture']) 
                else: st.write('Culture Unknown ')
    
    for i in searched_art_list[1][0:4]:
        art_url= f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{i}'
        art = requests.get(art_url).json()
        art_image = art['primaryImage']
        with col1:
            st.image(art_image,caption=art['title'])
            LearnMore(i)
        
            
    for i in searched_art_list[1][4:7]:
        # art_url= f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{i}'
        art = requests.get(art_url).json()
        art_image = art['primaryImage']

        with col2:
            st.image(art_image,caption=art['title'])
            LearnMore(i)
       
    for i in searched_art_list[1][7:10]:
        # art_url= f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{i}'
        art = requests.get(art_url).json()
        art_image = art['primaryImage']

        with col3:
            st.image(art_image,caption=art['title'])
            LearnMore(i)
            
     
            

            


