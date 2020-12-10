import pandas as pd

df = pd.read_csv('test.csv')

kokugo = df.sort_values('国語', ascending=False)
print('国語の降順\n', kokugo)
