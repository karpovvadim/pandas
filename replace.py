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

# Заменим все вхождения числового значения 40 на 39
df.replace(40, 39, inplace=True)

# Заменим все вхождения строки sunny на sun
df.replace("Sunny", "Sun", inplace=True)

# Заменим все вхождения строки на основе регулярного выражения
# (Cloudy на Cloud)
df.replace(to_replace="^Cl.*", value="Cloud", inplace=True, regex=True)
# или также можно применить к определенному столбцу
df["condition"].replace(to_replace="^R.*", value="Rainy",
                        inplace=True, regex=True)
# использование меток to_replace и value опционально
print(df, "\n")

# Замена Monday и Tuesday на Mon и Tue.
df.replace(["Monday", "Tuesday"], ["Mon", "Tue"], inplace=True)
# ключи словаря (wednesday и Thursday) будут заменены значениями (wed и Thu).
df.replace({"Wednesday": "Wed", "Thursday": "Thu"}, inplace=True)
print(df, "\n")

df.replace({"day": "Friday"}, {"day": "Fri"}, inplace=True)
df.replace({"day": {"Saturday": "Sat", "Sunday": "Sun"},
            "condition": {"Rainy": "Rain"}}, inplace=True)
print(df)
# Аргумент inplace=True задействован во всех вызовах метода replace. Он
# используется для настройки вывода метода replace внутри того же объекта
# DataFrame. Параметр по умолчанию вернет новый объект, не меняя исходный.
# Для удобства этот аргумент доступен со многими методами DataFrame.
