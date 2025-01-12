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
        if file.startswith('Connections') and file.endswith('.csv'):
            df_in = pd.read_csv(f'{path_raw}/{file}', skiprows=2)
        if file.startswith('leaderboards') and file.endswith('.csv'):
            df_duo = pd.read_csv(f'{path_raw}/{file}')

# %%
#   linkedin transformation
#   adding columns/simple changes
df_in['full_name'] = df_in['First Name'] + ' ' + df_in['Last Name']
df_in['connected_on'] = pd.to_datetime(df_in['Connected On'])
df_in = df_in.rename(str.lower, axis='columns')

#   selecting main columns
df_in = df_in[['full_name', 'connected_on', 'company', 'position', 'url']]

#   save csv
df_in.to_csv(f'{path_done}/linkedin_conn.csv', index=False)

# %%
#   duolinguo transformation
df_duo['date'] = pd.to_datetime(df_duo['timestamp']).dt.date

#   selecting main columns
df_duo = df_duo[['date', 'score']]

#   save csv
df_duo.to_csv(f'{path_done}/duolinguo_xp.csv', index=False)
