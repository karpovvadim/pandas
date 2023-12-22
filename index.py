import pandas as pd
weekly_data = {'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                       'Friday', 'Saturday', 'Sunday'],
               'temperature': [40, 33, 42, 31, 41, 40, 30],
               'condition': ['Sunny', 'Cloudy', 'Sunny', 'Rain', 'Sunny',
                             'Cloudy', 'Rain']
               }
df = pd.DataFrame(weekly_data)

print("\n-------set_index(day)------------------------------------")
df_new = df.set_index('day')
print(df_new)

# index: предоставляет список индексов (или меток) объекта DataFrame;
print("\n--Задать индекс вручную, передав его через список-------")
df.index = ['MON', 'ТUЕ', 'WED', 'ТНU', 'FRI', 'SAT', 'SUN']
print(df)
