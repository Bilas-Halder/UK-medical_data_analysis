
import numpy as np
import pandas as pd


def get_march_all_hospital(month="2023-03-31"):
    monthly_data = pd.read_excel("./data/Monthly Data.xlsx")

    monthly_data["Month"] = pd.to_datetime(
        monthly_data["Month"], errors='coerce')

    monthly_data["Month"] = pd.to_datetime(
        monthly_data["Month"], format="%Y-%m")

    x = monthly_data.groupby('Month')

    selected_Provider = x.get_group(month)
    selected_Provider.head()

    sample_std = selected_Provider.std(ddof=0)
    sample_mean = selected_Provider.mean()

    features = [
        "AandE_Attends_Type1",
        "Attends_Under_4Hrs_Arr_To_Adm_Tfr_Disch_Type1",
        "Attends_Over_4Hrs_Arr_To_Adm_Tfr_Disch_Type1",
        "Emerg_Adms_Via_Type1",
        "Emerg_Adms_Not_Via_AandE",
        "Dec_To_Adm_4_to_12Hrs",
        "Dec_To_Adm_Over_12Hrs",
    ]

    std_away = (selected_Provider[features] -
                sample_mean[features])/sample_std[features]
    std_away = std_away + (std_away > 0)
    std_away = (std_away*10)//10

    return std_away
