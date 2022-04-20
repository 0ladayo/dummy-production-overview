#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

import dash

import dash_bootstrap_components as dbc

from dash import html, dcc

from dash.dependencies import Input, Output

import plotly.express as px

from dash.dependencies import Input, Output

import plotly.graph_objects as go


# In[ ]:


def data():
    
    df_1 =pd.read_excel('gs://production-overview/production overview data.xlsx', sheet_name ='production')
    
    df_2 = pd.read_excel('gs://production-overview/production overview data.xlsx', sheet_name = 'wells details')
    
    return df_1, df_2

df_1, df_2 = data()


# In[ ]:


api_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


# In[ ]:


_app=dash.Dash(__name__,external_stylesheets=[dbc.themes.GRID])

app = _app.server

_app.layout=html.Div([
    
    dbc.Row([dbc.Col([html.Div(html.H1('COMPANY X PRODUCTION OVERVIEW',
                                     
                                     style={'font-family':'Open Sans','font-size':'24px','color':'rgb(96,96,96)'
                                            
                                             }))
                    
                     ])
            
    ]),
    
    html.Br(),
    
    dbc.Row([dbc.Col([html.Div([html.Span('Filter by year:',
                                     
                                     style={'font family': 'Open Sans','font-size':'15.3px','color':'black'}),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                dcc.RangeSlider(df_1['year'].min(), df_1.year.max(),1,
                                               
                                               value = [2009,2015],
                                               
                                               marks = {i: str(i) for i in range(df_1['year'].min(), df_1['year'].max() + 1, 1)},
                                               
                                               id ='my-range-slider'),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                dcc.RadioItems(
                                
                                options = [
                                    
                                    {'label':'All', 'value':'All'},
                                    
                                    {'label':'Active', 'value':'Active'},
                                    
                                    {'label':'Shut In', 'value':'Shut In'}
                                    
                                    
                                ], value = 'All', inline = True,
                                
                                style = {'font-family':'Open Sans', 'font-size':'17px','color':'rgb(96,96,96)'},
                                
                                inputStyle = {'margin-right':'3px'},
                                
                                labelStyle = {'margin-left':'30px'},
                                
                                id ='my-radio-items'),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Label('Select a well',
                                          
                                          style = {'font family': 'Open Sans','font-size':'15.3px','color':'black'}),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                dcc.Dropdown(id = 'wells_dropdown',
                                             
                                             options = [{'label': i, 'value': i} for i in df_2['wells'].unique()],
                                             
                                             value ='well 1',
                                             
                                             style={'width':'35%','font-family':'Open Sans','color':'black'}
                                            
                                            ),               
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                                
                                html.Br(),
                               
                               ], style = {'background-color':'rgb(249,249,249)', 'padding':'20px'}),
                      
                      
                    
                     ], md =4),
             
             dbc.Col([html.Div([
                 
                 dbc.Row([dbc.Col([html.Div([html.Span(id = 'no_of_wells',
                                                      
                                                      style = {'font-family':'Open Sans','font-size':'34px','color':'rgb(96,96,96)'}),
                                             
                                             html.Br(),
                                             
                                             html.Br(),
                                             
                                             html.Span('No of Wells',
                                                      
                                                      style = {'font-family':'Open Sans', 'font-size':'13.6px', 'color':'rgb(96,96,96)'})
                                            
                                            ], style = {'background-color':'rgb(249,249,249)', 'padding':'4px'})
                                  
                                  ],  md = 3),
                          
                          dbc.Col([html.Div([html.Span(id = 'oil_volume',
                                                       
                                                       style = {'font-family':'Open Sans','font-size':'34px','color':'rgb(96,96,96)'}),
                                             
                                             html.Br(),
                                             
                                             html.Br(),
                                             
                                             html.Span('Oil (bbl)',
                                                      
                                                      style = {'font-family':'Open Sans', 'font-size':'13.6px', 'color':'rgb(96,96,96)'})
                                            
                                            ], style = {'background-color':'rgb(249,249,249)', 'padding':'4px'})
                                  
                                  ],  md = 3),
                          
                           dbc.Col([html.Div([html.Span(id = 'gas_volume',
                                                       
                                                       style = {'font-family':'Open Sans','font-size':'34px','color':'rgb(96,96,96)'}),
                                             
                                             html.Br(),
                                             
                                             html.Br(),
                                             
                                             html.Span('Gas (mscf)',
                                                      
                                                      style = {'font-family':'Open Sans', 'font-size':'13.6px', 'color':'rgb(96,96,96)'})
                                            
                                            ], style = {'background-color':'rgb(249,249,249)', 'padding':'4px'})
                                  
                                  ],  md = 3),
                          
                          dbc.Col([html.Div([html.Span(id = 'water_volume',
                                                       
                                                       style = {'font-family':'Open Sans','font-size':'34px','color':'rgb(96,96,96)'}),
                                             
                                             html.Br(),
                                             
                                             html.Br(),
                                             
                                             html.Span('Water (bbl)',
                                                      
                                                      style = {'font-family':'Open Sans', 'font-size':'13.6px', 'color':'rgb(96,96,96)'})
                                            
                                            ], style = {'background-color':'rgb(249,249,249)', 'padding':'4px'})
                                  
                                  ],  md = 3),
                          
                         ]),
                 
                 html.Br(),
                 
                 html.Br(),
                 
                 dbc.Row([dbc.Col([
                     
                     dcc.Graph(id = 'wells_bar_chart',
                              
                              style = {'background-color':'rgb(249,249,249)'})
                 
                 ], md = 12)
                         
                         ])
             
             ])
                     
                     ], md =8)
            
            ]),
    
    html.Br(),
    
    html.Br(),
    
    html.Br(),
    
    dbc.Row([
        
        dbc.Col([html.Div([
            
            dcc.Graph(id = 'wells_satellite_map',
                      
                      style = {'background-color':'rgb(249,249,249)'})
        ])
                
                ], md = 6),
        
        dbc.Col([html.Div([
            
            dcc.Graph(id = 'wells_individual_chart',
                      
                      style = {'background-color':'rgb(249,249,249)'})
        
        ])
                ], md = 6)
    
    ]),
    
    html.Br(),
    
    html.Br(),
    
    dbc.Row([
        
        dbc.Col([html.Div([
            
            dcc.Graph(id = 'wells_aggregate_chart',
                      
                      style = {'background-color':'rgb(249,249,249)'})
        ])
                
                ], md = 12)
    
    ]),

])

@_app.callback(
    
    Output('no_of_wells', 'children'),
    
    Output('oil_volume', 'children'),
    
    Output('gas_volume', 'children'),
    
    Output('water_volume', 'children'),
    
    Output('wells_bar_chart', 'figure'),
    
    Output('wells_satellite_map','figure'),
    
    Output('wells_aggregate_chart', 'figure'),
    
    Input('my-range-slider', 'value'),
    
    Input('my-radio-items', 'value'))

def plot_update(years_chosen, wells_status):
    
    df_1_filtered_years = df_1[(df_1['year']>=years_chosen[0])&(df_1['year']<=years_chosen[1])]
    
    df_2_filtered_years = df_2[(df_2['year of completion']>=years_chosen[0])&(df_2['year of completion']<=years_chosen[1])]
    
    if wells_status == 'All':
        
        df_5_filtered_years = df_1[df_1['year']==years_chosen[1]]
        
        df_6_filtered_years = df_2_filtered_years[df_2_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())]['year of completion'].value_counts().rename_axis('year of completion').reset_index(name = 'counts')
        
        df_7_filtered_years = df_6_filtered_years[(df_6_filtered_years['year of completion']>=years_chosen[0])&(df_6_filtered_years['year of completion']<=years_chosen[1])]
    
        text1 = str(df_5_filtered_years['wells'].count())
        
        text2 = str(round(df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())]['oil production (bbl)'].sum()/1000000,2)) + 'M'
        
        text3 = str(round(df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())]['gas produced (mscf)'].sum()/1000,2)) + 'M'
        
        text4 = str(round(df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())]['water produced (bbl)'].sum()/1000000,2)) + 'M'
        
        figure1 = px.bar(df_7_filtered_years, x = 'year of completion', y  = 'counts')
        
        figure1.update_layout(plot_bgcolor = 'rgb(249,249,249)',paper_bgcolor='rgb(249,249,249)',title = {'text':'Completed Wells/Year','x':0.5})
        
        figure1.update_yaxes(fixedrange = True, gridcolor='rgb(233,233,233)')
        
        figure1.update_xaxes(fixedrange = True, linecolor='rgb(233,233,233)')
        
        figure1.update_traces(width = 0.1)
        
        figure2 = px.scatter_mapbox(df_2_filtered_years[df_2_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())], lat='Latitude', lon='Longitude',hover_name='wells', color_discrete_sequence = ['light blue'], zoom = 7)
        
        figure2.update_layout(mapbox_style = 'satellite-streets', mapbox_accesstoken = api_token)
        
        figure2.update_layout(margin=dict(l=20, r=20, t=30, b=20), title = {'text':'Satellite Overview', 'x':0.5})
        
        figure3 = go.Figure()
        
        figure3.add_trace(go.Scatter(x = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum().index, 
                                
                                y = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum()['oil production (bbl)'], line = dict(color = 'green', width = 0.3),
                                
                                 name = 'oil production (bbl)', line_shape='spline'))
    
        figure3.add_trace(go.Scatter(x = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum().index, 
                                
                                y = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum()['gas produced (mscf)'], line = dict(color = 'red', width = 0.3),
                                
                                name = 'gas produced (mscf)', line_shape='spline'))
    
        figure3.add_trace(go.Scatter(x = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum().index, 
                                
                                y = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum()['water produced (bbl)'], line = dict(color = 'blue', width = 0.3),
                             
                             name = 'water produced (bbl)', line_shape='spline'))
        
        figure3.update_layout(plot_bgcolor = 'rgb(249,249,249)',paper_bgcolor='rgb(249,249,249)', margin=dict(l=20, r=20, t=30, b=20), title = {'text':'Aggregate Production', 'x':0.5}, 
                           
                           legend = dict(orientation="h", yanchor="bottom", y=1, xanchor="right",x=1))
        
        figure3.update_yaxes(fixedrange = True, gridcolor='rgb(233,233,233)')
        
        figure3.update_xaxes(fixedrange = True, linecolor='rgb(233,233,233)', gridcolor='rgb(233,233,233)')
        
        return text1, text2, text3, text4, figure1, figure2, figure3
    
    elif wells_status == 'Active':
        
        df_5_filtered_years = df_1[(df_1['year']==years_chosen[1]) & (df_1['status']=='active')]
            
        df_6_filtered_years = df_2_filtered_years[df_2_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())]['year of completion'].value_counts().rename_axis('year of completion').reset_index(name = 'counts')
        
        df_7_filtered_years = df_6_filtered_years[(df_6_filtered_years['year of completion']>=years_chosen[0])&(df_6_filtered_years['year of completion']<=years_chosen[1])]
        
        text1 = str(df_5_filtered_years['wells'].count())
        
        text2 = str(round(df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())]['oil production (bbl)'].sum()/1000000,2)) + 'M'
        
        text3 = str(round(df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())]['gas produced (mscf)'].sum()/1000,2)) + 'M'
        
        text4 = str(round(df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())]['water produced (bbl)'].sum()/1000000,2)) + 'M'
        
        figure1 = px.bar(df_7_filtered_years, x = 'year of completion', y  = 'counts')
        
        figure1.update_layout(plot_bgcolor = 'rgb(249,249,249)',paper_bgcolor='rgb(249,249,249)', title = {'text':'Completed Wells/Year','x':0.5})
        
        figure1.update_yaxes(fixedrange = True, gridcolor='rgb(233,233,233)')
        
        figure1.update_xaxes(fixedrange = True, linecolor='rgb(233,233,233)')
        
        figure1.update_traces(width = 0.1)
        
        figure2 = px.scatter_mapbox(df_2_filtered_years[df_2_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())], lat='Latitude', lon='Longitude',hover_name='wells', color_discrete_sequence = ['light blue'], zoom = 7)
        
        figure2.update_layout(mapbox_style = 'satellite-streets', mapbox_accesstoken = api_token)
        
        figure2.update_layout(margin=dict(l=20, r=20, t=30, b=20), title = {'text':'Satellite Overview', 'x':0.5})
        
        figure3 =go.Figure()
        
        figure3.add_trace(go.Scatter(x = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum().index, 
                                
                                y = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum()['oil production (bbl)'], line = dict(color = 'green', width = 0.3),
                                
                                 name = 'oil production (bbl)', line_shape='spline'))
    
        figure3.add_trace(go.Scatter(x = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum().index, 
                                
                                y = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum()['gas produced (mscf)'], line = dict(color = 'red', width = 0.3),
                                
                                name = 'gas produced (mscf)', line_shape='spline'))
    
        figure3.add_trace(go.Scatter(x = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum().index, 
                                
                                y = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum()['water produced (bbl)'], line = dict(color = 'blue', width = 0.3),
                             
                             name = 'water produced (bbl)', line_shape='spline'))
        
        figure3.update_layout(plot_bgcolor = 'rgb(249,249,249)',paper_bgcolor='rgb(249,249,249)', margin=dict(l=20, r=20, t=30, b=20), title = {'text':'Aggregate Production', 'x':0.5}, 
                           
                           legend = dict(orientation="h", yanchor="bottom", y=1, xanchor="right",x=1))
        
        figure3.update_yaxes(rangemode='tozero', fixedrange = True, gridcolor='rgb(233,233,233)')
        
        figure3.update_xaxes(fixedrange = True, linecolor='rgb(233,233,233)', gridcolor='rgb(233,233,233)')
        
        return text1, text2, text3, text4, figure1, figure2, figure3
    
    elif wells_status == 'Shut In':
        
        df_5_filtered_years = df_1[(df_1['year']==years_chosen[1]) & (df_1['status']=='shut in')]
            
        df_6_filtered_years = df_2_filtered_years[df_2_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())]['year of completion'].value_counts().rename_axis('year of completion').reset_index(name = 'counts')
        
        df_7_filtered_years = df_6_filtered_years[(df_6_filtered_years['year of completion']>=years_chosen[0])&(df_6_filtered_years['year of completion']<=years_chosen[1])]
        
        text1 = str(df_5_filtered_years['wells'].count())
        
        text2 = str(round(df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())]['oil production (bbl)'].sum()/1000000,2)) + 'M'
        
        text3 = str(round(df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())]['gas produced (mscf)'].sum()/1000,2)) + 'M'
        
        text4 = str(round(df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())]['water produced (bbl)'].sum()/1000000,2)) + 'M'
        
        figure1 = px.bar(df_7_filtered_years, x = 'year of completion', y  = 'counts')
        
        figure1.update_layout(plot_bgcolor = 'rgb(249,249,249)',paper_bgcolor='rgb(249,249,249)', title = {'text':'Completed Wells/Year','x':0.5})
        
        figure1.update_yaxes(fixedrange = True, gridcolor='rgb(233,233,233)')
        
        figure1.update_xaxes(fixedrange = True, linecolor='rgb(233,233,233)')
        
        figure1.update_traces(width = 0.02)
        
        figure2 = px.scatter_mapbox(df_2_filtered_years[df_2_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())], lat='Latitude', lon='Longitude',hover_name='wells', color_discrete_sequence = ['light blue'], zoom = 7)
        
        figure2.update_layout(mapbox_style = 'satellite-streets', mapbox_accesstoken = api_token)
        
        figure2.update_layout(margin=dict(l=20, r=20, t=30, b=20), title = {'text':'Satellite Overview', 'x':0.5})
        
        figure3 =go.Figure()
        
        figure3.add_trace(go.Scatter(x = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum().index, 
                                
                                y = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum()['oil production (bbl)'], line = dict(color = 'green', width = 0.3),
                                
                                 name = 'oil production (bbl)', line_shape='spline'))
    
        figure3.add_trace(go.Scatter(x = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum().index, 
                                
                                y = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum()['gas produced (mscf)'], line = dict(color = 'red', width = 0.3),
                                
                                name = 'gas produced (mscf)', line_shape='spline'))
    
        figure3.add_trace(go.Scatter(x = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum().index, 
                                
                                y = df_1_filtered_years[df_1_filtered_years['wells'].isin (df_5_filtered_years['wells'].unique())].groupby('year')['oil production (bbl)', 'gas produced (mscf)', 'water produced (bbl)'].sum()['water produced (bbl)'], line = dict(color = 'blue', width = 0.3),
                             
                             name = 'water produced (bbl)', line_shape='spline'))
        
        figure3.update_layout(plot_bgcolor = 'rgb(249,249,249)',paper_bgcolor='rgb(249,249,249)', margin=dict(l=20, r=20, t=30, b=20), title = {'text':'Aggregate Production', 'x':0.5}, 
                           
                           legend = dict(orientation="h", yanchor="bottom", y=1, xanchor="right",x=1))
        
        figure3.update_yaxes(rangemode='tozero', fixedrange = True, gridcolor='rgb(233,233,233)')
        
        figure3.update_xaxes(fixedrange = True, linecolor='rgb(233,233,233)', gridcolor='rgb(233,233,233)')
        
        return text1, text2, text3, text4, figure1, figure2, figure3
    
@_app.callback(
    
    Output('wells_individual_chart', 'figure'),
    
    Input('wells_dropdown', 'value'))

def plot_update2(wells_name):
    
    
    figure4 =go.Figure()

    figure4.add_trace(go.Scatter(x = df_1[df_1['wells']==wells_name]['year'], 
                                
                                y = df_1[df_1['wells']==wells_name]['oil production (bbl)'], line = dict(color = 'green', width = 0.3),
                                
                                 name = 'oil production (bbl)', line_shape='spline'))
    
    figure4.add_trace(go.Scatter(x = df_1[df_1['wells']==wells_name]['year'], 
                                
                                y = df_1[df_1['wells']==wells_name]['gas produced (mscf)'], line = dict(color = 'red', width = 0.3),
                                
                                name = 'gas produced (mscf)', line_shape='spline'))
    
    figure4.add_trace(go.Scatter(x = df_1[df_1['wells']==wells_name]['year'], 
                                
                                y = df_1[df_1['wells']==wells_name]['water produced (bbl)'], line = dict(color = 'blue', width = 0.3),
                             
                             name = 'water produced (bbl)', line_shape='spline'))
     
    figure4.update_layout(plot_bgcolor = 'rgb(249,249,249)',paper_bgcolor='rgb(249,249,249)', margin=dict(l=20, r=20, t=30, b=20), 

                       title = {'text':'Individual Well Production:' + ' ' + str(wells_name),'x':0.5},

                       legend=dict(orientation="h", yanchor="bottom", y=1.,xanchor="right",x=1))

    figure4.update_yaxes(rangemode='tozero',fixedrange=True, gridcolor='rgb(233,233,233)')

    figure4.update_xaxes(range=[df_1[df_1['wells']==wells_name]['year'].min(),df_1[df_1['wells']==wells_name]['year'].max()],linecolor='rgb(233,233,233)', gridcolor='rgb(233,233,233)')

    return figure4

if __name__ == '__main__':
    
    _app.run_server(debug=True)
    

