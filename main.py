from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash_2
from dash import html
import assets


def main():

    #initialize the app with theme
    app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])

    #get data frame
    df = px.data.medals_long()

    #building components
    my_title = dcc.Markdown(children='My first graph in DASH')
    my_graph = dcc.Graph(figure={})
    dropdown = dcc.Dropdown(options=['Bar Plot', 'Scatter Plot'],
                            value='Bar Plot',
                            clearable=False)


    #customize layout
    # app.layout = dbc.Container([my_title, my_graph,dropdown])

    app.layout = html.Div([
        html.Div([
            #...
            html.Div([
                html.Div([
                    html.H3("Covid - 19", style={"margin-bottom": "0px", 'color': 'white'}),
                    html.H5("Track Covid - 19 Cases", style={"margin-top": "0px", 'color': 'white'}),
                ])
            ], className="twelve columns", id="title"),



        ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),

        html.Div([
            html.Div([
                html.H6(children='Global Cases',
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),

                html.P(f"{754}",
                       style={
                           'textAlign': 'center',
                           'color': 'orange',
                           'fontSize': 40}
                       ),

                html.P('new:  321',
                       style={
                           'textAlign': 'center',
                           'color': 'orange',
                           'fontSize': 15,
                           'margin-top': '-18px'}
                       )], className="card_container three columns",
            ),

            html.Div([
                html.H6(children='Global Deaths',
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),

                html.P(f"{532}",
                       style={
                           'textAlign': 'center',
                           'color': '#dd1e35',
                           'fontSize': 40}
                       ),

                html.P('new:',
                       style={
                           'textAlign': 'center',
                           'color': '#dd1e35',
                           'fontSize': 15,
                           'margin-top': '-18px'}
                       )], className="card_container three columns",
            ),

            html.Div([
                html.H6(children='Global Recovered',
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),

                html.P(f"{5325}",
                       style={
                           'textAlign': 'center',
                           'color': 'green',
                           'fontSize': 40}
                       ),

                html.P('new: 4324 ',
                       style={
                           'textAlign': 'center',
                           'color': 'green',
                           'fontSize': 15,
                           'margin-top': '-18px'}
                       )], className="card_container three columns",
            ),

            html.Div([
                html.H6(children='Global Active',
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),

                html.P(f"{5325}",
                       style={
                           'textAlign': 'center',
                           'color': '#e55467',
                           'fontSize': 40}
                       ),

                html.P('new: 6436 ',
                       style={
                           'textAlign': 'center',
                           'color': '#e55467',
                           'fontSize': 15,
                           'margin-top': '-18px'}
                       )], className="card_container three columns")

        ], className="row flex-display"),

        html.Div([
            html.Div([

                html.P('Select Country:', className='fix_label', style={'color': 'white'}),

                dcc.Dropdown(id='w_countries',
                             multi=False,
                             clearable=True,
                             value='321',
                             placeholder='Select Countries',
                             options=['321','42'], className='dcc_compon'),
                html.P('New Cases : ',
                       className='fix_label',
                       style={'color': 'white', 'text-align': 'center'})



            ], className="create_container three columns", id="cross-filter-options"),

        ], className="row flex-display"),

        html.Div([
            html.Div([
                html.H6(children='Global Cases',
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        )

        ], className="row flex-display"),

        ], id = 'cos', style={"display": "flex", "flex-direction": "column"})

        ],
        id="mainContainer",
        style={"display": "flex", "flex-direction": "column"}

    )

    #allowing components to interact with each other
    @app.callback(
        Output(my_graph, component_property='figure'),
        Input(dropdown, component_property='value')
    )
    def update_graph(user_input):
        dict_res = dash_2.analyze_team("Poland")
        if (user_input=='Bar Plot'):


            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=dict_res.get("zdobyte_gole"),
                title={'text': "Zdobyte gole"},
                domain={'x': [0, 1], 'y': [0, 1]}
            ))
        elif (user_input=="Scatter Plot"):
            zdobyte_gole = dict_res.get("zdobyte_gole")
            stracone_gole = dict_res.get("strcone_gole")
            fig = go.Pie(labels=['Zdobyte Gole', 'Stracone gole'],
                         values=[zdobyte_gole, stracone_gole])
        return fig

    # run the app
    app.run_server(port=8052)


    #maybe take the data from world championship soccer 2022 !!! ->


if __name__ == '__main__':
    main()
