from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None

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

    # ad.2 liczba straconych goli
    gole_stracone_gdy_gospodarze = df_brazil.loc[df["home_team"] == "Brazil"]['away_team_score'].sum()
    gole_stracone_gdy_nie_gospodarze = df_brazil.loc[df["away_team"] == "Brazil"]['home_team_score'].sum()
    print(f"gole stracone gdy byli gospodarzami = {gole_stracone_gdy_gospodarze}")
    print(f"gole stracone gdy nie byli gospodarzami = {gole_stracone_gdy_nie_gospodarze}")
    gole_stracone_w_sumie =gole_stracone_gdy_gospodarze+gole_stracone_gdy_nie_gospodarze
    print(f"gole stracone w sumie {gole_stracone_w_sumie}")

    print(f"bilans goli (strzelone-stracone): {liczba_goli_suma-gole_stracone_w_sumie}")


    #ad.3 przeciwnik najtrudniejszy i naltwiejszy -> czyli z kim wygrali najwiecej meczow i z kim przegrali najwiecej meczow


    print(df.columns)

    df_licznosc_meczow = df_brazil.groupby(['home_team','away_team']).size().reset_index()
    print(df_licznosc_meczow)
    print("\n")
    # print(df_brazil.loc[(df_brazil['home_team'] == 'Brazil') & (df_brazil['away_team'] =='Australia')][['home_team','away_team']])


    result_column_win_or_lost = df_brazil.apply(lambda row: win_or_lost(row), axis=1)
    df_brazil['win_or_lost'] = result_column_win_or_lost

    print(df_brazil.head())

    df_wygrane = df_brazil[df_brazil['win_or_lost']==1].\
        groupby(['home_team','away_team'])['win_or_lost'].count()
    print(df_wygrane)

    df_przegrane = df_brazil[df_brazil['win_or_lost']==-1].\
        groupby(['home_team','away_team'])['win_or_lost'].count()



    df_remis = df_brazil[df_brazil['win_or_lost']==0].\
        groupby(['home_team','away_team'])['win_or_lost'].count()



    print("\n")


    pd_result = pd.merge(df_licznosc_meczow,df_wygrane, how='left', left_on=['home_team', 'away_team'], right_on=['home_team', 'away_team'])
    pd_result = pd.merge(pd_result, df_przegrane,how='left', left_on=['home_team', 'away_team'], right_on=['home_team', 'away_team'])
    pd_result = pd.merge(pd_result, df_remis,how='left', left_on=['home_team', 'away_team'], right_on=['home_team', 'away_team'])
    print(pd_result.columns)
    pd_result.rename(columns={'home_team' : 'home_team',
                            'away_team' : 'away_team',
                            0:'liczba_meczy',
                            'win_or_lost_x':'wygrane',
                            'win_or_lost_y':'przegrane',
                            'win_or_lost':'remis'}, inplace=True)
    pd_result.fillna(0,inplace=True)
    print(pd_result)
    print(pd_result.columns)

    print("\n")
    print("Brazylia VS Argentyna")
    print("Gdy Brazylia NIE byla gospodarzem: ")
    print(f"Rozegrali w sumie: {pd_result[(pd_result['home_team'] =='Argentina') & (pd_result['away_team']=='Brazil')].iloc[0]['liczba_meczy']} spotkan")
    print(f"Z czego wygrala Argentyna = {pd_result[(pd_result['home_team'] =='Argentina') & (pd_result['away_team']=='Brazil')].iloc[0]['wygrane']}")
    print(f"Z czego wygrala Brazylia = {pd_result[(pd_result['home_team'] =='Argentina') & (pd_result['away_team']=='Brazil')].iloc[0]['przegrane']}")
    print(f"Z czego REMIS = {pd_result[(pd_result['home_team'] =='Argentina') & (pd_result['away_team']=='Brazil')].iloc[0]['remis']}")


def win_or_lost(row):
    if row['home_team_score'] > row['away_team_score']:
        return 1
    elif row['home_team_score'] < row['away_team_score']:
        return -1
    return 0

def analyze_data():
    df = pd.read_csv("C:/Users/Uzytkownik/PycharmProjects/dash_lib/international_matches.csv")
    print(df.head(5))
    print(df.columns)
    print(df.info)
    print(df.describe())
    print(df.date)


if __name__ == '__main__':
    generate_graph_1()
