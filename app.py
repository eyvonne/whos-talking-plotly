import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from pages import home, about, newMeeting

external_stylesheets = [
    dbc.themes.CERULEAN,  # Bootswatch theme
    "https://use.fontawesome.com/releases/v5.9.0/css/all.css",  # for social media icons
]

meta_tags = [{"name": "viewport",
              "content": "width=device-width, initial-scale=1"}]

app = dash.Dash(
    __name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags
)
app.config.suppress_callback_exceptions = True
app.title = "Who's Talking"  # appears in browser title bar
server = app.server


navbar = dbc.NavbarSimple(
    brand="Who's Talking",
    brand_href="/",
    children=[
        dbc.NavItem(dcc.Link("About The API", href="/about", className="nav-link")),
    ],
    sticky="top",
    color="dark",
    light=False,
    dark=True,
    style={"height": "50px"},
)

footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
                [
                    html.Span("Who's Talking", className="mr-2"),
                    html.A(
                        html.I(className="fas fa-envelope-square mr-1"),
                        href="mailto:quakelabs.ds.lambda@gmail.com",
                    ),
                    html.A(
                        html.I(className="fab fa-github-square mr-1"),
                        href="https://github.com/quake-labs",
                    ),
                ],
                className="lead",
            )
        )
    )
)


app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        navbar,
        dbc.Container(id="page-content", className="h-25"),
        html.Hr(),
        footer,
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/newmeeting":
        return newMeeting.layout
    elif pathname == "/histogram":
        return histogram.layout
    elif pathname == "/about":
        return about.layout
    elif pathname == "/tips":
        return tips.layout
    elif re.search("/quakedetail/*", str(pathname)):
        return detail.layout
    elif pathname == "/search":
        return search.layout
    elif pathname == "/signup":
        return signup.layout
    else:
        return dcc.Markdown("## Page not found")

if __name__ == '__main__':
    app.run_server(debug=True)
