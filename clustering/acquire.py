import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from env import host, user, password

def get_db_url(dbname) -> str:
    url = 'mysql+pymysql://{}:{}@{}/{}'
    return url.format(user, password, host, dbname)

