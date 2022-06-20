# -*- coding: utf-8 -*-
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




df2=px.data.election()
geojson = px.data.election_geojson() # to customize map locations

#///////////////////header
colors = {
    'background': '#111111',
    'bodyColor':'#F2DFCE',
    'text': '#7FDBFF'
}
def get_page_heading_style():
    return {'backgroundColor': "#FFD07B"}


def get_page_heading_title():
    return html.H1(children='Election Dashboard',
                                        style={
                                        'textAlign': 'center',
                                        'color': "#8C6841"
                                    })
#/////////////////////////////////


#///////////////////bins part

def generate_card_content(card_header,card_value,overall_value):
    card_head_style = {'textAlign':'center','fontSize':'150%'}
    card_body_style = {'textAlign':'center','fontSize':'200%'}
    card_header = dbc.CardHeader(card_header,style=card_head_style)
    card_body = dbc.CardBody(
        [
            html.H5(f"{int(card_value):,}", className="card-title",style=card_body_style),
        
            #html.P(
               # "Total Districts : {:,}".format(overall_value),
                #className="card-text",style={'textAlign':'center'}
            #)
            
        
        ]
    )
    card = [card_header,card_body]
    return card


def generate_cards(cntry='US'):
   
    cards = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(dbc.Card(generate_card_content("Coderre",len(df2[df2["winner"]=="Coderre"]),len(df2)), color="#E45826", inverse=True),md=dict(size=2,offset=3)),#"success"
                    dbc.Col(dbc.Card(generate_card_content("Bergeron",len(df2[df2["winner"]=="Bergeron"]),len(df2)), color="warning", inverse=True),md=dict(size=2)),
                    dbc.Col(dbc.Card(generate_card_content("Joly",len(df2[df2["winner"]=="Joly"]),len(df2)),color="#446A46", inverse=True),md=dict(size=2)),
                ],
                className="mb-4", style={"margin": 20,'backgroundColor':"#E6D5B8"}
            ),
        ],id='card1'
    )
    return cards
#////////////////////////////////



#////////////////////////////////////////////////////map part
# first map
fig1_map = px.choropleth(df2, geojson=geojson,color=df2[df2["winner"]=="Coderre"]["Coderre"],color_continuous_scale='ylorbr' ,
                    locations=df2[df2["winner"]=="Coderre"]["district"]
                     ,featureidkey="properties.district"
                  ,labels={"locations":"District","color":" Votes Number"},
                     
                   )
fig1_map.update_geos(fitbounds="locations", visible=False)
fig1_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0},plot_bgcolor="#E6D5B8",paper_bgcolor="#E6D5B8")


#second map

fig2_map = px.choropleth(df2, geojson=geojson, color=df2[df2["winner"]=="Bergeron"]["Bergeron"],color_continuous_scale='solar' ,
                    locations=df2[df2["winner"]=="Bergeron"]["district"],
                    featureidkey="properties.district",
                  #  hover_data=["total"]
                  labels={"locations":"District","color":" Votes Number"},
                   
                   )
fig2_map.update_geos(fitbounds="locations", visible=False)
fig2_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0},plot_bgcolor="#E6D5B8",paper_bgcolor="#E6D5B8")


#third map

fig3_map = px.choropleth(df2, geojson=geojson, color=df2[df2["winner"]=="Joly"]["Joly"],color_continuous_scale='greens' ,
                    locations=df2[df2["winner"]=="Joly"]["district"], featureidkey="properties.district",
                  #  hover_data=["total"]
                #    ,labels={"district":" "},
                labels={"locations":"District","color":" Votes Number"},
                   
                   )
fig3_map.update_geos(fitbounds="locations", visible=False)
fig3_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0},plot_bgcolor="#E6D5B8",paper_bgcolor="#E6D5B8")


#///// cards body for all maps

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            
            html.Div(dcc.Graph(figure=fig1_map),className="four columns")
        ],class_name="four columns"
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            
            html.Div([
       
       html.Div(dcc.Graph(figure=fig2_map),className="four columns"),
       
        ])
        ]
    ),
    className="mt-3",
)
tab3_content = dbc.Card(
    dbc.CardBody(
        [
           
                 html.Div([
       html.Div(dcc.Graph(figure=fig3_map),className="four columns"),
        ])
        ]
        
    ),
    className="mt-3",
)
#///////////////



#//////////////////////////////////////////////////////////
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
     dbc.Row([
         html.Br(),
         html.Br()
         ],style={"margin": 20,'backgroundColor':"#E6D5B8" })
    
     ,
     dbc.Row([
         dbc.Col([html.H2("Which Districts did the Candidate win?")],width={'size': 8, "offset": 3, 'order': "last"},style={'color': "#8C6841"})
         ],style={"margin": 40,'backgroundColor':"#E6D5B8"})
  ,    
     html.Div([
          
             
         dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Coderre", activeTabClassName = "fw-bold fst-italic", active_label_style={"color": "#E45826"}),
        dbc.Tab(tab2_content, label="Bergeron", activeTabClassName = "fw-bold fst-italic", active_label_style={"color": "#F0A500"}),
        dbc.Tab(tab3_content, label="Joly", activeTabClassName = "fw-bold fst-italic", active_label_style={"color": "#446A46"},style={'color': "yellow"}),
        
       
    ],style={"margin": 20,"align":"center",'TextAlign':'center','backgroundColor': "#FFD07B"}#"margin": 20,
),
      
         
         ],   style={'backgroundColor': "#E6D5B8"}),
     
     
     
     
     
     
     
     
     
     
     
     dbc.Row([
         
         html.Br(),
         dbc.Col([html.H4("Select District")],width={'size': 4,"offset": 1},style={'color': "#8C6841"}),
         dbc.Col([],width={'size': 2})
         ,
         
        
         
         ],style={"margin": 20})#'backgroundColor': "#E6D5B8",

     ,
     dbc.Row([
         dbc.Col([dcc.Dropdown(id="list1",options=[{'label':str(c),'value':str(c)} for c in df2["district"].unique()],value="101-Bois-de-Liesse")],width={'size': 5},style={'color': "#8C6841"})
         ,dbc.Col([],width={'size': 2})
         
         ,dbc.Col([dbc.RadioItems( id="radios1",options=[{"label": "Coderre", "value": 0},{"label": "Bergeron", "value": 1},{ "label": "Joly", "value": 2}],value='3', inline=True)],)
         
         ],style={'backgroundColor':"#E6D5B8","margin": 20 })
    
     ,
     dbc.Row([

         dbc.Col([html.H3("Votes For Each Candidate")],width={'size': 4, "offset": 0.5, 'order': 1},style={'color': "#8C6841"})#,style={'color': "yellow"},className='four columns') #figure=fig stack
         ,
         dbc.Col([html.H3("Candidate Votes Across All Regions")], width={'size': 5, "offset": 0, 'order': 2},style={'color': "#8C6841"})#,className='four columns')#figure=fig3  box
        ,
       
         dbc.Col([html.H3("Majority & Plurality")],width={'size': 3,  "offset": 0, 'order': 3},style={'color': "#8C6841"})
         
         ],style={"margin": 40})
     
     
     
    
     
     
     ,
     
     
       dbc.Row([
            
            dbc.Col([dcc.Graph(id="g_stack")],width={'size': 4, "offset": 0, 'order': 1})#,style={'color': "yellow"},className='four columns') #figure=fig stack
            ,
            dbc.Col([dcc.Graph(id="g_box")], width={'size': 4, "offset": 0.5, 'order': 2})#,className='four columns')#figure=fig3  box
           , 
            dbc.Col([dcc.Graph(id="g_hist")],width={'size': 4,  "offset": 0.5, 'order': 3})#,className='four columns')#(figure=fig2 #hist
            ],style={'backgroundColor': "#E6D5B8"})
       
        ,
        
        
        
        
    
        dbc.Row([
            html.Br(),
            html.Br()
            ],style={"margin": 20,'backgroundColor':"#E6D5B8" })
       
        
      
        
     ],style={'backgroundColor':"#E6D5B8" } #"#F2DFCE"
    )




@app.callback(
    Output(component_id="g_stack", component_property='figure'),
    
    
    #State(component_id='list1', component_property='value'),
    Input(component_id='list1', component_property='value')
    )
def action(dist):
    global df2
    #filter=df[(df['year']==year) and (df["continent"]==continent)] error 
    fig = px.bar(df2[df2["district"]==dist], x="district", y=['Coderre','Bergeron','Joly'],
            labels={"variable":"Candidate","value":"Votes"}   , color_discrete_sequence =["#E45826","#F0A500","#446A46"],barmode = 'stack',width=500,height=500)#,title="Number of votes for each candidate in the district"
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
        fig2=px.histogram(df2[df2["winner"]=="Coderre"],x="result",pattern_shape="result",width=500,height=500,color_discrete_sequence=["#E45826"],labels={"count":"Total District"})#,title="Number of districts won by the candidate (majority & plurality)"
        fig3=px.box(df2,y="Coderre",width=500,height=500,color_discrete_sequence=["#E45826"])#,title="Distribution of votes for the candidate across all regions"
    
    
    elif name==1:
        fig2=px.histogram(df2[df2["winner"]=="Bergeron"],x="result",pattern_shape="result",width=500,height=500,color_discrete_sequence=["#F0A500"],labels={"count":"Total District"})#,title="Number of districts won by the candidate (majority & plurality)"
        fig3=px.box(df2,y="Bergeron",width=500,height=500,color_discrete_sequence=["#F0A500"])#,title="Distribution of votes for the candidate across all regions"
    else:
        fig2=px.histogram(df2[df2["winner"]=="Joly"],x="result",pattern_shape="result",width=500,height=500,color_discrete_sequence=["#446A46"],labels={"count":"Total District"})#,title="Number of districts won by the candidate (majority & plurality)"
        fig3=px.box(df2,y="Joly",width=500,height=500,color_discrete_sequence=["#446A46"])#,title="Distribution of votes for the candidate across all regions"
       
    
    return fig3,fig2



'''
The `dash_bootstrap_components.RadioItems` component (version 1.0.3) with the ID "radios1" received an unexpected keyword argument: `display`
# Allowed arguments: className, class_name, id, inline, inputCheckedClassName, inputCheckedStyle, inputClassName, inputStyle, input_checked_class_name, input_checked_style, input_class_name, input_style, key, labelCheckedClassName, labelCheckedStyle, labelClassName, labelStyle, label_checked_class_name, label_checked_style, label_class_name, label_style, loading_state, name, options, persisted_props, persistence, persistence_type, style, switch, value


'''




app.run_server()