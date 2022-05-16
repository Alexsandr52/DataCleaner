import pandas as pd
import gekDataCleaner as dc

df1 = dc.get_dataframe('tests.xlsx')
df2 = pd.read_excel('tests.xlsx')
print(df1 == df2)


# df = dc.get_dataframe('tests.xlsx')
# start_mem = df.memory_usage().sum() / 1024**2 
# print(f'start memory {start_mem} MB')

# dc.reduce_mem_usage(df, copy=False, logs=False)
# # print(df.memory_usage())
# dc.conversion_binary_pharmacies(df, logs=False)

# end_mem = df.memory_usage().sum() / 1024**2 
# print(f'end memory {end_mem} MB')
# print(f'differens {round(100 * (start_mem - end_mem) / start_mem, 2)}%')

# start memory 0.00067138671875 MB
# end memory 0.000396728515625 MB
# differens 40.91%