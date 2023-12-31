"""
Простой способ применить функцию к DataFrame - использовать методы
apply, applymap или map. Метод apply применим к столбцам или строкам, а метод
applymap работает поэлементно для всего DataFrame. Метод map также работает
поэлементно, но для одного ряда.
Часто импортированные в DataFrame данные нуждаются в очистке. Например, они
могут иметь пробелы в конце или в начале, символы новой строки и другие
нежелательные элементы. Их можно легко удалить, используя метод map и
лямбда-функцию в рядах столбцов. Лямбда-функция применяется к каждому элементу
столбца. В нашем примере сначала удалим конечный пробел, точку и запятую.
Затем удалим начальный пробел, подчеркивание и тире в столбце condition.
После очистки данных в столбце condition мы создадим столбец temp_F из значений
столбца temp, а затем преобразуем эти значения из градусов Цельсия в градусы
Фаренгейта. Обратите внимание, мы будем использовать другую лямбда-функцию для
этого преобразования и метод apply. Когда мы получим результат от метода apply,
сохраним его внутри новой метки столбца (temp_F) для создания нового столбца.
"""
import pandas as pd

weekly_data = {'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                       'Friday', 'Saturday', 'Sunday'],
               'temperature': [40, 33, 42, 31, 41, 40, 30],
               'condition': ['Sunny, ', '_Cloudy ', 'Sunny', 'Rainy',
                             '--Sunny. ', 'Cloudy.', 'Rainy']
               }

df = pd.DataFrame(weekly_data)
print(df, "\n")

df["condition"] = df["condition"].map(lambda x: x.lstrip('_- ').rstrip(',. '))
df["temp_F"] = df["temperature"].apply(lambda x: 9 / 5 * x + 32)
print(df)
