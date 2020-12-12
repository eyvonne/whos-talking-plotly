import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go
import requests
import datetime
# from app import app

from . import BASE_URL



about_text = """
# About the API
This app was built based on a simple app that only tracked when a man versus woman was
talking. I did not build that app. I wanted some additional data to be tracked to truely
get information about who's dominating conversations (we've all done it) and if there are
any demographics that can be used to predict this.


## About the Author
I am a Data Scientist and technical educator. I built this app to track meetings as mentioned
above, and will only use the data collected to improve the app and make predictions. I'm
hoping to eventually add features that warn when someone is talking to much or try to
predict who will speak next."""


layout = dbc.Col([
    dbc.Row([dcc.Markdown(about_text)]),
])
