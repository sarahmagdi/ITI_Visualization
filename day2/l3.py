# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:53:38 2022

@author: kareem
"""

from dash import Dash,html,dcc
import plotly.express as px
df=px.data.gapminder() 
fig1=px.scatter(df,x="gdpPercap",y="lifeExp",size="pop",color="continent",animation_frame="year",size_max=50,hover_name="country",title="gdp as lifeEX",
          log_x=True,width=700,height=500,symbol="country",trendline="ols",template='seaborn',range_y=[0,100])

app=Dash(external_stylesheets=["http://codepen.io/chriddyp/pen/bWLwgP.css"])
app.layout=html.Div(
    [dcc.Input(
        placeholder='Enter value',
        type='text',
        value=''
    ),
        html.Div([
    dcc.Dropdown(['option1', 'option2', 'option3'], 'option2', multi=True),
    dcc.Slider(0, 10, 1, marks={i: f'Label{i}' for i in range(11)},value=4),
    
   
]),
        html.Div([
            
            html.Div([dcc.Graph(figure=fig1)],className='six columns'),
            html.Div([dcc.Graph(figure={})],className='six columns')#figure=fig
            
            
            ])
        
        
        
        
     ]
    )


app.run_server()