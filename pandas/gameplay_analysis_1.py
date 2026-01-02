# Write a solution to find the first login date for each player.

# Return the result table in any order.

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    res = activity.groupby(by="player_id")["event_date"].min().reset_index()
    res.columns = ["player_id","first_login"]
    return res
