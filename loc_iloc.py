"""
Можно выбрать одну или несколько строк, используя метки индекса с методом
loc; метка предоставляется как отдельный элемент или список
"""
import pandas as pd
weekly_data = {'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                       'Friday', 'Saturday', 'Sunday'],
               'temperature': [40, 33, 42, 31, 41, 40, 30],
               'condition': ['Sunny', 'Cloudy', 'Sunny', 'Rain', 'Sunny',
                             'Cloudy', 'Rain']
               }
df = pd.DataFrame(weekly_data)
df.index = ['MON', 'ТUЕ', 'WED', 'ТНU', 'FRI', 'SAT', 'SUN']
print(df.loc['ТUЕ'], "\n")
print(df.loc[['ТUЕ', 'WED']], "\n")


# Можно выбрать значение из расположения в объекте DataFrame по метке
# строки и метке столбца:
print("FRI, temperature:", df.loc['FRI', 'temperature'], "\n")

# Мы можем выбрать строку по значению индекса без указания меток:
print(df.iloc[2], "\n")

# Можно выбрать значение из расположения, используя индексы строки и столбца
print(df.iloc[6, 2], "\n")

# Добавление строки
df.loc['TST'] = ['Test day 1', 50, 'NA']
print(df, "\n")

# Добавление строки индексу
df.loc[8] = ['Test day 2', 40, 'NA']
print(df)
