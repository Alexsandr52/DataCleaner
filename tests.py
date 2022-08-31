import pandas
from gekDataCleaner import DataCleaner

data = DataCleaner('tests.xlsx')
data.conversion_binary_pharmacies(data)
data.convert_to_csv('./test.csv')
print(data.show(data))