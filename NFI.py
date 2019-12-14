#!/usr/bin/env python
# coding: utf-8

# In[352]:


import numpy as np 
import pandas as pd

my_data = pd.read_csv("data.csv", delimiter=",")


# In[353]:

#aasfasfa
my_data.columns[:]


# In[354]:


cols = [
       'ID','Name', #Common info
       'Contract Valid Until', #contract duration
       'Age', #young or experienced
       'Value','Wage', #Value or wage - cheap or expensive
       'Position', #position
       'Potential', #potential
       'Preferred Foot', #L or R foot
       'Height',#tall
       'Overall', #overall
       'Work Rate', #hardworking
       'Crossing','Agility','Acceleration','SprintSpeed','Dribbling', #speed
       'Balance','Jumping', 'Stamina', 'Strength', #physical status
       'Finishing', 'LongShots','ShotPower','HeadingAccuracy','LS', 'ST', 'RS', 'LF', 'CF', 'RF', #striker
       'ShortPassing', 'LongPassing','LW', 'RW','LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LDM',
       'CDM', 'RDM',   #midfielder        
       'Interceptions', 'Positioning', 'Vision', 'Composure','StandingTackle','Marking', 'SlidingTackle','LWB','RWB', 
       'LB', 'LCB', 'CB', 'RCB', 'RB', #defender
       'GKDiving', 'GKHandling','GKKicking', 'GKPositioning', 'GKReflexes', 'GKHandling' #GK
]


# In[ ]:





# In[355]:


colcol = []
for i in my_data:
    if not i in cols:
        colcol.append(str(i))
my_data = my_data.drop(colcol, axis=1)


# In[356]:


my_data.dropna(axis='rows', inplace = True)


# In[357]:


my_data.isnull().sum().sum()


# In[358]:


my_data.set_index('ID', inplace = True)


# In[359]:


my_data["Value_"] = my_data["Value"].replace({'€': '','K': '*1e3', 'M': '*1e6'}, regex=True).map(pd.eval).astype(int)
my_data["Wage_"] = my_data["Wage"].replace({'€': '','K': '*1e3', 'M': '*1e6'}, regex=True).map(pd.eval).astype(int)


# In[360]:


my_data['Contract Valid Until'] = my_data['Contract Valid Until'].str[-4:]


# In[361]:


my_data["duration"] = my_data['Contract Valid Until'].apply(lambda x: int(x)-2019)


# In[362]:


rent_cost = []
for i in range(0,len(my_data["duration"].values)):
    rent_cost.append(int(my_data['Wage_'].values[i])*my_data['duration'].values[i])
my_data["Rent_cost"] = rent_cost


# In[363]:


my_data.count()
my_data.head()


# In[364]:


#my_data['Work Rate'] = my_data['Work Rate'].str.split('/')
my_data['Work Rate'] = my_data['Work Rate'].str.split('/').str[0]


# In[365]:


#my_data["Height"].str.split(' ').str[0]


# In[366]:


my_data["Height"] = my_data["Height"].apply(lambda x: x.replace("'",'.'))
my_data["Height"] = my_data["Height"].apply(lambda x: float(x)*30.48)
my_data["Height"] = my_data["Height"].round(1)


# In[367]:


my_data.iloc[:5, :]


# In[368]:


#pd.to_numeric(my_data['Value_'], errors='coerce')
my_data['Value_'] = my_data['Value_'].astype('float64')
my_data['Wage_'] = my_data['Wage_'].astype('float64')


# In[369]:


df1 = pd.DataFrame()


# In[370]:


new_index = my_data.index
df1["Age"] = my_data["Age"]
df1["Overall"] = my_data["Overall"]
df1["Value"] = my_data["Value_"]
df1["Height"] = my_data["Height"]
df1["Work_Rate"] = my_data["Work Rate"]
df1["Potential"] = my_data["Potential"]
df1["PhysicalStat"] = my_data.loc[:, ['Balance','Jumping', 'Stamina', 'Strength']].mean(axis =1).round(1)
df1["Speed"] = my_data.loc[:, ["Crossing","Agility","Acceleration","SprintSpeed","Dribbling"]].mean(axis =1).round(1)
df1["Striker"] = my_data.loc[:, ['Finishing', 'LongShots','ShotPower','HeadingAccuracy','LS', 'ST', 'RS', 'LF', 'CF', 'RF']].mean(axis =1).round(1)
df1["Midfielder"] = my_data.loc[:, ['ShortPassing', 'LongPassing','LW', 'RW','LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LDM',
       'CDM', 'RDM']].mean(axis =1).round(1)
df1["Defender"] = my_data.loc[:, ['Interceptions', 'Positioning', 'Vision', 'Composure','StandingTackle','Marking', 'SlidingTackle','LWB','RWB', 
       'LB', 'LCB', 'CB', 'RCB', 'RB']].mean(axis =1).round(1)
df1["GoalKeeper"] = my_data.loc[:, ['GKDiving', 'GKHandling','GKKicking', 'GKPositioning', 'GKReflexes', 'GKHandling']].mean(axis =1).round(1)
df1.set_index(new_index, inplace = False)
df1.head()


# In[371]:


#df.dtypes


# In[372]:


df = pd.DataFrame()


# In[383]:


df["Name"] =my_data["Name"]
df["Age"] = pd.cut(df1["Age"], 3, labels = ["young","mid age", "old"])
df["Overall"] = pd.cut(df1["Overall"], 5, labels = ["very bad", "bad","average", "good", "excellent"])
df["Value"] = pd.cut(df1["Value"], 5, labels = ["very cheap","cheap", "average", "expensive", "very expensive"])
df["Potential"] = pd.cut(df1["Potential"], 5, labels = ["very poor", "poor","average", "good", "excellent"])
df["PhysicalStatus"] = pd.cut(df1["PhysicalStat"], 5, labels = ["very poor", "poor","average", "good", "excellent"])

df["Speed"] =pd.cut(df1["Speed"], 5, labels = ["very slow", "slow","average", "fast", "very fast"])
df["Diligence"] =df1["Work_Rate"] #Filter with capital Letters !!!
df["Worth"] =my_data["Value"]  #To show the Value
df["Wage"] =my_data["Wage"]  #To show the wage
df["Value_Real"] = my_data["Value_"] #To sort
df["Wage_Real"] = my_data["Wage_"] #To sort
df["Main_Position"] = my_data["Position"]


# In[384]:


#df.iloc[500:550,0:]


# In[385]:


df_output = pd.DataFrame()
def querry(criteria, wish):
    df_output = df[(df[criteria]==wish)]
    print(df_output.iloc[:3,:])


# In[386]:
df_output = pd.DataFrame()
def querry2(*args):
    df_output = df[(df['Diligence']==args)]
    print(df_output.iloc[:3,:])


defender = ['LWB','RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB']
midfielder = ['LW', 'RW','LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LDM','CDM', 'RDM']
striker = ['LS', 'ST', 'RS', 'LF', 'CF', 'RF']
goalkeeper = ['GK']

#df.assign(Role = "")
#value_list = []
#pos_list = [defender, midfielder, striker, goalkeeper]
#pos_names = ["defender", "midfielder", "striker", "goalkeeper"]
#for ix,i in enumerate(pos_list):
#   for bx, b in enumerate(df['Main_Position']):
#        for ax, a in enumerate(i):
#            if a == b:
#                df['Role'].iloc[bx] = pos_names[ix]

#budget
#attribute
#quantifier
#name
#role


def filter(context):
    #print("fas")
    if context.has_player is False:
        usr_budget = context.budget_amount

        usr_attr = context.category_attribute
        usr_quant = context.quantifier_attribute
        usr_role = context.category_player_role
    else:
        usr_name = context.category_player
    print(df[(df['Age'] == usr_attr)]) #& (df['Value_Real'] <= usr_budget)])
  # (df['Role'] == usr_role) &

#import moneyball.NFI as nfi
 nfi.filter(context)

    #df[(df['Value'] == "very cheap") & (df['PhysicalStatus'] == "good") &
    #(df['Age'] == "young") & (df['Potential'] == "excellent")].sort_values(by=['Value_Real'], ascending=True)
