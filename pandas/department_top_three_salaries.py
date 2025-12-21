# A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

# Write a solution to find the employees who are high earners in each of the departments.

# Return the result table in any order.

import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp', '_dep'))
    df['rank'] = df.groupby('name_dep')['salary'].rank(method='dense',ascending=False)
    res = df[df['rank'] <= 3][['name_dep','name_emp','salary']].rename(columns={
        'name_dep' : 'Department',
        'name_emp' : 'Employee',
        'salary' : 'Salary'
    })
    return res
