"""
Получение статистики по данным объекта DataFrame
Получить статистические данные, например, центральную тенденцию, стандартное
отклонение и форму можно, используя метод describe. Вывод метода для числовых
столбцов включает следующее:
♦ count (количество);
♦ mean (среднее значение);
♦ standard deviation (стандартное отклонение);
♦ min (минимальное значение);
♦ max (максимальное значение);
♦ 25th percentile (25-й персентиль), 50 th percentile (50-й персентиль),
75th percentile (75-й персентиль).
Разделение персентилей по умолчанию можно изменить с помощью аргумента
percentiles.
Если метод describe используется для нечисловых данных вроде строк, мы можем
получить от них count, unique, top и freq. Где top - наиболее распространенное
значение, а freq - частота наиболее распространенного значения. По умолчанию
только числовые столбцы оцениваются методом describe, если мы не предоставим
аргумент include с соответствующим значением.
"""
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

weekly_data = {'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                       'Friday', 'Saturday', 'Sunday'],
               'temperature': [40, 33, 42, 31, 41, 40, 30],
               'condition': ['Sunny, ', '_Cloudy ', 'Sunny', 'Rainy',
                             '--Sunny. ', 'Cloudy.', 'Rainy']
               }
df = pd.DataFrame(weekly_data)
df["condition"] = df["condition"].map(lambda x: x.lstrip('_- ').rstrip(',. '))
print(df, "\n\n", "-------------df.describe()---------------------------------")
print(df.describe(), '\n')
print("----------include='all'--------------------------------------")
print(df.describe(include="all"), '\n')
print("----------percentiles----------------------------------------")
print(df.describe(percentiles=np.arange(0, 1, 0.1)), '\n')
print("--------groupby('condition').describe(percentiles--------------")
print(df.groupby('condition').describe(percentiles=np.arange(0, 1, 0.1)))
