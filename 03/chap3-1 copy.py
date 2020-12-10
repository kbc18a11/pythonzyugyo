import pandas as pd

df = pd.read_csv('test.csv')

df['美術'] = [68, 73, 82, 77, 94, 96]
print('列データ(美術)を追加\n', df)

df.loc[6] = ['G絵', 90, 92, 94, 96, 92, 98]
print('列データ(G絵)を追加\n', df)
