import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

# df = pd.read_csv('data/2018WinterOlympics.csv')
# # print(df.head())

# trace1 = go.Bar(x=df['NOC'], y=df['Gold'], marker={
#                 'color': '#ffd700'}, name='Gold')
# trace2 = go.Bar(x=df['NOC'], y=df['Silver'], marker={
#                 'color': '#c0c0c0'}, name='Silver')
# trace3 = go.Bar(x=df['NOC'], y=df['Bronze'], marker={
#                 'color': '#cd7f32'}, name='Bronze')

# # data = [go.Bar(x=df['NOC'], y=df['Total'])]
# data = [trace1, trace2, trace3]
# layout = go.Layout(title='Medals', barmode='stack')
# fig = go.Figure(data, layout)
# pyo.plot(fig)

df = pd.read_csv('data/mocksurvey.csv', index_col=0)
# print(df.head())

data = [go.Bar(y=df.index, x=df[i], name=i, orientation='h')
        for i in df.columns]
layout = go.Layout(title='Mock Survey', barmode='stack')
fig = go.Figure(data, layout)
pyo.plot(fig)
