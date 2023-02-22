import plotly.offline as pyo
import plotly.graph_objects as go

# y = [1, 13, 12, 34, 64, 63, 34, 86, 34, 11, 77, 31, 7, 42, 14, 67]

# data = [go.Box(
#     y=y,
#     boxpoints='outliers',  # disply the original points
#     jitter=0.3,  # spread them out so they all appear
#     pointpos=-1.8  # offset them to the left of the box
# )]

# pyo.plot(data)


""" The Quintus Curtius Snodrass Letters """

snodrass = [0.209, 0.205, 0.196, 0.210, 0.202, 0.207, 0.224, 0.223, 0.220, 0.201]
twain = [0.225, 0.262, 0.217, 0.240, 0.230, 0.229, 0.235, 0.217]

data = [go.Box(y=snodrass, name="QCS"), go.Box(y=twain, name="MT")]

layout = go.Layout(
    title="Comparison of three-letter-word frequencies<br>\
        between Quintus Curtius Snodrass and Mark Twain"
)
fig = go.Figure(data, layout)
pyo.plot(fig)
