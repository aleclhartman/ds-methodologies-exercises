import numpy as np
import pandas as pd

from env import get_db_url

telco_url = get_db_url("telco_churn")

telco_query = """
SELECT c.customer_id, c.monthly_charges, c.tenure, c.total_charges
FROM customers AS c
JOIN contract_types AS ct USING(contract_type_id)
WHERE ct.contract_type = 'Two year'"""

def wrangle_telco():
    customers = pd.read_sql(telco_query, telco_url)
    customers.total_charges = customers.total_charges.str.strip()
    customers = customers.replace("", np.nan)
    df = customers.dropna()
    df["total_charges"] = df.total_charges.astype("float")
    return df