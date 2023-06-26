
import numpy as np
import pandas as pd


def get_provider_monthly_insight(provider_code):
    # getting the data
    monthly_data = pd.read_excel("./data/Monthly Data.xlsx")

    # changing month to datetime
    monthly_data["Month"] = pd.to_datetime(
        monthly_data["Month"], errors='coerce')

    # groupby provider_code to select provider
    x = monthly_data.groupby('Provider_Code')

    # selecting provider / hospital
    selected_Provider = x.get_group(provider_code)

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
