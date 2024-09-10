import pandas as pd
import numpy as np

current_month = pd.to_datetime("today").month
current_year = pd.to_datetime("today").year

days_in_month = pd.date_range(start=f'{current_year}-{current_month}-01', end=f'{current_year}-{current_month + 1}-01', freq='D')[:-1]

temperatures = np.random.uniform(15, 35, size=len(days_in_month))

temperature_series = pd.Series(data=temperatures, index=days_in_month)

print(temperature_series)
