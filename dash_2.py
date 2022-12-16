from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np
import pandas as pd


def main():
    print("bonjounrno")

    # "Wykres 1: Wybierasz dana druzyne a nastepnie"
    # Masz o tej druzynie tworzony dashboard
    # Liczba goli strzelonych w sumie, liczba straconych, bilans goli (strzelone - stracone)
    # Przeciwnik najtrudniejszy, przeciwnik najlatwiejszy
    # Najlepszy mecz, najgorszy mecz

    # Wykres 2: Wybierasz 2 druzyny i masz rozne dane
    # Kiedy jakie mecze byly i jakie byly wyniki

    # maybe take the data from world championship soccer 2022 !!! ->


def generate_graph_1():
    df = pd.read_csv("C:/Users/Uzytkownik/PycharmProjects/dash_lib/international_matches.csv")

    df_brazil = df[(df["home_team"] == "Brazil") | (df["away_team"] == "Brazil")]
    print(df_brazil)

    #ad.1 liczba strzelonych goli w sumie

    #gdy byli gospodarzami
    liczba_meczy_jako_gospodarz = len(df_brazil.loc[df["home_team"] == "Brazil"])
    liczba_goli_g = df_brazil.loc[df["home_team"] == "Brazil"]['home_team_score'].sum()
    print(f"Liczba goli jako gospodarze: {liczba_goli_g}")
    print(f"liczba meczy jako gospodarze: {liczba_meczy_jako_gospodarz}")

    #gdy nie byli gospodarzemi
    liczba_meczy_jako_nie_gospodarze = len(df_brazil.loc[df["away_team"] == "Brazil"])
    liczba_goli_ng = df_brazil.loc[df["away_team"] == "Brazil"]['away_team_score'].sum()
    print(f"Liczba goli jako NIE gospodarze: {liczba_goli_ng}")
    print(f"liczba meczy jako NIE gospodarze: {liczba_meczy_jako_nie_gospodarze}")

    liczba_meczy_suma = liczba_meczy_jako_nie_gospodarze + liczba_meczy_jako_gospodarz
    liczba_goli_suma = liczba_goli_g + liczba_goli_ng
    print(f"Liczba meczow w sumie: {liczba_meczy_suma} \n"
          f"liczba golow w sumie: {liczba_goli_suma}")


    #ad.2 liczba straconych goli


def analyze_data():
    df = pd.read_csv("C:/Users/Uzytkownik/PycharmProjects/dash_lib/international_matches.csv")
    print(df.head(5))
    print(df.columns)
    print(df.info)
    print(df.describe())
    print(df.date)


if __name__ == '__main__':
    generate_graph_1()
