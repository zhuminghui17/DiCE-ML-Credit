import streamlit as st
import pandas as pd
import datetime


st.write("""
# DiCE ML Pipeline in Hotel Booking Model and Targeted Advertising

DiCE (Diverse Counterfactual Explanations) is an emerging machine learning tool designed 
to enhance the interpretability and fairness of predictive models. It focuses on providing 
counterfactual explanations, which are essentially insights into how slight changes 
in input features can lead to different prediction outcomes. This is particularly useful 
in scenarios where understanding the model's decision-making process is crucial, like credit approval. 
https://interpret.ml/DiCE/
""")

def user_input_features():

    hotelType = st.sidebar.selectbox('Hotel Type',('Resort Hotel','City Hotel'))

    bookingDate = st.sidebar.date_input("Booking Date", datetime.date.today())

    dateDeserved = st.sidebar.date_input(
        "Date You Reserved",
        (datetime.date.today(), datetime.date.today() + datetime.timedelta(days=1))
    )

    numOfAdults = st.sidebar.number_input("Number of Adults", value=1)
    numOfChildren = st.sidebar.number_input("Number of Children", value=0)

    meal = st.sidebar.selectbox("Type of Meal Booked", ("self-catering", "Bed & Breakfast", "Half Board", "Full Board"))

    is_repeated_guest = st.sidebar.checkbox("is a repeated guest")

    previous_cancellations = st.sidebar.number_input("Previous Cancel", value=0)
    previous_bookings_not_canceled = st.sidebar.number_input("previous_bookings_not_canceled", value= 0)

    reserved_room_type = st.sidebar.selectbox('Room Type',('A','B', "C", "D"))

    deposit_type = st.sidebar.selectbox('Deposit Type',('No Deposit','Non Refund', "Refundable"))

    adr = st.sidebar.slider("Average Daily Rate", 0, 1000, 0)

    required_car_parking_spaces = st.sidebar.number_input(" required_car_parking_spaces", value=0)

    total_of_special_requests = st.sidebar.number_input("total_of_special_requests", value=0)

    customer_type = st.sidebar.selectbox('Customer Type',('Transient', 'Contract', 'Transient-Party', 'Group'))




    data = {'hotel':[hotelType], }

    features = pd.DataFrame(data)

    return features

input_df = user_input_features()