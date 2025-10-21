import pandas as pd
df = pd.read_csv('toilets.csv')

print(df.head())


print(df['country'].value_counts())
