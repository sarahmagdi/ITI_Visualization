# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:20:37 2022

@author: kareem
"""

from dash import Dash,html,dcc
from dash.dependencies import Input,Output
app=Dash()
app.layout=html.Div([
    dcc.Input(
        id='input1',
        placeholder='Enter value',
        type='text',
        #value=''
        ),
    html.Div(id='div2')
    
    ]
    
    
    )


@app.callback(
    Output(component_id='div2', component_property='children'),
    Input(component_id='input1', component_property='value')
    )
def action(inputfor_fun):
    if inputfor_fun==None:
        return "no value !"
    else:
        return "you write:{}".format(inputfor_fun)

app.run_server()