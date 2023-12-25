import pandas as pd

weekly_data = {'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                       'Friday', 'Saturday', 'Sunday'],
               'temperature': [40, 33, 42, 31, 41, 40, 30],
               'condition': ['Sunny, ', '_Cloudy ', 'Sunny', 'Rainy',
                             '--Sunny. ', 'Cloudy.', 'Rainy']
               }

df = pd.DataFrame(weekly_data)
df["condition"] = df["condition"].map(lambda x: x.lstrip('_- ').rstrip(',. '))
print(df, "\n")
print(df[(df.condition == 'Rainy') | (df.condition == 'Sunny')], "\n")
print(df[df['condition'].str.contains('Rainy|Sunny')])
