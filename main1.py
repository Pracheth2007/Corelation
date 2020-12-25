import plotly.express as px
import csv
with open("cofee.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.bar(df,x = "Coffee", y="sleep")
    fig.show()