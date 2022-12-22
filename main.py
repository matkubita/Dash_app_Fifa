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
                html.H6(children='Games played',
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),

                html.Div(id="games_played_123",
                         style={
                             'textAlign': 'center',
                             'color': '#D6DBD2',
                             'fontSize': 40}
                         ),

            ], className="card_container three columns",
            ),

            html.Div([
                html.H6(children='Scores',
                        style={
                            'textAlign': 'center',
                            'color': 'white'}
                        ),

                html.Div(id='mean_offense123',
                         style={
                           'textAlign': 'center',
                           'color': '#D6DBD2',
                           'fontSize': 19}
                         ),
                html.Div(id='mean_defense123',
                         style={
                             'textAlign': 'center',
                             'color': '#D6DBD2',
                             'fontSize': 19}
                         ),
                html.Div(id='mean_field123',
                         style={
                             'textAlign': 'center',
                             'color': '#D6DBD2',
                             'fontSize': 19}
                         ),
                dcc.Graph(id='graph_score123',
                          config={'displayModeBar': False},
                          className='dcc_compon',
                          style={'margin-top': '20px'},
                          ),


            ], className="card_container three columns")

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

    @app.callback(
        Output('games_played_123', 'children'),
        [Input('country_selection', component_property='value')]
    )
    def updateGamesPlayed(user_input):
        dict_res = dash_2.analyze_team(user_input)
        mecze = dict_res.get("rozegrane_mecze")
        return str(mecze)

    @app.callback(
        Output('mean_offense123', 'children'),
        [Input('country_selection', component_property='value')]
    )
    def updateOffense(user_input):
        dict_res = dash_2.analyze_team(user_input)
        off = dict_res.get("mean_offense")
        return "Mean offense score: " + str(off)

    @app.callback(
        Output('mean_defense123', 'children'),
        [Input('country_selection', component_property='value')]
    )
    def updateDefense(user_input):
        dict_res = dash_2.analyze_team(user_input)
        defe = dict_res.get("mean_defense")
        return "Mean defense score: " + str(defe)

    @app.callback(
        Output('mean_field123', 'children'),
        [Input('country_selection', component_property='value')]
    )
    def updateMidfield(user_input):
        dict_res = dash_2.analyze_team(user_input)
        fieldmid = dict_res.get("mean_midfield")
        return "Mean midfield score: " + str(fieldmid)

    @app.callback(
        Output('graph_score123', 'figure'),
        [Input('country_selection', component_property='value')]
    )
    def updateGraphScore(user_input):
        dict_res = dash_2.analyze_team(user_input)
        score12 = dict_res.get("mean_midfield")

        labels = ['score', 'nic']
        values = [score12, 100 - score12]
        colors = ['green', 'white']

        # Use `hole` to create a donut-like pie chart
        fig = go.Figure(data=[go.Pie(labels=labels,
                                     values=values,
                                     hole=.7,
                                     showlegend=False)])
        fig.update_traces(marker=dict(colors=colors))
        fig.update_traces(textinfo='none')
        fig.add_annotation(text=str(score12),
                           font=dict(size=30, family='Verdana', color='black'),
                           showarrow=False)
        return {
            'data': [go.Pie(labels=labels,
                            values=values,
                            marker=dict(colors=colors),
                            textinfo='none',
                            textfont=dict(size=13),
                            showlegend=False,
                            hole=.7,
                            # insidetextorientation='radial',

                            )],

            'layout': go.Layout(
                # width=800,
                # height=520,
                plot_bgcolor='#1f2c56',
                paper_bgcolor='#1f2c56',
                hovermode='closest',
                annotations=[{
                    'text':str(score12),
                    'x':0.5,
                    'y':0.5,
                    'showarrow':False,
                    'font':{'size':30, 'family':'Verdana', 'color':'black'}}
                ],
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







    # run the app
    app.run_server(port=8052)


    #maybe take the data from world championship soccer 2022 !!! ->


if __name__ == '__main__':
    main()
