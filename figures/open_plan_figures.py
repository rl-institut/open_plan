#!/usr/bin/env python
# coding: utf-8

# In[135]:


import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
path_to_ts_scenario1 = "max_boegl/Szenario_1/timeseries_all_busses.xlsx"
path_to_json_scenario1 = 'max_boegl/Szenario_1/json_with_results.json'
path_to_ts_scenario2 = "max_boegl/Szenario_2/timeseries_all_busses.xlsx"
path_to_json_scenario2 = 'max_boegl/Szenario_2/json_with_results.json'
path_to_ts_scenario3 = "max_boegl/Szenario_3/timeseries_all_busses.xlsx"
path_to_json_scenario3 = 'max_boegl/Szenario_3/json_with_results.json'
path_to_ts_scenario4 = "max_boegl/Szenario_4/timeseries_all_busses.xlsx"
path_to_json_scenario4 = 'max_boegl/Szenario_4/json_with_results.json'
#path_to_demand = 'max_boegl/Szenario_1heat_demand.csv'

text1=open(path_to_json_scenario1,'r')
x1=text1.read()
y1=json.loads(x1)
data_scenario1=pd.DataFrame(y1)
 
text2=open(path_to_json_scenario2,'r')
x2=text2.read()
y2=json.loads(x2)
data_scenario2=pd.DataFrame(y2)
 
text3=open(path_to_json_scenario3,'r')
x3=text3.read()
y3=json.loads(x3)
data_scenario3=pd.DataFrame(y3)
 
text4=open(path_to_json_scenario4,'r')
x4=text4.read()
y4=json.loads(x4)
data_scenario4=pd.DataFrame(y4)


# In[136]:


print(data)


# In[150]:


pd.set_option('display.max_rows', None)


# In[151]:


column_name=data_scenario1.loc['scalar_matrix']['kpi']['columns']


# In[161]:


values = data_scenario1.loc['scalar_matrix']['kpi']['data']
df_scalar_matrix1 = pd.DataFrame(values, columns=column_name)
df_scalar_matrix1

values = data_scenario2.loc['scalar_matrix']['kpi']['data']
df_scalar_matrix2 = pd.DataFrame(values, columns=column_name)
df_scalar_matrix2

values = data_scenario3.loc['scalar_matrix']['kpi']['data']
df_scalar_matrix3 = pd.DataFrame(values, columns=column_name)
df_scalar_matrix3

values = data_scenario4.loc['scalar_matrix']['kpi']['data']
df_scalar_matrix4 = pd.DataFrame(values, columns=column_name)
df_scalar_matrix4


# In[153]:


data_scenario1.loc['scalar_matrix']['kpi']['data']


# In[154]:


df_ts = pd.read_excel(path_to_ts_scenario1)

df_demand = -df_ts['Industriepark']
df_dso_feedin = -df_ts['DSO_feedin']
df_pv = df_ts['pv_18']
df_dso_demand = df_ts['DSO_consumption']
df_wind_karholz = df_ts['wind_karholz']
df_wind_winnberg03 = df_ts['wind_winnberg03']
df_wind_winnberg04= df_ts['wind_winnberg04']

df = df_ts[df_ts.columns[1:7]]
df_total= df.sum(axis=1)


# In[155]:


fig = px.line(df_ts, x=df_ts.columns[0], y= df_ts.columns[1:], title='Load profile',line_shape='hv')
fig.show()


# In[177]:


fig = go.Figure()
n=24*7

df_ts_scope = df_ts[:n]

fig.add_trace(go.Scatter(
    x=df_ts_scope[df_ts_scope.columns[0]],
    y=df_total,
    name='feedin',
    line=go.scatter.Line(shape='hv',color='blue')))

fig.add_trace(go.Scatter(
    x=df_ts_scope[df_ts_scope.columns[0]],
    y=-df_ts_scope[df_ts_scope.columns[8]],
    name='demand',
    line=go.scatter.Line(shape='hv', color= 'red')))


#stackgroup
fig.add_trace(go.Scatter(
    x=df_ts_scope[df_ts_scope.columns[0]],
    y=df_ts_scope[df_ts_scope.columns[2]],
    name='pv',
    stackgroup='one',
    mode='none',
    fillcolor='yellow',
    line=go.scatter.Line(shape='hv')))


fig.add_trace(go.Scatter(
    x=df_ts_scope[df_ts_scope.columns[0]],
    y=df_ts_scope[df_ts_scope.columns[3]], ### multiplied with conversion factor from transformer
    name='wind_karholz',
    stackgroup='one',
    mode='none',
    line=go.scatter.Line(shape='hv')))

fig.add_trace(go.Scatter(
    x=df_ts_scope[df_ts_scope.columns[0]],
    y=df_ts_scope[df_ts_scope.columns[4]], ### multiplied with conversion factor from transformer
    name='wind_winneberg03',
    stackgroup='one',
    mode='none',
    line=go.scatter.Line(shape='hv')))

fig.add_trace(go.Scatter(
    x=df_ts_scope[df_ts_scope.columns[0]],
    y=df_ts_scope[df_ts_scope.columns[5]], ### multiplied with conversion factor from transformer
    name='wind_winneberg04',
    stackgroup='one',
    mode='none',
    line=go.scatter.Line(shape='hv')))

fig.add_trace(go.Scatter(
    x=df_ts_scope[df_ts_scope.columns[0]],
    y=df_ts_scope[df_ts_scope.columns[1]], ### multiplied with conversion factor from transformer
    name='dso',
    stackgroup='one',
    mode='none',
    line=go.scatter.Line(shape='hv')))


fig.show()


# In[164]:


df_scalar_matrix1


# In[172]:


df_scalar_matrix4


# In[158]:


import plotly.graph_objects as go




fig = go.Figure(go.Bar(x=['Szenario_1'], y=[df_scalar_matrix1['installedCap'][7]], name='PV', width = 0.5))                  #Kapazität aus Szenarien für Technologie 1 
fig.add_trace(go.Bar(x=['Szenario_1'], y=[df_scalar_matrix1['installedCap'][9]], name='wind_winneberg03', width = 0.5))              #Kapazität aus Szenarien für Technologie 2
fig.add_trace(go.Bar(x=['Szenario_1'], y=[df_scalar_matrix1['installedCap'][10]], name='wind_winneberg04', width = 0.5))     #Kapazität aus Szenarien für Technologie 3
fig.add_trace(go.Bar(x=['Szenario_1'], y=[df_scalar_matrix1['installedCap'][8]], name='wind_karholz', width = 0.5))
#fig.add_trace(go.Bar(x=['Szenario_1'], y=[df_scalar_matrix['installedCap'][7]], name='dso_in', width = 0.5))


fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'}, 
                  xaxis_title='Szenario', yaxis_title='Installierte Kapazität in kWp',
                  bargap=0)
fig.show()


# In[159]:


import plotly.graph_objects as go



fig = go.Figure(go.Bar(x=['Erzeugung', 'Verbrauch'], y=[df_scalar_matrix1['total_flow'][7], 0], name='PV', width = 0.5))                  #Kapazität aus Szenarien für Technologie 1 
fig.add_trace(go.Bar(x=['Erzeugung', 'Verbrauch'], y=[df_scalar_matrix1['total_flow'][0], 0], name='Netznutzung', width = 0.5))
fig.add_trace(go.Bar(x=['Erzeugung', 'Verbrauch'], y=[df_scalar_matrix1['total_flow'][9], 0], name='wind_winneberg03', width = 0.5))              #Kapazität aus Szenarien für Technologie 2
fig.add_trace(go.Bar(x=['Erzeugung', 'Verbrauch'], y=[df_scalar_matrix1['total_flow'][10], 0], name='wind_winneberg04', width = 0.5))     #Kapazität aus Szenarien für Technologie 3
fig.add_trace(go.Bar(x=['Erzeugung', 'Verbrauch'], y=[df_scalar_matrix1['total_flow'][8],0], name='wind_karholz', width = 0.5))
fig.add_trace(go.Bar(x=['Erzeugung', 'Verbrauch'], y=[0, df_scalar_matrix1['total_flow'][12]], name='Industriepark', width = 0.5))
fig.add_trace(go.Bar(x=['Erzeugung', 'Verbrauch'], y=[0, df_scalar_matrix1['total_flow'][1]], name='Netzeinspeisung', width = 0.5))

fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'}, 
                  xaxis_title='Szenario', yaxis_title='Gesamter Fluss in kWh',
                  bargap=0)
fig.show()


# In[174]:


import plotly.graph_objects as go

n = 4                                #Anzahl der Szenarien, die verglichen werden sollen

x=[str(chr(ord('@')+number)) for number in range(1,n+1)] 
#x = ['A','B','C','D']

# Eine Datenreihe für jede Technologie -> Wie viele Technologien werden pro Szenario verwendet? (betrachten hauptsächlich Producer)

fig = go.Figure(go.Bar(x=x, y=[df_scalar_matrix1['installedCap'][7], 
                               df_scalar_matrix2['installedCap'][10],
                               df_scalar_matrix3['installedCap'][11],
                               df_scalar_matrix4['installedCap'][14]], name='PV', width = 0.5))


fig.add_trace(go.Bar(x=x, y=[df_scalar_matrix1['installedCap'][9], 
                             df_scalar_matrix2['installedCap'][13],
                             df_scalar_matrix3['installedCap'][15],
                             df_scalar_matrix4['installedCap'][18]], name='wind_winneberg03', width = 0.5))              #Kapazität aus Szenarien für Technologie 2

fig.add_trace(go.Bar(x=x, y=[df_scalar_matrix1['installedCap'][10], 
                             df_scalar_matrix2['installedCap'][14],
                             df_scalar_matrix3['installedCap'][16],
                             df_scalar_matrix4['installedCap'][19]], name='wind_winneberg04', width = 0.5))     #Kapazität aus Szenarien für Technologie 3

fig.add_trace(go.Bar(x=x, y=[df_scalar_matrix1['installedCap'][8], 
                             df_scalar_matrix2['installedCap'][12], 
                             df_scalar_matrix3['installedCap'][14], 
                             df_scalar_matrix4['installedCap'][17]], name='wind_karholz', width = 0.5))

fig.add_trace(go.Bar(x=x, y=[0, 
                               df_scalar_matrix2['optimizedAddCap'][9],
                               df_scalar_matrix3['optimizedAddCap'][10],
                               df_scalar_matrix4['optimizedAddCap'][6]], name='PV_frei', width = 0.5))   #Kapazität aus Szenarien für Technologie 1 
fig.add_trace(go.Bar(x=x, y=[0, 
                               0,
                               df_scalar_matrix3['optimizedAddCap'][13],
                               df_scalar_matrix4['optimizedAddCap'][8]], name='Wind_erweiterung', width = 0.5))

fig.add_trace(go.Bar(x=x, y=[0, 
                               0,
                               0,
                               df_scalar_matrix4['optimizedAddCap'][0]], name='Batterie', width = 0.5))



fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'}, 
                  xaxis_title='Szenario', yaxis_title='Installierte Kapazität in kWp',
                  bargap=0)
fig.show()


# In[ ]:




