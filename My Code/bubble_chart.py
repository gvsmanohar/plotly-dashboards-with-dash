import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd

# df = pd.read_csv('data/mpg.csv')
# # print(df.head())


# data = [go.Scatter(x=df['horsepower'], y=df['mpg'],
#                    mode='markers', text=df['name'], marker=dict(size=1.5*df['cylinders']))]
# layout = go.Layout(title='Vehicle mpg vs. Mileage', xaxis={'title': 'horsepower'}, yaxis=dict(
#     title='mpg'), hovermode='closest')
# fig = go.Figure(data, layout)
# pyo.plot(fig, filename='bubble.html')

"""__Exercise__
   Objective: Create a bubble chart that compares three other features from the mpg.csv dataset. 
   Fields include: 'mpg', 'cylinders', 'displacement' 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
   """
