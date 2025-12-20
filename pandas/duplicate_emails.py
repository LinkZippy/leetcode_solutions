# Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

# Return the result table in any order.

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person["dupe"] = person.duplicated(subset="email")
    res = person[person["dupe"] == True][["email"]].drop_duplicates()
    res.columns = ["Email"]
    return res
    
