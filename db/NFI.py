#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd

df = pd.read_csv("db/NFIdatabase.csv",
                 names=['name', 'age', 'overall', 'value', 'potential', 'stamina', 'Average_', 'speed', 'diligence',
                        'Worth', 'Wage',
                        'Value_Real', 'Wage_Real', 'Main_Position', 'position'])


def get_request_players(context):
    # print("fas")
    # context.has_player_name = True
    if context.has_player_name is False:
        usr_budget = context.budget_amount

        usr_attr = context.category_attribute
        usr_quant = context.quantifier_attribute
        usr_role = context.category_player_role

    else:
        usr_name = context.category_player

    # usr_attr = 'age'
    # usr_quant = 'young'
    # usr_role = 'striker'
    # usr_budget = 10000000

    df_output = pd.DataFrame()

    df['Value_Real'] = df['Value_Real'].astype(int)
    df_filtered = df[df['Value_Real'] < int(usr_budget)]
    df_output = df_filtered[(df_filtered[usr_attr] == usr_quant) & (df_filtered['position'] == usr_role)]
    df_output = df_output.sort_values('overall', ascending=True)

    df_screen = df_filtered.loc[df_filtered.index[:5], ['name', 'Worth', 'Average_', 'potential', 'Value_Real']]
    df_screen['Average_'] = df_screen['Average_'].astype(str) + '/' + '100'
    df_screen.columns = ['Player Name', 'Market Value', 'Overall Score', 'Player Talent', 'Value_Real']
    df_screen = df_screen.sort_values('Value_Real', ascending=True)
    df_screen = df_screen.reset_index()
    df_screen.reindex(['1', '2', '3', '4', '5'])
    print(df_screen.iloc[:, 1:-1])
