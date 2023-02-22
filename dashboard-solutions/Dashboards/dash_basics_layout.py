import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {"background": "#111111", "text": "#7FDBFF"}

app.layout = html.Div(
    children=[
        html.H1(
            children="Hello Dash",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        html.Div(
            children="Dash: A web application framework for python",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "SF"},
                    {"x": [1, 2, 3], "y": [2, 4, 5], "type": "bar", "name": "Montreal"},
                ],
                "layout": {
                    "plot_bgcolor": colors["background"],
                    "paper_bgcolor": colors["background"],
                    "font": {"color": colors["text"]},
                    "title": "Dash Data Visualization",
                },
            },
        ),
    ],
    style={"backgroungColor": colors["background"]},
)

if __name__ == "__main__":
    app.run_server()

    """_summary_
    1) The 'style' property in HTML is a semicolon-separated string. In Dash, you can just supply a dict.
    2) The keys in the 'style' dictionary are camelCased. So, instead of text-align, it's textAlign.
    3) The HTML class attribute is className in Dash.
    4) The children of an HTML tag are specified through the children keyword argument.
        By convention, this is always the first argument and so it is often omitted.
        html.H1(children='Hello Dash') is same as html.H1('Hello Dash')
    """
