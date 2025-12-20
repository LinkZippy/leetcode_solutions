# Write a solution to find employees who have the highest salary in each of the departments.

# Return the result table in any order.

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp', "_dep"))
    df['rank'] = df.groupby('name_dep')['salary'].rank(method="dense", ascending=False)
    result = df[df['rank'] == 1][["name_dep", "name_emp", "salary"]]
    result.columns = ["Department", "Employee", "Salary"]
    return result
