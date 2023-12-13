import datetime


def calculate_booking_details(BookingDate, DateDeserved):
    # Calculate lead_time
    lead_time = (DateDeserved[0] - BookingDate).days

    # Extract arrival date details
    arrival_date_month = DateDeserved[0].strftime("%B")
    arrival_date_week_number = DateDeserved[0].isocalendar()[1]
    arrival_date_day_of_month = DateDeserved[0].day

    # Calculate stays_in_weekend_nights and stays_in_week_nights
    stays_in_weekend_nights = 0
    stays_in_week_nights = 0

    for single_date in (
        DateDeserved[0] + datetime.timedelta(n)
        for n in range((DateDeserved[1] - DateDeserved[0]).days + 1)
    ):
        if single_date.weekday() >= 5:  # 5 and 6 correspond to Saturday and Sunday
            stays_in_weekend_nights += 1
        else:
            stays_in_week_nights += 1

    return (
        lead_time,
        arrival_date_month,
        arrival_date_week_number,
        arrival_date_day_of_month,
        stays_in_weekend_nights,
        stays_in_week_nights,
    )
