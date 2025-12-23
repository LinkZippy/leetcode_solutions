# Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

# Return the result table in any order.

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:

    weather.sort_values(by="recordDate", inplace=True)

    prev_temp = weather["temperature"].shift(1)
    prev_date = weather["recordDate"].shift(1)

    mask = (weather["temperature"] > prev_temp) & (weather["recordDate"].diff().dt.days == 1)

    return weather[mask][["id"]]
    
