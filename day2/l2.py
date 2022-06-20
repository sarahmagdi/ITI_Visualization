# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 09:35:55 2022

@author: kareem
"""

from dash import Dash,html,dcc
app=Dash(external_stylesheets=["http://codepen.io/chriddyp/pen/bWLwgP.css"])
app.layout=html.Div(children=[
    html.H1("Hello",style={'color': "yellow", 'fontSize': 40,'text-align':'center','border':3,'marginBotton':50#space as border
           ,"marginTop" :50               }),
    html.Div([
    html.Div(
        "DIV1",style={'color': "yellow", 'fontSize': 30,'text-align':'center'
                             }
        ,className='four columns')
    ,
    html.Div([
        html.P("the first paragraph",style={'color': 'green', 'fontSize': 30}),
        html.Br(),#new line
        html.P("the Second paragraph",style={'color': 'green', 'fontSize': 30}),
        html.Hr(style={'width':400})
        ],style={"backgroundColor":"yellow"},className='four columns'),
    html.Div("DIV3",style={'color': "yellow", 'fontSize': 30,'text-align':'center'
                         }
             ,className='four columns')
        #all columns =12 
        #when we use className='four columns' to make div take 4 columns from all
        #[dcc.Graph(figure=fig)]
        ])
    
    ],style={"backgroundColor":"green",'border':"3px blue dotted",'width':1400,'height':500})# div container or section
app.run_server()