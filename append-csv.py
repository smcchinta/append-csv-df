import os
import pandas as pd

path = os.getcwd()
files = os.listdir(path)


files_csv = [f for f in files if f[-3:] == 'csv']
print(files_csv)

df = pd.DataFrame()
for f in files_csv:
    data = pd.read_csv(f)
    df = df.append(data)

df.to_csv('output.csv', encoding='utf-8', index=False)

## MERGE based on columns
# data1 = read_csv('CSVExport.csv')
# data2 = read_csv('Proof.csv')
#
# print(data1.head())
#
# data3 = merge(data1, data2, on='Reference Id|person.Reference-ID')
# #print(data3.head())
# #data3.rename(columns={'Asset Date|CoreField.DocDate_y': 'Asset Date|CoreField.DocDate'}, inplace=True)
# data3.rename(columns={'Discipline|person.discipline_y': 'Discipline|person.discipline'}, inplace=True)
# #df1 = data3[['Reference Id|person.Reference-ID', 'Unique Identifier|CoreField.Identifier', 'Asset Date|CoreField.DocDate', 'Discipline|person.discipline']]
# df1 = data3[['Reference Id|person.Reference-ID', 'Unique Identifier|CoreField.Identifier', 'Discipline|person.discipline']]
# print('**************')
# #print(df1.head())
# df1.to_csv('filename123.csv', encoding='utf-8', index=False)
