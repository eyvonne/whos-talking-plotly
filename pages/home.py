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
# Who's Talking
This app was created to track participation in meetings and group conversations.
On the next screen you will be asked a few questions about who's participating in your
meeting and be able to enter some demographic details about them. Names will only be used
to generate an internal ID that will not be linked with the name after your meeting
has ended. All other data collected is for information purposes only and will be used
to generate a report at the end of your meeting. """

start_meeting = dbc.Button("Start Meeting", color="primary", size="lg", block=True)

layout = dbc.Col([
    dbc.Row([dcc.Markdown(about_text)]),
    dbc.Row([start_meeting])
])
