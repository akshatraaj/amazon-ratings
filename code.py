import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv(
    r"E:\rv\whitehatjr\python\normal distribution\amazon ratings\data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])
fig.show()
