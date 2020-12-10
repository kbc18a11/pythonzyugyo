import pandas as pd

df = pd.read_csv('test.csv')
df.index = ['0', '1', '2', '3', '4', '5']

print('C子のデータ\n', df.iloc[2])
print('C子とD郎のデータ\n', df.iloc[[2, 3]])
print('C子の国語データ\n', df.iloc[2]['国語'])
print("slice 1-4 loc\n", df.loc["1": "4"])
print("slice 1-4 iloc\n", df.iloc[1:4])
