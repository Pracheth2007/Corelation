import plotly.express as px
import csv
with open("ICETEMP.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.bar(df,x = "Temperature", y="Ice-cream Sales")
    fig.show()