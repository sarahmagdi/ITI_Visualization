# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 18:13:12 2022

@author: kareem
"""

"""
Created on Fri Apr 22 14:33:31 2022

@author: kareem
"""

from dash import Dash,html,dcc
from dash.dependencies import Input,Output,State
import dash_bootstrap_components as dbc
import plotly.express as px
global df
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
import pandas as pd
df3 = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

fig0 = px.choropleth(df3, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           scope="usa",
                           labels={'unemp':'unemployment rate'}
                          )


df2=px.data.election()
colors = {
    'background': '#111111',
    'bodyColor':'#F2DFCE',
    'text': '#7FDBFF'
}
def get_page_heading_style():
    return {'backgroundColor': "yellow"}


def get_page_heading_title():
    return html.H1(children='Election Dashboard',
                                        style={
                                        'textAlign': 'center',
                                        'color': colors['text']
                                    })


def generate_card_content(card_header,card_value,overall_value):
    card_head_style = {'textAlign':'center','fontSize':'150%'}
    card_body_style = {'textAlign':'center','fontSize':'200%'}
    card_header = dbc.CardHeader(card_header,style=card_head_style)
    card_body = dbc.CardBody(
        [
            html.H5(f"{int(card_value):,}", className="card-title",style=card_body_style),
            html.P(
                "area counts : {:,}".format(overall_value),
                className="card-text",style={'textAlign':'center'}
            ),
        ]
    )
    card = [card_header,card_body]
    return card


def generate_cards(cntry='US'):
   
    cards = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Card(generate_card_content("Coderre",len(df2[df2["winner"]=="Coderre"]),len(df2)), color="success", inverse=True),md=dict(size=2,offset=3)),
                    dbc.Col(dbc.Card(generate_card_content("Bergeron",len(df2[df2["winner"]=="Bergeron"]),len(df2)), color="warning", inverse=True),md=dict(size=2)),
                    dbc.Col(dbc.Card(generate_card_content("Joly",len(df2[df2["winner"]=="Joly"]),len(df2)),color="dark", inverse=True),md=dict(size=2)),
                ],
                className="mb-4",
            ),
        ],id='card1'
    )
    return cards
'''
fig = px.bar(df2[df2["district"]=="101-Bois-de-Liesse"], x="district", y=['Coderre','Bergeron','Joly']
           , barmode = 'stack',width=500,height=500)
 

fig2=px.histogram(df2[df2["winner"]=="Joly"],x="result",pattern_shape="result",width=500,height=500)#,width=800,height=500
fig3=px.box(df2,y="Joly",width=500,height=500)
'''
external_stylesheets = [dbc.themes.BOOTSTRAP]

#app=Dash(external_stylesheets=["http://codepen.io/chriddyp/pen/bWLwgP.css"])
app=Dash(__name__, external_stylesheets=external_stylesheets)
app.layout=html.Div(
    [
     html.Div([
         dbc.Row(
                            [
                                dbc.Col(get_page_heading_title(),md=12)
                            ],
                            align="center",
                            style=get_page_heading_style()
                        )
         ])
     
     ,
     generate_cards()
     
     
     ,
     html.Div([
         dcc.Graph(figure=fig0)
         ]),
     
       dbc.Row([
            
            dbc.Col([dcc.Graph(id="g_stack")],width={'size': 4, "offset": 0, 'order': 1})#,style={'color': "yellow"},className='four columns') #figure=fig stack
            ,
            dbc.Col([dcc.Graph(id="g_box")], width={'size': 4, "offset": 0.5, 'order': 2})#,className='four columns')#figure=fig3  box
           , 
            dbc.Col([dcc.Graph(id="g_hist")],width={'size': 4,  "offset": 0.5, 'order': 3})#,className='four columns')#(figure=fig2 #hist
            ])
        ,
        
        html.Div([
            
            html.Div([dcc.Dropdown(id="list1",options=[{'label':str(c),'value':str(c)} for c in df2["district"].unique()],value="101-Bois-de-Liesse")],className='five columns'),
            html.Div([dcc.Slider(id="slinder1",min=0, max=2,step=1, marks=["Coderre","Bergeron","Joly"],value=1)],className='seven columns')
            
            ],style={'backgroundColor': "yellow"})

        ,html.Div([
            
            dbc.RadioItems(
                id="radios1",options=[{"label": "Coderre", "value": 0},{"label": "Bergeron", "value": 1},{ "label": "Joly", "value": 2}],value='3', inline=True)
            
            
            
            ])
        
        
      
        
     ],style={'backgroundColor':"#F2DFCE" }
    )


'''
        html.Div([
            
            dbc.RadioItems(
                id="radios1",options=[{"label": "Coderre", "value": 0},{"label": "Bergeron", "value": 1},{ "label": "Joly", "value": 2}],value='3', inline=True)
            
            
            
            ])
'''

@app.callback(
    Output(component_id="g_stack", component_property='figure'),
    
    
    #State(component_id='list1', component_property='value'),
    Input(component_id='list1', component_property='value')
    )
def action(dist):
    global df2
    #filter=df[(df['year']==year) and (df["continent"]==continent)] error 
    fig = px.bar(df2[df2["district"]==dist], x="district", y=['Coderre','Bergeron','Joly']
               , color_discrete_sequence =['green',"darkcyan","red"],barmode = 'stack',width=500,height=500,title="Number of votes for each candidate in the district")
    return fig


@app.callback(
    Output(component_id="g_box", component_property='figure'),
    Output(component_id="g_hist", component_property='figure'),
    
    #Input(component_id='slinder1', component_property='value')
    Input(component_id="radios1", component_property='value')
    )
def action(name):
    global df2
    if name==0:
        fig2=px.histogram(df2[df2["winner"]=="Coderre"],x="result",pattern_shape="result",width=500,height=500,title="Number of districts won by the candidate (majority & plurality)")
        fig3=px.box(df2,y="Coderre",width=500,height=500,title="Distribution of votes for the candidate across all regions")
    elif name==1:
        fig2=px.histogram(df2[df2["winner"]=="Bergeron"],x="result",pattern_shape="result",width=500,height=500,title="Number of districts won by the candidate (majority & plurality)")
        fig3=px.box(df2,y="Bergeron",width=500,height=500,title="Distribution of votes for the candidate across all regions")
    else:
        fig2=px.histogram(df2[df2["winner"]=="Joly"],x="result",pattern_shape="result",width=500,height=500,title="Number of districts won by the candidate (majority & plurality)")
        fig3=px.box(df2,y="Joly",width=500,height=500,title="Distribution of votes for the candidate across all regions")
        
    
    return fig3,fig2



'''
The `dash_bootstrap_components.RadioItems` component (version 1.0.3) with the ID "radios1" received an unexpected keyword argument: `display`
# Allowed arguments: className, class_name, id, inline, inputCheckedClassName, inputCheckedStyle, inputClassName, inputStyle, input_checked_class_name, input_checked_style, input_class_name, input_style, key, labelCheckedClassName, labelCheckedStyle, labelClassName, labelStyle, label_checked_class_name, label_checked_style, label_class_name, label_style, loading_state, name, options, persisted_props, persistence, persistence_type, style, switch, value


'''




app.run_server()