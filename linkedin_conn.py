# %%
#   import libs
import pandas as pd
import os

# %%
#   read files
path = os.path.abspath(os.getcwd())
path_raw = path + '/data/raw'
path_done = path + '/data/done'

for dirs, subs, files in os.walk(path_raw):
    for file in files:
        df = pd.read_csv(f'{path_raw}/{file}', skiprows=2)

# %%
#   adding columns/simple changes
df['full_name'] = df['First Name'] + ' ' + df['Last Name']
df['connected_on'] = pd.to_datetime(df['Connected On'])
df = df.rename(str.lower, axis='columns')
# %%
#   selecting just main columns
df = df[['full_name', 'connected_on', 'company', 'position', 'url']]

# %%
df
# %%
df.sort_values(by='connected_on').reset_index()
# %%
#   save csv
df.to_csv(f'{path_done}/linkedin_conn.csv')
# %%
