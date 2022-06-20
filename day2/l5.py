# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:50:34 2022

@author: kareem
"""

from dash import Dash,html,dcc
from dash.dependencies import Input,Output,State

import plotly.express as px
global df
df=px.data.gapminder() 
'''
fig1=px.scatter(df,x="gdpPercap",y="lifeExp",size="pop",color="continent",animation_frame="year",size_max=50,hover_name="country",title="gdp as lifeEX",
          log_x=True,width=700,height=500,symbol="country",trendline="ols",template='seaborn',range_y=[0,100])
'''

app=Dash()
app.layout=html.Div([
    html.Div([
        html.Button(id="b1",children="submit",n_clicks=0),
        dcc.Graph(id="g1"),
        html.Br(),#new line
        dcc.Graph(id="g2"),
        html.Br(),#new line
        #dcc.Slider(0, len(df['year']), 1, marks={i: df['year'][i] for i in range(len(df['year'])+1)},value=4),
        dcc.Slider(id="slinder1",min=df['year'].min(), max=df['year'].max(), marks={str(years): str(years) for years in df['year'].unique()},value=df['year'].min()),
        
        dcc.Dropdown(id="list1",options=[{'label':str(c),'value':str(c)} for c in df["continent"].unique()],multi=True)
        #label which appear to user 
        ])
    
   
    
    
    ])


@app.callback(
    Output(component_id="g1", component_property='figure'),
    Output(component_id="g2", component_property='figure'),
    #Input(component_id='slinder1', component_property='value'),
    #Input(component_id='list1', component_property='value')
    State(component_id="slinder1", component_property='value'),
    State(component_id='list1', component_property='value'),
    Input(component_id='b1', component_property='n_clicks')
    )
def action(year,continent,n):
    global df
    #filter=df[(df['year']==year) and (df["continent"]==continent)] error 
    filter=df[(df.year==year) & (df.continent.isin(continent))]
    gg=px.scatter(filter,x="gdpPercap",y="lifeExp",color="continent",trendline='ols')
    return gg,gg




app.run_server()