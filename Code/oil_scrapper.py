import pandas as pd
import os
from dotenv import load_dotenv
import eikon as ek

load_dotenv()
ek.set_app_key(os.getenv('EIKON_APP_KEY'))



#

#ek.get_data()
#ek.get_timeseries()


# Test 1: front-month WTI close prices
df = ek.get_timeseries('CLc1', fields='CLOSE', start_date='2026-04-01')
print("=== Front-month WTI ===")
print(df.head())

# Test 2: pull a few months of the curve at once
rics = [f'CLc{i}' for i in range(1, 7)]  # front 6 months
df2, err = ek.get_data(rics, ['CF_LAST', 'CF_DATE', 'EXPIR_DATE'])
print("\n=== WTI Term Structure (front 6) ===")
print(df2)







