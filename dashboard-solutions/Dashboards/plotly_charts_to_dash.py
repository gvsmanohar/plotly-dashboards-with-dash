import dash
from dash import html, dcc
import plotly.graph_objects as go
import numpy as np

np.random.seed(2)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.Graph(
            id="Scatter",
            figure={
                "data": [
                    go.Scatter(
                        x=random_x,
                        y=random_y,
                        mode="markers",
                        marker={
                            "size": 12,
                            "color": "rgb(51,204,153)",
                            "symbol": "pentagon",
                            "line": {"width": 2},
                        },
                    )
                ],
                "layout": go.Layout(
                    title="Random Data Scatterplot",
                    xaxis={"title": "Some random x-values"},
                    yaxis=dict(title="some random y-values"),
                    hovermode="closest",
                ),
            },
        )
    ]
)

if __name__ == "__main__":
    app.run_server()
