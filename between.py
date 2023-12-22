import pandas as pd

weekly_data = {'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                       'Friday', 'Saturday', 'Sunday'],
               'temperature': [40, 33, 42, 31, 41, 40, 30],
               'condition': ['Sunny, ', '_Cloudy ', 'Sunny', 'Rainy',
                             '--Sunny. ', 'Cloudy.', 'Rainy']
               }
df = pd.DataFrame(weekly_data)
print(df, "\n")

print(df[(df.temperature >= 30) & (df.temperature <= 40)], "\n")
print(df[df.temperature.between(30, 40)], "\n")
# В обоих случаях мы получим одинаковый консольный вывод. Однако использовать
# метод between удобнее, чем фильтры с условиями.
print((df["temperature"] >= 30) & (df["temperature"] <= 40), "\n")
