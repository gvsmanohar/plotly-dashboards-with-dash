import dash
import pandas as pd
from dash import html, dcc
import plotly.graph_objects as go
import numpy as np

df = pd.read_csv("data/OldFaithful.csv")
print(df.head())

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Graph(
            id="scatter",
            figure={
                "data": [
                    go.Scatter(x=df["X"], y=df["Y"], text=df["D"], mode="markers")
                ],
                "layout": go.Layout(
                    title="Old Faithful Eruption Intevals vs Durations",
                    xaxis={"title": "Duration of eruption (minutes)"},
                    yaxis={"title": "Interval to next eruption (minutes)"},
                    hovermode="closest",
                ),
            },
        )
    ]
)

if __name__ == "__main__":
    app.run_server()
