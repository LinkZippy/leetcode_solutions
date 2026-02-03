# Write a solution to find managers with at least five direct reports.

# Return the result table in any order.

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    manager_counts = employee['managerId'].value_counts()
    temp = manager_counts[manager_counts >= 5].index   
    result = employee[employee['id'].isin(temp)][['name']]
    return result
    
