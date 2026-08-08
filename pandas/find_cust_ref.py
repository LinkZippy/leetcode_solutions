# Find the names of the customer that are either:

# referred by any customer with id != 2.
# not referred by any customer.

import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer[(customer['referee_id'] != 2) | (customer['referee_id'].isnull())][['name']]
    
