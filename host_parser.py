import pandas as pd
from tools import times_unix

# Require inputs to the user
init_datetime = input('Please enter the initial date in the following format YYYY-MM-DD HH:MM:SS: ')
end_datetime = input('Please enter the end date in the following format YYYY-MM-DD HH:MM:SS: ')
host_name = input('Please enter the host name: ')

# Opens the required file
with open('examples.log', 'r', encoding='utf-8') as test:
    lines = test.readlines()
data = []
for line in lines:
    columns = line.strip().split()
    data.append(columns)

# Creates a dataframe to work with
df = pd.DataFrame(data, columns=['timestamp', 'host1', 'host2'])

# Sort timestamp column to reassure it is ordered
df['timestamp'] = df['timestamp'].astype('int')
df.sort_values(by='timestamp')

# Retrieve values between introduced dates
df_date_filtered = df[(df['timestamp'] >= times_unix(init_datetime)) & (df['timestamp'] <= times_unix(end_datetime))]

# Retrieve hosts connected to the introduced host
df_host_filtered = df_date_filtered[df_date_filtered['host1'] == host_name]

# Logs information to the user
print('The hosts connected to', host_name, 'between', init_datetime, 'and', end_datetime, 'are:', df_host_filtered['host2'].to_string(index=False))