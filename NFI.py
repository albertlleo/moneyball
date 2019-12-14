#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd

df = pd.read_csv("NFIdatabase.csv",  names=['name', 'age', 'overall', 'value', 'potential', 'stamina', 'Average_', 'speed', 'diligence', 'Worth', 'Wage',
             'Value_Real', 'Wage_Real', 'Main_Position', 'position'])

def filter(context):
    # print("fas")
    context.has_player_name = True
    if context.has_player_name is False:
        usr_budget = context.budget_amount

        usr_attr = context.category_attribute
        usr_quant = context.quantifier_attribute
        usr_role = context.category_player_role

    else:
        usr_name = context.category_player

usr_attr = 'age'
usr_quant = 'young'
usr_role = 'striker'
usr_budget = 1000000

df_output = pd.DataFrame()
df_output = df[(df[usr_attr] == usr_quant) & (df['position'] == usr_role)]
df_output = df_output.sort_values('overall', ascending=True)

df_output['Value_R'] = df_output['Value_Real'].values.astype(int)
df_output = df_output[df_output['Value_R'] <= usr_budget]

df_screen = df_output.loc[df_output.index[:5], ['name', 'Worth', 'Average_', 'potential', 'Value_Real']]
df_screen['Average_'] = df_screen['Average_'].astype(str) + '/' + '100'
df_screen.columns = ['Player Name', 'Market Value', 'Overall Score', 'Player Talent', 'Value_Real']

df_screen = df_screen.sort_values('Value_Real', ascending=True)
df_screen = df_screen.reset_index()
df_screen.reindex(['1','2','3'])
print(df_screen.iloc[:,1:-1])




