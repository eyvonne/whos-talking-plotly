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

title = dcc.Markdown('#### Add a person to your meeting')


name_input = dbc.FormGroup([
    dbc.Label("Name"),
    dbc.Input(type="text", id="name", placeholder="Enter Name"),
    dbc.FormText("Names will not be stored beyond your current meeting")
    ]
)

demographics = dbc.Label("Demographic imformation")

gender = dbc.FormGroup(
    [
        dbc.Label("Gender of best fit"),
        dbc.RadioItems(
            id='Gender_radios',
            options=[
                {"label": "Female", "value": "female"},
                {"label": "Male", "value": "male"},
                {"label": "None", "value": "none"},
                {"label": "Other", "value": "other"}
            ]
        ),
    ]
)


race = dbc.FormGroup(
    [
        dbc.Label("How do you describe yourself?"),
        dbc.RadioItems(
            id='race_radios',
            options=[
                {'label': 'Native American or Alaska Native', 'value': 'native'},
                {'label': 'Asian', 'value': 'asian'},
                {'label': 'Black or African American', 'value': 'black'},
                {'label': 'Native Hawaiian or Other Pacific Islander', 'value': 'hawaiian'},
                {'label': 'White', 'value': 'white'},
                {'label': "Other", "value": 'other'}
            ]
        ),
    ]
)


ethnicity = dbc.FormGroup(
    [
        dbc.Label("Are you of Hispanic, Latino, or of Spanish origin?"),
        dbc.RadioItems(
            id='ethnicity',
            options=[
                {'label': 'yes', 'value': 'true'},
                {'label': 'no', 'value': 'false'}
            ]
        )
    ]
)

age = dbc.FormGroup(
    [
        dbc.Label("Age"),
        dbc.Input(type="number", placeholder="Enter Age")
    ]
)

add_user = dbc.Button("Add another person", color="primary")

start_meeting = dbc.Button("Start Meeting", color='primary')

buttons = dbc.Row([add_user, html.Div(style={'width':'15px'}), start_meeting])

form = dbc.Form([name_input, gender, ethnicity, race, age, buttons])

disclaimer = dcc.Markdown("""
Demographic information is fundamentally a challenge to collect for the purposes of data
analytics. We have tried to include as broad a spectrum as possible, if you have feedback
on how we could better capture information or would like fields added, please contact us
using the button below.
""")

contact = dbc.Button('Contact Us/Feedback', color="info")

layout = dbc.Col([html.Div(style={'height': '15px'}), title, form, disclaimer, contact])
