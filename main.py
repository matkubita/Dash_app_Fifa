from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash_2


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
    app.layout = dbc.Container([my_title, my_graph,dropdown])

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
