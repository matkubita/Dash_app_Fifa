from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np
import pandas as pd

import dash_2


def main():

    #initialize the app with theme
    app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

    #get data frame
    df = px.data.medals_long()

    #building components
    my_title = dcc.Markdown(children='FIFA WORLD CUP DATA ANALYZIS')
    my_graph = dcc.Graph(figure={})
    dropdown = dcc.Dropdown(options=['Brazil', 'France'],
                            value='Brazil',
                            clearable=False)


    #customize layout
    app.layout = dbc.Container([my_title, my_graph,dropdown])

    #allowing components to interact with each other
    @app.callback(
        Output(my_graph, component_property='figure'),
        Input(dropdown, component_property='value')
    )
    def update_graph(user_input):
        if (user_input=='Brazil'):
            fig = px.bar(data_frame=df, x="nation", y="count", color="medal",
                         title="Elegancki bar plot")
        elif (user_input=="France"):
            fig = px.scatter(data_frame=df, x = "count", y="nation", color="medal",
                             title="Elegancki Scatter Plot",
                             labels={
                                 "count": "licznosc",
                                 "nation": "Panstwo, nacja",
                                 "medal":"jaki medal"
                             })
        return fig

    # run the app
    app.run_server(port=8052)


    #maybe take the data from world championship soccer 2022 !!! ->


if __name__ == '__main__':
    main()
