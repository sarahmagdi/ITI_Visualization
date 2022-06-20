# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import dash
import dash_bootstrap_components as dbc
BS = "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
app = dash.Dash(external_stylesheets=[BS])

#app = dash.Dash( external_stylesheets=[dbc.themes.BOOTSTRAP] )

app.layout = dbc.Alert(
    "Hello, Bootstrap!", className="m-5"
)

if __name__ == "__main__":
    app.run_server()