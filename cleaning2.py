import pandas as pd
import csv

df = pd.read_csv("bright_stars.csv")
del df["Luminosity"]


df = df.rename({
    "Star_name":"Stars_name"
},axis="columns")

df.to_csv("cleanedData2.csv")


