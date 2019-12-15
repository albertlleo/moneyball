#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd

import pandas as pd


def get_request_players(context):
    df = pd.read_csv("db/NFIdatabase.csv", names=['name', 'age', 'overall',
                                               'value', 'potential', 'stamina', 'Nationality',
                                               'Club', 'International Reputation', 'Contract Valid Until',
                                               'Release Clause', 'Overall Score', 'speed',
                                               'diligence', 'Worth', 'Wage',
                                               'Value_Real', 'Wage_Real', 'Main_Position', 'position'])

    # context.has_player_name = True
    if context.has_player_name is False:
        usr_budget = context.budget_amount

        usr_attr = context.category_attribute
        usr_quant = context.quantifier_attribute
        usr_role = context.category_player_role

        df = df[df['Value_Real'] != 0]
        df['Value_Real'] = df['Value_Real'].astype(int)

        df_filtered = df[df['Value_Real'] < int(usr_budget)]
        #print(df_filtered)
        df_output = df_filtered[(df_filtered[usr_attr] == usr_quant) & (df_filtered['position'] == usr_role)]
        df_output = df_output.sort_values('overall', ascending=True)

        is_empty = df_output.empty
        print(is_empty)
        output = ""
        if is_empty:
            usr_budget = 10000000000
            df_output = df_filtered[(df_filtered[usr_attr] == usr_quant) & (df_filtered['position'] == usr_role)]
            df_output = df_output.sort_values('overall', ascending=True)

        df_screen = df_output.loc[
            df_output.index[:5], ['name', 'Worth', 'Overall Score', 'potential', 'Value_Real']]
        df_screen['Overall Score'] = df_screen['Overall Score'].astype(str) + '/' + '100'
        df_screen.columns = ['Player Name', 'Market Value', 'Overall Score', 'Player Talent', 'Value_Real']
        df_screen = df_screen.sort_values('Value_Real', ascending=False)
        df_screen = df_screen.reset_index()

        output = df_screen.iloc[:, 1:-1].to_string()
        return output

    else:
        usr_name = context.player_name
        df_filtered = df[df['name'].str.contains(usr_name)]
        df_screen = df_filtered.loc[
            df_filtered.index[:5], ['name', 'Worth', 'Overall Score', 'potential', 'Value_Real']]
        df_screen = df_screen.reset_index()

        output = df_screen.iloc[:, 1:-1].to_string()
        return output




    # usr_attr = 'age'
    # usr_quant = 'low'
    # usr_role = 'striker'
    # usr_budget = 10000000




