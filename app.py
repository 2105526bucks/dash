import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from dash import dash
import plotly.express as px

import flask; import plotly.express as px
import dash; import dash_core_components as dcc; import dash_html_components as html
from dash.dependencies import Input, Output

df = pd.read_csv(r"C:\Users\Rhiann.Nelson\Documents\DEAV resit\OxCGRT_summary200520_final.csv")
df.head(5)
df.duplicated().sum()

# Setup the app. The server & app names should match those in Procfile


fig =  px.bar(df, x="Continent_Name", y="ConfirmedCases", color="Continent_Name",
animation_frame="Date", animation_group="CountryName",
range_y=[0,2500000])
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
fig.write_html('Question3.html', auto_open=True)

server = flask.Flask(dashq3)

app = dash.Dash(dashq3, server=server)

app.layout = html.Div([ html.Br(),html.Br(),html.Label("Data Input"),
dcc.Dropdown(id="data1", options=[{'label': 'Confirmed Cases', 'value': 'ConfirmedCases'},{'label': 'Confirmed Deaths', 'value': 'Confirmed Deaths'},
                                  {'label': 'Stringency Index', 'value': 'StringencyIndex'}], value='ConfirmedCases'),
dcc.Graph(id="fig1",figure=fig)])
@app.callback(Output('fig1', 'figure'),[Input('data1', 'value')])

def updatefig(d): 
    if d =="ConfirmedCases": return figure
elif d == "ConfirmedDeaths": return px.bar(df, x="Continent_Name", y="ConfirmedDeaths", color="Continent_Name",
                    animation_frame="Date", animation_group="CountryName",
                    range_y=[0,2500000])
elif d =="StringencyIndex": return px.bar(df, x="Continent_Name", y="StringencyIndex", color="Continent_Name",
                    animation_frame="Date", animation_group="CountryName",
                    range_y=[0,150])
else: return px.bar(df, x="Continent_Name", y="ConfirmedCases", color="Continent_Name",
                    animation_frame="Date", animation_group="CountryName",
                    range_y=[0,2500000])
    app.server.run(debug=True, use_reloader=False)