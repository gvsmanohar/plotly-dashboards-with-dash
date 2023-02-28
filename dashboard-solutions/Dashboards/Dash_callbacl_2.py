import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("data/gapminderDataFiveYear.csv")

app = dash.Dash()

# construct a dictionary of dropdown values for the years
year_options = []
for i in df["year"].unique():
    year_options.append({"label": str(i), "value": i})


app.layout = html.Div(
    [
        dcc.Graph(id="graph-with-slider"),
        dcc.Dropdown(id="year-picker", options=year_options, value=df["year"].min()),
    ]
)


@app.callback(Output("graph-with-slider", "figure"), [Input("year-picker", "value")])
def update_figure(selected_year):
    filtered_df = df[df["year"] == selected_year]
    traces = []
    for continent_name in filtered_df["continent"].unique():
        df_by_continent = filtered_df[filtered_df["continent"] == continent_name]
        traces.append(
            go.Scatter(
                x=df_by_continent["gdpPercap"],
                y=df_by_continent["lifeExp"],
                text=df_by_continent["country"],
                mode="markers",
                marker={"size": 15},
                name=continent_name,
            )
        )
    return {
        "data": traces,
        "layout": go.Layout(
            xaxis={"type": "log", "title": "GDP per Capita"},
            yaxis={"title": "Life expectancy"},
            hovermode="closest",
        ),
    }


if __name__ == "__main__":
    app.run_server()


"""
Callback's should never mutate variables outside of theri scope. if the callbacks modify global state, then one user's session might effect the next user's session and
when the app is deployed on multiple processes or threads, those modifications will not be shared across sessions.
"""
