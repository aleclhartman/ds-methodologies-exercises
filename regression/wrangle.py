import numpy as np
import pandas as pd

from env import get_db_url

def wrangle_grades():
    grades = pd.read_csv("student_grades.csv")
    grades.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    df = grades.dropna().astype('int')
    df.drop(columns="student_id", inplace=True)
    return df

telco_query = """
SELECT c.customer_id, c.monthly_charges, c.tenure, c.total_charges
FROM customers AS c
JOIN contract_types AS ct USING(contract_type_id)
WHERE ct.contract_type = 'Two year';
"""

telco_url = get_db_url("telco_churn")

def wrangle_telco():
    """
    This function does the following:
        1. Queries data from the telco_churn database into a pandas DataFrame
        2. Cleans the total_charges feature
        3. Replaces any empty strings with np.nan
        4. Removes any rows with missing values
        5. Reassigns the total_charges feature as a float
        6. Returns a new pandas DataFrame
    """
    customers = pd.read_sql(telco_query, telco_url)
    customers.total_charges = customers.total_charges.str.strip()
    customers = customers.replace("", np.nan)
    df = customers.dropna()
    df["total_charges"] = df.total_charges.astype("float")
    return df