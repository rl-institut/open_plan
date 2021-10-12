

import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
path_to_time_series = "timeseries_all_busses.xlsx"
path_to_json = 'json_input_processed.json'
path_to_demand = 'heat_demand.csv'
text=open(path_to_json,'r')
x=text.read()

y=json.loads(x)
data=pd.DataFrame(y)




df_ts = pd.read_excel(path_to_time_series)

df_demand = pd.read_csv(path_to_demand)

df_demand.columns = ['heat_demand']
#df_demand = -df_demand
print(df_demand[df_demand.columns[0]])




df_concat = pd.concat([df_ts[df_ts.columns[:]], df_demand], axis=1)
df_concat





fig = px.line(df_concat, x=df_concat.columns[0], y= df_concat.columns[1:], title='Load profile',line_shape='hv')
fig.show()





fig = go.Figure()
fig = px.area(df_concat, x=df_concat.columns[0], y=df_concat.columns[1:-1],title='Load profile')

fig.add_trace(go.Scatter(
    x=df_ts[df_ts.columns[0]],
    y=df_demand[df_demand.columns[0]],
    name='demand'))

fig.show()



fig = go.Figure()
#fig = px.area(df_concat, x=df_concat.columns[0], y=df_concat.columns[1:-1],title='Load profile')

fig.add_trace(go.Scatter(
    x=df_ts[df_ts.columns[0]],
    y=df_demand[df_demand.columns[0]],
    name='demand',
    line=go.scatter.Line(shape='hv')))

fig.add_trace(go.Scatter(
    x=df_ts[df_ts.columns[0]],
    y=df_ts[df_ts.columns[1]]*4.5, ### multiplied with conversion factor from transformer
    name='grid_el',
    stackgroup='one',
    mode='none',
    fillcolor='rgba(0, 155, 255, 0.3)',
    line=go.scatter.Line(shape='hv')))


fig.add_trace(go.Scatter(
    x=df_ts[df_ts.columns[0]],
    y=df_ts[df_ts.columns[2]]*4.5, ### multiplied with conversion factor from transformer
    name='pv',
    stackgroup='one',
    mode='none',
    line=go.scatter.Line(shape='hv')))

fig.add_trace(go.Scatter(
    x=df_ts[df_ts.columns[0]],
    y=df_ts[df_ts.columns[3]]*4.5, ### multiplied with conversion factor from transformer
    name='el_excess',
    stackgroup='one',
    mode='none',
    fillcolor='rgba(255, 0, 0, 0.5)',
    line=go.scatter.Line(shape='hv')))

fig.show()






