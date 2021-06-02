from typing import List, Text
from requests.api import request
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests 
from PIL import Image
import numpy as np
import random
import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
import matplotlib.pyplot as plt
from pandas import DataFrame
from IPython.core.display import HTML





st.set_page_config(layout="wide")
st.title('All in One Application')


url = 'http://numbersapi.com/random/year'

st.header('Here is a fun fact about a random number')
random = st.button('learn about a random number', key="1")

#If random button is clicked then fact will be shown about random number
if random:
    st.write(requests.get(url).text)

st.markdown('''**Here is a fun fact about a number of your choosing**''')

#User can enter what number they will to learn about
num = st.text_input('Please enter a number you wish to learn about')

number = st.button('Learn about',key="2")
if number:
    #will append whatever number user entered to find a fun fact about it
    st.write(requests.get(f'http://numbersapi.com/{num}/trivia').text)



st.write('---------------------------------------------')

st.header('Take a Break with a Funny Joke')

joke_body = requests.get('https://official-joke-api.appspot.com/random_joke').json()

set_up_joke = joke_body['setup']
punch_line = joke_body['punchline']

jokes= st.button('Random Joke', key="3")
if jokes:
    st.write(set_up_joke)
    st.write(punch_line)
    
st.write('---------------------------------------------')

st.header('Enjoy these Art pieces')

st.markdown('''**Move the slider to see an art piece** ''')

#Allows user to select a art id they want to see 
art_number = st.slider('Art Number', 1000, 6000)

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
                            width=300,
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

#Only if user selects a art id will the image and description be shown 
if art_number:
    SelectArt(art_number)

st.header('Search For An Art Work')

#allows art search feature for user
art_word = st.text_input("Enter a word of an art you would like to see")

#whatever word is inputted will be appended to URL 
search_art_url = f'https://collectionapi.metmuseum.org/public/collection/v1/search?q={art_word}'

#Display art only if user searches something 
if art_word:
    art_search_request = requests.get(search_art_url).json()

    #shows the total number of art pieces from searched word
    total_art_pieces = art_search_request['total']

    searched_art_list = [] #ids of all the art from search 
    total_art_pieces

    for k,v in art_search_request.items():
        #appends unique art ids
        if v not in searched_art_list:
            searched_art_list.append(v)


    #Used this to divide my gallery into 3 columns
    col1, col2, col3 = st.beta_columns(3) 

    #Function takes 2 parameters, id being art id and col being what column art will be displayed
    def ArtAPI(id,col):
        art_url= f'https://collectionapi.metmuseum.org/public/collection/v1/objects/{id}'
        art = requests.get(art_url).json()
        with col:
            st.image(art['primaryImage'],caption=art['title'])
            #checkbox if user wants more information
            learn_more = st.checkbox("Learn More",key=id)
            #if user clicks checkbox, artist and culture will be displayed
            if learn_more:
                    if art['artistDisplayName']: st.write('Artist: ' + art['artistDisplayName'])
                    else: st.write('Artist Unknown ')
                    if art['culture']: st.write('Culture: ' + art['culture']) 
                    else: st.write('Culture Unknown ')
        

    
    for i in searched_art_list[1][0:4]:
        ArtAPI(i,col1)
            
    for i in searched_art_list[1][4:8]:
        ArtAPI(i,col2)

    for i in searched_art_list[1][8:12]:
        ArtAPI(i,col3)
            
st.write('---------------------------------------------')

st.header('Cheer up with these dogs')


dog_image_link = []

random_dog = st.button('Random Dog',key="2")
if random_dog:
    random_dog_request = requests.get('https://random.dog/woof.json').json()
    for i in random_dog_request.values():
        dog_image_link.append(i)
    st.image(dog_image_link[1],width=300,)

st.write('---------------------------------------------')


consumer_key = ""
consumer_secret = ""

access_token = ''
access_token_secret = ''



auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)


st.header('Cant decide what to eat? Let twitter decide for you! ') 

def get_tweets(food):
    public_tweets = api.search(food)
    all_tweets = []
    sentiment_score = []
    for tweet in public_tweets:
        all_tweets.append(tweet.text)
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_score.append(blob.sentiment.polarity)
    average_score = statistics.mean(sentiment_score)
    return average_score

food1 = st.text_input('Enter one food item you are thinking of trying')
food_2_entered = False
if food1: 
    food1_average_sentiment = get_tweets(food1)
    food2 = st.text_input('Enter another food item you are thinking of trying')
    if food2:
        food_2_entered= True
    
if food_2_entered == True:
    food2_average_sentiment = get_tweets(food2)

    if (food1_average_sentiment > food2_average_sentiment):
        st.write(f'Twitter users seem to prefer {food1} more than {food2}')
    if (food1_average_sentiment < food2_average_sentiment):
        st.write(f'Twitter users seem to prefer {food2} more than {food1}')

st.write('---------------------------------------------')

r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')  #to timeout on request 
r_data = r.json()

data_list = []
image_list = []

for i in range(len(r_data)):
    data_list.append((r_data[i]["name"],r_data[i]["symbol"],r_data[i]["current_price"],r_data[i]["high_24h"],r_data[i]["low_24h"],"{:,}".format(r_data[i]["market_cap"])))


for i in range(len(r_data)):
    image_list.append((r_data[i]["image"]))

df = DataFrame (data_list,columns=['Name','Symbol','Current Price','Highest Price in 24hrs','Lowest Price in 24hrs','Market Cap'])

df