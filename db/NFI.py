#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd

import pandas as pd



def get_request_players(context):
    df = pd.read_csv("db/NFIdatabase.csv", names=['name', 'age', 'overall',
                                                  'value', 'potential', 'stamina', 'Nationality',
                                                  'Club', 'International Reputation', 'Contract Valid Until',
                                                  'Overall Score', 'speed',
                                                  'diligence', 'Worth', 'Wage',
                                                  'Value_Real', 'Wage_Real', 'Main_Position', 'position',
                                                  'Release Clause'])

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
    # usr_budget = 1

    df_output = pd.DataFrame()

    df = df[df['Value_Real'] != 0]

    df['Value_Real'] = df['Value_Real'].astype(int)
    df_filtered = df[df['Value_Real'] < int(usr_budget)]
    df_output = df_filtered[(df_filtered[usr_attr] == usr_quant) & (df_filtered['position'] == usr_role)]
    df_output = df_output.sort_values('overall', ascending=True)


    isempty = df_output.empty
    if not isempty:

        df_screen = df_filtered.loc[
            df_filtered.index[:5], ['name', 'Worth', 'Overall Score', 'potential', 'Release Clause', 'Value_Real']]
        df_screen['Overall Score'] = df_screen['Overall Score'].astype(str) + '/' + '100'
        df_screen.columns = ['Player Name', 'Market Value', 'Overall Score', 'Player Talent', 'Release Clause',
                             'Value_Real']
        df_screen = df_screen.sort_values('Value_Real', ascending=False)
        df_screen = df_screen.reset_index()

        output = df_screen.iloc[:, 1:-1].to_string()
        return output
    else:
        output = ''
        return output


