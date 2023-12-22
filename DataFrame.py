"""
Введение в Pandas DataFrame
Pandas - библиотека Python с открытым исходным кодом, которая предоставляет
инструменты для высокопроизводительной обработки данных и упрощает анализ
информации. Обычно используется для изменения формы, сортировки, создания
срезов, агрегирования и объединения данных.
Библиотека построена поверх библиотеки NumPy - еще одной библиотеки Python
для работы с массивами. NumPy работает значительно быстрее, чем традиционные
списки Python, поскольку данные хранятся в одном непрерывном месте памяти.
Pandas работает с тремя ключевыми структурами данных:
♦ Series: одномерный массив, который содержит массив данных и массив меток
данных; массив меток называется index и может быть указан автоматически с
помощью целых чисел от О до n-1, если он явно не задан пользователем.
♦ DataFrame: представление табличных данных, вроде электронной таблицы со
списком столбцов; объект DataFrame помогает хранить и обрабатывать табличные
данные в строках и столбцах; следует отметить, что DataFrame имеет индекс,
как для столбцов, так и для строк.
♦ Panel: трехмерный контейнер данных.
DataFrame - это ключевая структура, которая используется для анализа данных.
"""
import pandas as pd
weekly_data = {'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                       'Friday', 'Saturday', 'Sunday'],
               'temperature': [40, 33, 42, 31, 41, 40, 30],
               'condition': ['Sunny', 'Cloudy', 'Sunny', 'Rain', 'Sunny',
                             'Cloudy', 'Rain']
               }
df = pd.DataFrame(weekly_data)
print(df)
