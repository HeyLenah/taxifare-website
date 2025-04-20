import streamlit as st

import numpy as np
import pandas as pd
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
# date & time
d = str(st.date_input(
    "When's your taxi ride?",
    datetime.date(2019, 7, 6)))
st.write('Your ride is on:', d)

t = str(st.time_input('Time of your ride', datetime.time(8, 45)))
st.write("You're taking a taxi at the following time:", t)

date_and_time = d + ' ' + t

date_and_time = datetime.datetime.strptime(date_and_time, '%Y-%m-%d %H:%M:%S')

st.write(date_and_time)

# pickup longitude
pickup_long = st.number_input('Pickup longtiude ')
st.write('Pickup longtiude', pickup_long)

# pickup latitude
pickup_lat = st.number_input('Pickup latitude ')
st.write('Pickup latitude', pickup_lat)

# dropoff longitude
dropoff_long = st.number_input('Dropoff longitude ')
st.write('Dropoff longitude:', dropoff_long)

# dropoff latitude
dropoff_lat = st.number_input('Dropoff latitude ')
st.write('Dropoff latitude', dropoff_lat)

# Passenger count
pass_count = st.number_input('How many cars do you need?', step=1, min_value=1, max_value=40)
st.write(pass_count)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''
#2. Let's build a dictionary containing the parameters for our API...

params = {
    'pickup_datetime': date_and_time,
    'pickup_longitude': pickup_long,
    'pickup_latitude': pickup_lat,
    'dropoff_longitude': dropoff_long,
    'dropoff_latitude': dropoff_lat,
    'passenger_count': pass_count
    }

#3. Let's call our API using the `requests` package...
resposne = requests.get('https://taxifare.lewagon.ai/predict', params=params)

url = 'https://taxifare.lewagon.ai/predict'

#4. Let's retrieve the prediction from the **JSON** returned by the API...
st.write(resposne.json())



'''
## Finally, we can display the prediction to the user
'''
