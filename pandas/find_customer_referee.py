# Find the names of the customer that are either:

# referred by any customer with id != 2.
# not referred by any customer.
# Return the result table in any order.

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    mask = (customer["referee_id"] != 2) | (customer["referee_id"].isnull())
    return customer[mask][["name"]]
    
