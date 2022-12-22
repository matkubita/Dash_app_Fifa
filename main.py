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
    df = pd.read_csv("C:/Users/Uzytkownik/PycharmProjects/dash_lib/international_matches.csv")

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
            html.Div([
                html.Div([
                    html.H1("FIFA WORLD CUP", style={"margin-bottom": "0px", 'color': 'white'}),
                    html.H5("DATA ANALYSIS BY MATEUSZ KUBITA", style={"margin-top": "0px", 'color': 'white'}),
                ])
            ], className="twelve columns", id="title"),



        ], id="header", className="row flex-display", style={"margin-bottom": "25px"}),

        html.Div([
            html.Div([
                html.H6(children='Scored goals',
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),
                html.Div(id="zdobyte_gole123",
                         style={
                           'textAlign': 'center',
                           'color': '#D6DBD2',
                           'fontSize': 40}),
                html.P(id="last_game_goals",
                       style={
                           'textAlign': 'center',
                           'color': 'orange',
                           'fontSize': 15,
                           'margin-top': '-18px'}
                       ),



                ], className="card_container three columns",
            ),

            html.Div([
                html.H6(children='Conceded goals',
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),
                html.Div(id="stracone_bramki123",
                         style={
                             'textAlign': 'center',
                             'color': '#D6DBD2',
                             'fontSize': 40}
                         ),
                html.P(id="last_game_goals_stracone",
                       style={
                           'textAlign': 'center',
                           'color': 'orange',
                           'fontSize': 15,
                           'margin-top': '-18px'}
                       ),


            ], className="card_container three columns",

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

                dcc.Dropdown(id='country_selection',
                             multi=False,
                             clearable=True,
                             value='Poland',
                             placeholder='Select Countries',
                             options=df["home_team"].unique(), className='dcc_compon'),
                html.P('New Cases : ',
                       className='fix_label',
                       style={'color': 'white', 'text-align': 'center'}),

                dcc.Graph(id="graph_1",
                          config={'displayModeBar':False},
                          className='dcc_compon',
                          style={'margin-top':'20px'})


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
        Output('graph_1', component_property='figure'),
        Input("country_selection", component_property='value')
    )
    def update_graph_with_country_selection(user_input):
        dict_res = dash_2.analyze_team(user_input)

        zdobyte_gole = dict_res.get("zdobyte_gole")
        stracone_gole = dict_res.get("stracone")
        fig = go.Pie(labels=['Zdobyte Gole', 'Stracone gole'],
                     values=[32, 321])

        df = px.data.medals_long()
        fig = px.scatter(data_frame=df, x="count", y="nation", color="medal",
                         title="Elegancki Scatter Plot",
                         labels={
                             "count": "licznosc",
                             "nation": "Panstwo, nacja",
                             "medal": "jaki medal"
                         })

        df = px.data.tips()
        fig = px.pie(df, values='tip', names='day', color_discrete_sequence=px.colors.sequential.RdBu)

        fig = go.Figure(go.Sunburst(
            labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
            parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
            values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
        ))
        fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))


        zdobyte_gole = dict_res.get("zdobyte_gole")
        stracone_gole = dict_res.get("stracone_gole")
        mecze = dict_res.get("rozegrane_mecze")

        fig = go.Figure(go.Sunburst(
            labels=['rozegrane mecze', 'zdobyte gole', 'stracone gole'],
            parents=['', 'rozegrane mecze', 'rozegrane mecze'],
            values=[mecze, zdobyte_gole, stracone_gole],
        ))
        fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
        # return fig
        colors = ['orange', '#dd1e35', 'green']
        # '#e55467'



        return {
            'data': [go.Pie(labels=['rozegrane mecze', 'zdobyte gole', 'stracone gole'],
                            values=[mecze, zdobyte_gole, stracone_gole],
                            marker=dict(colors=colors),
                            hoverinfo='label+value+percent',
                            textinfo='label+value',
                            textfont=dict(size=13),
                            hole=.7,
                            rotation=45
                            # insidetextorientation='radial',

                            )],

            'layout': go.Layout(
                # width=800,
                # height=520,
                plot_bgcolor='#1f2c56',
                paper_bgcolor='#1f2c56',
                hovermode='closest',
                title={
                    'text': 'Total Cases : fds',

                    'y': 0.93,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                titlefont={
                    'color': 'white',
                    'size': 20},
                legend={
                    'orientation': 'h',
                    'bgcolor': '#1f2c56',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.07},
                font=dict(
                    family="sans-serif",
                    size=12,
                    color='white')
            ),

        }



    @app.callback(
        Output('zdobyte_gole123','children'),
        [Input('country_selection', component_property='value')]
    )
    def updateZdobyteGole(user_input):
        dict_res = dash_2.analyze_team(user_input)
        zdobyte_gole = dict_res.get("zdobyte_gole")
        return zdobyte_gole

    @app.callback(
        Output('last_game_goals', 'children'),
        [Input('country_selection', component_property='value')]
    )
    def updateZdobyteGole(user_input):
        dict_res = dash_2.analyze_team(user_input)
        zdobyte_gole = dict_res.get("last_game_goals")
        return "Last game:" + str(zdobyte_gole)

    @app.callback(
        Output('stracone_bramki123', 'children'),
        [Input('country_selection', component_property='value')]
    )
    def updateStraconeBramki(user_input):
        dict_res = dash_2.analyze_team(user_input)
        stracone = dict_res.get("stracone_gole")
        return stracone

    @app.callback(
        Output('last_game_goals_stracone', 'children'),
        [Input('country_selection', component_property='value')]
    )
    def updateStraconeBramkiOstatnie(user_input):
        dict_res = dash_2.analyze_team(user_input)
        stracone = dict_res.get("last_game_goals_stracone")
        return "Last game:" + str(stracone)











    # run the app
    app.run_server(port=8052)


    #maybe take the data from world championship soccer 2022 !!! ->


if __name__ == '__main__':
    main()
