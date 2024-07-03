
import pandas

print("Start csv uitlezen")


df = pandas.read_csv('pokemon.csv')

# print(df["Name"])

for r,rij in df.iterrows():
    print(rij["Name"])