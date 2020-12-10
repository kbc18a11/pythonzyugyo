import pandas as pd

df = pd.read_csv('test.csv')

data_d = df.query("英語%2 == 0")
print("数学が70点未満\n", data_d)
