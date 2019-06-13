import pandas


df1 = pandas.read_csv("supermarkets.csv")
print(df1)

df2 = pandas.read_json("supermarkets.json")
print(df2)

df3 = pandas.read_excel("supermarkets.xlsx", sheet_name=0)
print(df3)

df4 = pandas.read_csv("supermarkets-commas.txt")
print(df4)

df5 = pandas.read_csv("supermarkets-semi-colons.txt", sep=";")
print(df5)

df6 = pandas.read_csv("supermarkets.txt", header=None)
# print(df6)

df6.columns = ["ID", "Address", "City", "ZIP", "Country", "Name", "Employees"]
print(df6)

df7 = df6.set_index("ID", inplace=True)
print(df7)

df8 = df7.drop("332 Hill St", 1)
print(df8)


