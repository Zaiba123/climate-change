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



art_number = st.slider('Art Number', 1, 4000)

art_url= f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{art_number}'

art = requests.get(art_url).json()
# art_image = ''

art_objectid = art['objectID']

if art_objectid:
    art_image = art['primaryImage']
    art_title = art['title']
    art_department = art['department']
    artist = art['artistDisplayName']
    art_culture = art['culture']
    art_highlight = art['isPublicDomain']



st.write(art_highlight)
st.write(art_objectid)
# art_image
if art['objectID']:
    if art_image:
        st.image(
                    art_image,
                    width=400, # Manually Adjust the width of the image as per requirement
                )
    if art_title: st.write('Title: ' +art_title)
    if art_department: st.write('Department: ' + art_department)
    if artist: st.write('Artist: ' + artist)
    if art_culture: st.write('Culture: ' + art_culture)

elif not art['objectID']:
    st.error("Sorry no image available")



st.header('Search For An Art Work')
art_word = st.text_input("Enter a word of an art you would like to see")
search_art_url = f'https://collectionapi.metmuseum.org/public/collection/v1/search?q={art_word}'

art_search_request = requests.get(search_art_url).json()
total_art_pieces = art_search_request['total']

searched_art_list = [] #ids of all the art from search 
# art_search_request
total_art_pieces
# art_search_request[1][5]
for k,v in art_search_request.items():
    #print(k,v)
    searched_art_list.append(v)


def SelectArt(art_id):
    art_url= f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{art_id}'

    art = requests.get(art_url).json()
    # art_image = ''

    art_objectid = art['objectID']

    if art_objectid:
        art_image = art['primaryImage']
        art_title = art['title']
        art_department = art['department']
        artist = art['artistDisplayName']
        art_culture = art['culture']
        art_highlight = art['isPublicDomain']


for i in searched_art_list[1][:5]:
    SelectArt(str(i))
    print('this is i: ' + str(i))

# searched_art_list

    # st.image(
    #                 art_search_request[i]["objectIDs"],
    #                 width=400, # Manually Adjust the width of the image as per requirement
    #             )


