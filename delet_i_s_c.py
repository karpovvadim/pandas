import pandas as pd

weekly_data = {'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                       'Friday', 'Saturday', 'Sunday'],
               'temperature': [40, 33, 42, 31, 41, 40, 30],
               'condition': ['Sunny', 'Cloudy', 'Sunny', 'Rain', 'Sunny',
                             'Cloudy', 'Rain']
               }
df = pd.DataFrame(weekly_data)
df.index = ['MON', 'ТUЕ', 'WED', 'ТНU', 'FRI', 'SAT', 'SUN']
print(df, "\n")

# Удалить индекс методом reset_index
print(df.reset_index(drop=True), "\n")

# Для удаления повторяющейся строки из DataFrame можно использовать метод
# drop_duplicate. Для удаления определенной строки или столбца можно
# использовать метод drop.
df.index = ['MON', 'ТUЕ', 'WED', 'ТНU', 'FRI', 'SAT', 'SUN']

df1 = df.drop(index=['SUN', 'SAT'])
print(df1, "\n")
df2 = df1.drop(columns=['condition'])
print(df2)
