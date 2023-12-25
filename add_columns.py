import pandas as pd

weekly_data = {'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                       'Friday', 'Saturday', 'Sunday'],
               'temperature': [40, 33, 42, 31, 41, 40, 30],
               'condition': ['Sunny', 'Cloudy', 'Sunny', 'Rain', 'Sunny',
                             'Cloudy', 'Rain']
               }

df = pd.DataFrame(weekly_data)
df.index = ['MON', 'ТUЕ', 'WED', 'ТНU', 'FRI', 'SAT', 'SUN']

# Добавление списка значений после метки столбца: при таком подходе новый
# столбец добавляется после существующих столбцов; если указать существующую
# метку столбца, это позволит заменить или обновить значения в нем.
# Добавляем столбец и обновляем его
df['Humidity1'] = [60, 70, 65, 62, 56, 25, '']  # Влажность
print(df, "\n")
df['Humidity1'] = [60, 70, 65, 62, 56, 91, '']
print(df, "\n")

# Вставляем столбец с индексом 2, используя insert
df.insert(2, "Humidity2", [60, 70, 65, 62, 56, 25, ''])
print(df, "\n")

# Добавляем 2 столбца методом assign
df1 = df.assign(HumidityЗ=[60, 70, 65, 62, 56, 25, ''],
                Humidity4=[60, 70, 65, 62, 56, 25, ''])
print(df1)
