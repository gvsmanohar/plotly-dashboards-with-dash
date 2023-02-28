import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

df = pd.read_csv("data/wheels.csv")

app = dash.Dash()

app.layout = html.Div(
    [
        dcc.RadioItems(
            id="wheels",
            options=[{"label": i, "value": i} for i in df["wheels"].unique()],
            value=1,
        ),
        html.Div(id="wheels-output"),
        html.Hr(),  # add horizontal rule
        dcc.RadioItems(
            id="colors",
            options=[{"label": i, "value": i} for i in df["color"].unique()],
            value="red",
        ),
        html.Div(id="colors-output"),
    ],
    style={"fontFamily": "helvetica", "fontSize": 18},
)


@app.callback(Output("wheels-output", "children"), [Input("wheels", "value")])
def callback_a(wheels_value):
    return 'you\'ve selected "{}"'.format(wheels_value)


@app.callback(Output("colors-output", "children"), [Input("colors", "value")])
def callback_b(colors_value):
    return 'You\'ve selected "{}"'.format(colors_value)


if __name__ == "__main__":
    app.run_server()
