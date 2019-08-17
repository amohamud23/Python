import plotly.plotly as py
import plotly.graph_objs as go
import numpy as mp

import pandas as pd

# Read data from a csv
i=0
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
x = mp.linspace(-2*mp.math.pi,2*mp.math.pi,100)
y = 20*mp.cos(x)
z = mp.linspace(20,20,100)
data = [
    go.Surface(
        z=[z,y]
    )
]
layout = go.Layout(
    title='Test',
    autosize=True,
    width=500,
    height=500,
    margin=dict(
        l=65,
        r=50,
        b=65,
        t=90
    )
)
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='elevations-3d-surface')