# Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:

# have the same tiv_2015 value as one or more other policyholders, and
# are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
# Round tiv_2016 to two decimal places.

import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    mask1 = insurance.duplicated("tiv_2015",keep=False)
    mask2 = ~insurance.duplicated(["lat", "lon"],keep=False)
    res = insurance[mask1 & mask2]["tiv_2016"].sum().round(2)
    return pd.DataFrame({"tiv_2016" : [res]})
