#!/usr/bin/env python
# coding: utf-8

# In[136]:


import numpy as np
import pandas as pd

df = pd.read_csv("NFIdatabase.csv",  names=['name', 'age', 'overall', 'value', 'potential', 'stamina', 'speed', 'diligence', 'Worth', 'Wage',
             'Value_Real', 'Wage_Real', 'Main_Position', 'position'])


def filter(context):
    # print("fas")
    if context.has_player is False:
        usr_budget = context.budget_amount

        usr_attr = context.category_attribute
        usr_quant = context.quantifier_attribute
        usr_role = context.category_player_role
        usr_budget = context.budget_amount
    else:
        usr_name = context.category_player

    #usr_attr = 'age'
    #usr_quant = 'young'
    #usr_role = 'striker'
    #usr_budget = 1000000

    df_output = pd.DataFrame()
    df_output = df[(df[usr_attr] == usr_quant) & (df['position'] == usr_role)]
    df_output = df_output.sort_values('overall', ascending=False)
    df_output = df_output[df_output['Value_Real'] <= usr_budget]

    df_output.loc[df_output.index[:3], ['name', 'Worth']].values






