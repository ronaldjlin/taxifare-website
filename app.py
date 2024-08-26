import streamlit as st
import requests

import datetime

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

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

with st.form('User_form '):
    input_date = st.date_input('Specify a date',  datetime.date(2024, 7, 6))
    user_time = st.time_input('Specify time', datetime.time(8, 45))
    date_time = f'{input_date} {user_time}'
    pickup_longitude = st.number_input('Please specify your longtitude', value=(-73.950655))
    pickup_latitude = st.number_input('Please specify your latitude', value=(40.783282))
    dropoff_longitude = st.number_input('Please specify your drop off longtitude', value=(-73.984365))
    dropoff_latitude = st.number_input('Please specify your drop off latitude', value=(40.769802))
    passenger_count = st.number_input('Please specify number of passengers', value = (1))

    # slider_val = st.slider('Pick a value', 0, 100)
    # checkbox_val = st.checkbox('I agree')

    submitted = st.form_submit_button("Submit")

    if submitted:
            # Build the dictionary with the parameters
            params = {
                "pickup_datetime": date_time,
                "pickup_longitude": pickup_longitude,
                "pickup_latitude": pickup_latitude,
                "dropoff_longitude": dropoff_longitude,
                "dropoff_latitude": dropoff_latitude,
                "passenger_count": passenger_count,
                # "slider_val": slider_val,
                # "checkbox_val": checkbox_val
            }

            # st.write("Parameters for API:", params)

            # Call the API using the requests package
            api_url = "https://taxifare.lewagon.ai/predict"
            response = requests.get(api_url, params=params).json()

            st.warning(response)

            st.write('Fare amount is:', round(response['fare'], 2))

            # if response.status_code == 200:
            #     # Retrieve the prediction from the JSON response
            #     prediction = response.json().get('prediction')
            #     st.write("Prediction:", prediction)
            # else:
            #     st.write("Failed to retrieve prediction. Status code:", response.status_code)

st.write("Outside the form")
