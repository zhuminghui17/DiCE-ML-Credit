import streamlit as st
import pandas as pd
import datetime
from lib import calculate_booking_details
from predict import predict
import openai


def display_header():
    st.write(
        """
    # DiCE ML Pipeline in Hotel Booking Model and Targeted Advertising
    """
    )


def get_hotel_type():
    return st.sidebar.selectbox("Hotel Type", ("Resort Hotel", "City Hotel"))


def get_booking_dates():
    booking_date = st.sidebar.date_input("Booking Date", datetime.date.today())
    date_reserved = st.sidebar.date_input(
        "Date You Reserved",
        (datetime.date.today(), datetime.date.today() + datetime.timedelta(days=1)),
    )
    return booking_date, date_reserved


def get_guest_info():
    num_of_adults = st.sidebar.number_input("Number of Adults", value=1)
    num_of_children = st.sidebar.number_input("Number of Children", value=0)

    meal_options = {
        "Bed & Breakfast": "BB",
        "Full Board": "FB",
        "Half Board": "HB",
        "Self Catering": "SC",
    }
    meal_choice = st.sidebar.selectbox("Type of Meal Booked", list(meal_options.keys()))
    meal = meal_options[meal_choice]

    is_repeated_guest = st.sidebar.checkbox("is a repeated guest")
    return num_of_adults, num_of_children, meal, is_repeated_guest


def get_booking_history():
    previous_cancellations = st.sidebar.number_input("Previous Cancel", value=0)
    previous_bookings_not_canceled = st.sidebar.number_input(
        "previous_bookings_not_canceled", value=0
    )
    return previous_cancellations, previous_bookings_not_canceled


def get_room_and_payment_details():
    reserved_room_type = st.sidebar.selectbox("Room Type", ("A", "B", "C", "D"))
    deposit_type = st.sidebar.selectbox(
        "Deposit Type", ("No Deposit", "Non Refund", "Refundable")
    )
    adr = st.sidebar.slider("Average Daily Rate", 0, 1000, 0)
    required_car_parking_spaces = st.sidebar.number_input(
        " required_car_parking_spaces", value=0
    )
    total_of_special_requests = st.sidebar.number_input(
        "total_of_special_requests", value=0
    )
    customer_type = st.sidebar.selectbox(
        "Customer Type", ("Transient", "Contract", "Transient-Party", "Group")
    )
    return (
        reserved_room_type,
        deposit_type,
        adr,
        required_car_parking_spaces,
        total_of_special_requests,
        customer_type,
    )


def user_input():
    hotel_type = get_hotel_type()
    booking_date, date_reserved = get_booking_dates()
    num_of_adults, num_of_children, meal, is_repeated_guest = get_guest_info()
    previous_cancellations, previous_bookings_not_canceled = get_booking_history()
    (
        reserved_room_type,
        deposit_type,
        adr,
        required_car_parking_spaces,
        total_of_special_requests,
        customer_type,
    ) = get_room_and_payment_details()
    (
        lead_time,
        arrival_date_month,
        arrival_date_week_number,
        arrival_date_day_of_month,
        stays_in_weekend_nights,
        stays_in_week_nights,
    ) = calculate_booking_details(booking_date, date_reserved)

    data = {
        "hotel": [hotel_type],
        "lead_time": [lead_time],
        "arrival_date_month": [arrival_date_month],
        "arrival_date_week_number": [arrival_date_week_number],
        "arrival_date_day_of_month": [arrival_date_day_of_month],
        "stays_in_weekend_nights": [stays_in_weekend_nights],
        "stays_in_week_nights": [stays_in_week_nights],
        "adults": [num_of_adults],
        "children": [num_of_children],
        "meal": [meal],
        "is_repeated_guest": [int(is_repeated_guest)],
        "previous_cancellations": [int(previous_cancellations)],
        "previous_bookings_not_canceled": [int(previous_bookings_not_canceled)],
        "reserved_room_type": [reserved_room_type],
        "deposit_type": [deposit_type],
        "customer_type": [customer_type],
        "adr": [adr],
        "required_car_parking_spaces": [required_car_parking_spaces],
        "total_of_special_requests": [total_of_special_requests],
    }

    return pd.DataFrame(data)


def main():
    display_header()
    input_df = user_input()
    api_key = st.text_input("Enter your OpenAI API key", type="password")

    if st.button("Run", key="run1") and api_key:  # Unique key for this button
        openai.api_key = api_key
        prompt = predict(input_df)

        # Directly making the API call without try-catch block
        response = openai.Completion.create(
            model="text-davinci-003", prompt=prompt, max_tokens=1000
        )

        # Display the generated response
        st.write(response["choices"][0]["text"].strip())


if __name__ == "__main__":
    main()
