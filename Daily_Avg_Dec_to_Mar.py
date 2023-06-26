
import numpy as np
import pandas as pd


def get_daily_avg_dec_to_mar(provider_code="R0A"):
    daily_data = pd.read_excel("./data/Daily Average Data.xlsx")

    daily_data["Date"] = pd.to_datetime(daily_data["Date"], errors='coerce')

    daily_data["Date"] = pd.to_datetime(daily_data["Date"], format="%Y-%m")

    x = daily_data.groupby('Provider_Code')

    selected_Provider = x.get_group(provider_code)
    selected_Provider.head()

    sample_std = selected_Provider.std(ddof=0)
    sample_mean = selected_Provider.mean()

    features = [
        "Daily_Average_Staff_Absence",
        "Arriving_by_ambulance",
        "Time_Lost_to_Ambulance_Handover_Delays_Hours",
        "Monthly_Avg_Patients_who_no_longer_meet_the_criteria_to_reside",
        "Daily_Avg_Bed_Occupancy>7 days",
        "Daily_Avg_Bed_Occupancy>14 days",
        "Daily_Avg_Bed_Occupancy>21 days"
    ]

    std_away = (selected_Provider[features] -
                sample_mean[features])/sample_std[features]
    std_away = std_away + (std_away > 0)
    std_away = (std_away*10)//10

    std_away[std_away >= 5] = 4
    std_away[std_away <= -5] = -4

    return std_away


get_daily_avg_dec_to_mar()
