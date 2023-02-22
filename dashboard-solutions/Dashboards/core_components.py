import dash
from dash import dcc, html

app = dash.Dash()

app.layout = html.Div(
    [
        # DROPDOWN https://dash.plot.ly/dash-core-components/dropdown
        html.Label("Dropdown"),
        dcc.Dropdown(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "United Kingdom", "value": "UK"},
                {"label": "San Francisco", "value": "SF"},
            ],
            value="UK",
        ),
        html.Label("Multi-Select Dropdown"),
        dcc.Dropdown(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "United Kingdom", "value": "UK"},
                {"label": "San Francisco", "value": "SF"},
            ],
            value=["UK", "SF"],
            multi=True,
        ),
        # SLIDER https://dash.plot.ly/dash-core-components/slider
        html.Label("Slider"),
        html.P(
            dcc.Slider(
                min=-5, max=10, step=0.5, marks={i: i for i in range(-5, 11)}, value=-3
            )
        ),
        # RADIO ITEMS https://dash.plot.ly/dash-core-components/radioitems
        html.Label("Radio Items"),
        dcc.RadioItems(
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "United Kingdom", "value": "UK"},
                {"label": "San Francisco", "value": "SF"},
            ],
            value="UK",
        ),
    ],
    style={"width": "50%"},
)

if __name__ == "__main__":
    app.run_server()
