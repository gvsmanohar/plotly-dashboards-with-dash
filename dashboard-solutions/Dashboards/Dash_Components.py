"""
Dash Components
- html.Div([section]) : applies CSS to section page
- html.P() : paragraph
- html.H1('text') : heading (level1)
- html.Label('text') : label

# HTML elements and dash classes are mostly the same but there are a few key difference:
- The style property is a dictionary
- Properties in the style dictionary are camelCased
- The class key is renamed as className
- Style properties in pixel units can be supplied as just numbers without the px unit.
"""

import dash
from dash import html

app = dash.Dash()

app.layout = html.Div(
    [
        "This is the outermost Div",
        html.Div(
            "This is an inner Div",
            style={
                "color": "blue",
                "border": "2px blue solid",
                "borderRadius": 5,
                "padding": 10,
                "width": 220,
            },
        ),
        html.Div(
            "This is another inner Div",
            style={
                "color": "green",
                "border": "2px green solid",
                "margin": 10,
                "width": 220,
            },
        ),
    ],
    # this styles  the outermost div
    style={"width": 500, "height": 200, "color": "red", "border": "2px red dotted"},
)

if __name__ == "__main__":
    app.run_server()
