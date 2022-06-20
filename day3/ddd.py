from  dash import Dash,html,dcc
import dash_bootstrap_components as dbc

app = Dash(
    external_stylesheets=[dbc.themes.DARKLY]
)
app.title='eman'
card_content = [
   
    dbc.CardBody(
        [
            html.H5("Card title", className="card-title"),
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",
            ),
        ]
    ),
]

app.layout = html.Div(
    [
        dbc.Row(dbc.Col(html.H1('my dashboard'))),
         dbc.Row(
            [
                dbc.Col(dbc.Card(card_content, color="primary", inverse=True), style={'padding-left':'3%'}),
                dbc.Col(
                    dbc.Card(card_content, color="secondary", inverse=True)
                ),
                dbc.Col(dbc.Card(card_content, color="info", inverse=True)),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(dcc.Graph()),
                dbc.Col(dcc.Graph()),
                dbc.Col(dcc.Graph()),
            ]
        ),
    ]




)

if __name__ == "__main__":
    app.run_server()