import pandas as pd

weekly_data = {'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                       'Friday', 'Saturday', 'Sunday'],
               'temperature': [40, 33, 42, 31, 41, 40, 30],
               'condition': ['Sunny', 'Cloudy', 'Sunny', 'Rain', 'Sunny',
                             'Cloudy', 'Rain']
               }
df = pd.DataFrame(weekly_data)
df.index = ['MON', 'ТUЕ', 'WED', 'ТНU', 'FRI', 'SAT', 'SUN']

# Для переименования меток индекса или столбца используется метод rename
df1 = df.rename(index={'SUN': 'SU', 'SAT': 'SA'})
df2 = df1.rename(columns={'condition': 'cond'})
print(df2)
