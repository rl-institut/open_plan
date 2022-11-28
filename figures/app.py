import dash_core_components as dcc
import dash_html_components as html



import dash

# Initializes dash app
app = dash.Dash()





import pandas as pd
import numpy as np
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


def load_json(path):
    text=open(path,'r')
    x=text.read()
    y=json.loads(x)
    data_scenario=pd.DataFrame(y)
    return data_scenario

data_scenario1 = load_json(path_to_json_scenario1)

data_scenario2 = load_json(path_to_json_scenario2)

data_scenario3 = load_json(path_to_json_scenario3)

data_scenario4 = load_json(path_to_json_scenario4)


column_name=data_scenario1.loc['scalar_matrix']['kpi']['columns']

values = data_scenario1.loc['scalar_matrix']['kpi']['data']
df_scalar_matrix1 = pd.DataFrame(values, columns=column_name)


values = data_scenario2.loc['scalar_matrix']['kpi']['data']
df_scalar_matrix2 = pd.DataFrame(values, columns=column_name)


values = data_scenario3.loc['scalar_matrix']['kpi']['data']
df_scalar_matrix3 = pd.DataFrame(values, columns=column_name)


values = data_scenario4.loc['scalar_matrix']['kpi']['data']
df_scalar_matrix4 = pd.DataFrame(values, columns=column_name)


df_ts = pd.read_excel(path_to_ts_scenario1)

df_demand = -df_ts['Industriepark']
df_dso_feedin = -df_ts['DSO_feedin']
df_pv = df_ts['pv_18']
df_dso_demand = df_ts['DSO_consumption']
df_wind_karholz = df_ts['wind_karholz']
df_wind_winnberg03 = df_ts['wind_winnberg03']
df_wind_winnberg04= df_ts['wind_winnberg04']

df = df_ts[df_ts.columns[1:7]]
df_total= df.sum(axis=1)/1e3                   # for feedin
df_ts[df_ts.columns[1:]] = df_ts[df_ts.columns[1:]]/1e3

n = 24*21
m = 24*0
fig = px.line(df_ts[m:m+n], x=df_ts.columns[0], y= df_ts.columns[1:], title='Lastprofil',line_shape='hv',
              labels={
                  "value": "Leistung in MW",
                  "Unnamed: 0": "Zeit",
                  "variable": "Komponente"
              })

newnames = {'DSO_consumption':'Netznutzung',
            'pv_18': 'PV',
            'wind_karholz':'Wind - Karholz',
            'wind_winnberg03': 'Wind - Winnberg03',
            'wind_winnberg04' : 'Wind - Winnberg04',
            'DSO_feedin': 'Netzeinspeisung',
            'AC bus_excess_sink':'Überschuss',
            'Industriepark':'Strombedarf'}
fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                      )
                   )

#fig.update_layout(xaxis_title = 'Zeit', yaxis_title = 'Energie in kWh')
# fig.show()

#########################

fig1 = go.Figure()
x = df_ts[df_ts.columns[0]][m:m+n]
#df_total= df.sum(axis=1)/1e3                   # for feedin
#df_ts[df_ts.columns[1:]] = df_ts[df_ts.columns[1:]]/1e3
df_ts_scope = df_ts[:n]

#df_ts_scope= df_ts_scope[df_ts_scope.columns[1:]]/1e3

fig1.add_trace(go.Scatter(
    x=x,
    y=df_total,
    name='Netzeinspeisung',
    line=go.scatter.Line(shape='hv',color='blue')))

fig1.add_trace(go.Scatter(
    x=x,
    y=-df_ts_scope[df_ts_scope.columns[8]],
    name='Strombedarf',
    line=go.scatter.Line(shape='hv', color= 'red')))


#stackgroup
fig1.add_trace(go.Scatter(
    x=x,
    y=df_ts_scope[df_ts_scope.columns[2]],
    name='PV',
    stackgroup='one',
    mode='none',
    fillcolor='rgba(255,255,0,0.3)',
    line=go.scatter.Line(shape='hv')))


fig1.add_trace(go.Scatter(
    x=x,
    y=df_ts_scope[df_ts_scope.columns[3]], ### multiplied with conversion factor from transformer
    name='Wind - Karholz',
    stackgroup='one',
    mode='none',
    fillcolor='rgba(0,0,255,0.3)',
    line=go.scatter.Line(shape='hv')))

fig1.add_trace(go.Scatter(
    x=x,
    y=df_ts_scope[df_ts_scope.columns[4]], ### multiplied with conversion factor from transformer
    name='Wind - Winnberg03',
    stackgroup='one',
    mode='none',
    fillcolor='rgba(30,144,255,0.3)',
    line=go.scatter.Line(shape='hv')))

fig1.add_trace(go.Scatter(
    x=x,
    y=df_ts_scope[df_ts_scope.columns[5]], ### multiplied with conversion factor from transformer
    name='Wind - Winnberg04',
    stackgroup='one',
    mode='none',
    fillcolor='rgba(0,255,255,0.3)',
    line=go.scatter.Line(shape='hv')))

fig1.add_trace(go.Scatter(
    x=x,
    y=df_ts_scope[df_ts_scope.columns[1]], ### multiplied with conversion factor from transformer
    name='Netznutzung',
    stackgroup='one',
    mode='none',
    fillcolor='rgba(255,0,0,0.3)',
    line=go.scatter.Line(shape='hv')))

fig1.update_layout(yaxis_title='Leistung in MW')

# fig.show()


#######
fig2 = go.Figure()
import plotly.graph_objects as go

n = 4                                #Anzahl der Szenarien, die verglichen werden sollen

#x=[str(chr(ord('@')+number)) for number in range(1,n+1)]
#x = ['A','B','C','D']
x = ['1','2','3','4']

# Eine Datenreihe für jede Technologie -> Wie viele Technologien werden pro Szenario verwendet? (betrachten hauptsächlich Producer)

fig2 = go.Figure(go.Bar(x=x, y=[df_scalar_matrix1['installedCap'][7]/1e3,
                               df_scalar_matrix2['installedCap'][10]/1e3,
                               df_scalar_matrix3['installedCap'][11]/1e3,
                               df_scalar_matrix4['installedCap'][14]/1e3], name='PV', width = 0.5,marker_color= 'yellow'))

colors = ['yellow','blue','teal','aqua','red','gold','dodgerblue','blueviolet','silver','maroon','indigo']
fig2.add_trace(go.Bar(x=x, y=[df_scalar_matrix1['installedCap'][8]/1e3,
                             df_scalar_matrix2['installedCap'][12]/1e3,
                             df_scalar_matrix3['installedCap'][14]/1e3,
                             df_scalar_matrix4['installedCap'][17]/1e3], name='Wind - Karholz', width = 0.5,marker_color= 'blue'))


fig2.add_trace(go.Bar(x=x, y=[df_scalar_matrix1['installedCap'][9]/1e3,
                             df_scalar_matrix2['installedCap'][13]/1e3,
                             df_scalar_matrix3['installedCap'][15]/1e3,
                             df_scalar_matrix4['installedCap'][18]/1e3], name='Wind - Winnberg03', width = 0.5, marker_color= 'teal'))              #Kapazität aus Szenarien für Technologie 2

fig2.add_trace(go.Bar(x=x, y=[df_scalar_matrix1['installedCap'][10]/1e3,
                             df_scalar_matrix2['installedCap'][14]/1e3,
                             df_scalar_matrix3['installedCap'][16]/1e3,
                             df_scalar_matrix4['installedCap'][19]/1e3], name='Wind - Winnberg04', width = 0.5, marker_color= 'aqua'))     #Kapazität aus Szenarien für Technologie 3


fig2.add_trace(go.Bar(x=x, y=[0,
                             df_scalar_matrix2['optimizedAddCap'][9]/1e3,
                             df_scalar_matrix3['optimizedAddCap'][10]/1e3,
                             df_scalar_matrix4['optimizedAddCap'][6]/1e3], name='PV Erweiterung', width = 0.5,marker_color= 'olive'))   #Kapazität aus Szenarien für Technologie 1
fig2.add_trace(go.Bar(x=x, y=[0,
                             0,
                             df_scalar_matrix3['optimizedAddCap'][13]/1e3,
                             df_scalar_matrix4['optimizedAddCap'][8]/1e3], name='Wind Erweiterung', width = 0.5, marker_color= 'dodgerblue'))

fig2.add_trace(go.Bar(x=x, y=[0,
                             0,
                             0,
                             df_scalar_matrix4['optimizedAddCap'][0]/1e3], name='Batterie', width = 0.5, marker_color= 'indigo'))



fig2.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'},
                  xaxis_title='Szenario', yaxis_title='Installierte Leistung in MW',
                  bargap=0)
# fig.show()


#######


df = pd.DataFrame(
    dict(
        scenario=[1,2,3,4],
        pv=np.array([df_scalar_matrix1['total_flow'][2],
                     df_scalar_matrix2['total_flow'][2],
                     df_scalar_matrix3['total_flow'][2],
                     df_scalar_matrix4['total_flow'][5]])/1e6,
        wind_karholz=np.array([df_scalar_matrix1['total_flow'][3],
                               df_scalar_matrix2['total_flow'][5],
                               df_scalar_matrix3['total_flow'][6],
                               df_scalar_matrix4['total_flow'][9]])/1e6,
        wind_winnberg03=np.array([df_scalar_matrix1['total_flow'][4],
                                  df_scalar_matrix2['total_flow'][6],
                                  df_scalar_matrix3['total_flow'][7],
                                  df_scalar_matrix4['total_flow'][10]])/1e6,
        wind_winnberg04=np.array([df_scalar_matrix1['total_flow'][5],
                                  df_scalar_matrix2['total_flow'][7],
                                  df_scalar_matrix3['total_flow'][8],
                                  df_scalar_matrix4['total_flow'][11]])/1e6,
        dso=np.array([df_scalar_matrix1['total_flow'][0],
                      df_scalar_matrix2['total_flow'][0],
                      df_scalar_matrix3['total_flow'][0],
                      df_scalar_matrix4['total_flow'][3]])/1e6,
        pv_erweiterung=np.array([0,
                                 df_scalar_matrix2['total_flow'][3],
                                 df_scalar_matrix3['total_flow'][3],
                                 df_scalar_matrix4['total_flow'][6]])/1e6,
        wind_erweiterung=np.array([0,
                                   0,
                                   df_scalar_matrix3['total_flow'][5],
                                   df_scalar_matrix4['total_flow'][8]])/1e6,
        battery_output=np.array([0,
                                 0,
                                 0,
                                 df_scalar_matrix4['total_flow'][2]])/1e6,
        industriepark=np.array([df_scalar_matrix1['total_flow'][12],
                                df_scalar_matrix2['total_flow'][16],
                                df_scalar_matrix3['total_flow'][18],
                                df_scalar_matrix4['total_flow'][21]])/1e6,
        feedin=np.array([df_scalar_matrix1['total_flow'][1],
                         df_scalar_matrix2['total_flow'][1],
                         df_scalar_matrix3['total_flow'][1],
                         df_scalar_matrix4['total_flow'][4]])/1e6,
        battery_input=np.array([0,
                                0,
                                0,
                                df_scalar_matrix4['total_flow'][1]])/1e6

    )
)

fig3 = go.Figure()

fig3.update_layout(
    #template="simple_white",
    xaxis=dict(title_text="Szenario"),
    yaxis=dict(title_text="Energie in GWh"),
    barmode="stack",
)

groups = ['pv',
          'wind_karholz',
          'wind_winnberg03',
          'wind_winnberg04',
          'dso',
          'pv_erweiterung',
          'wind_erweiterung',
          'battery_output',
          'industriepark',
          'feedin',
          'battery_input']
colors = ['yellow','blue','teal','aqua','orange','olive','dodgerblue','blueviolet','red','maroon','indigo']
names = ['PV',
         'Wind - Karholz',
         'Wind - Winnberg03',
         'Wind - Winnberg04',
         'Netznutzung',
         'PV Erweiterung',
         'Wind Erweiterung',
         'Batterie Output',
         'Strombedarf',
         'Netzeinspeisung',
         'Batterie Input']

i = 0
for r, n, c in zip(groups, names, colors):
    ## put var1 and var2 together on the first subgrouped bar
    if i <= 7:
        fig3.add_trace(
            go.Bar(x=[df.scenario, ['Erzeugung']*len(df.scenario)], y=df[r], name=n, marker_color = c)
        )
    ## put var3 and var4 together on the first subgrouped bar
    else:
        fig3.add_trace(
            go.Bar(x=[df.scenario, ['Nutzung']*len(df.scenario)], y=df[r], name=n,marker_color = c)
        )
    i+=1

# fig.show()

# the app and its options are defined in the main_app module
app.layout = html.Div(
    className='grid-x app_style',
    children=[
        dcc.Graph(
            className='cell medium-6',
            figure=fig,
        ),
        dcc.Graph(
            className='cell medium-6',
            figure=fig1,
        ),
        dcc.Graph(
            className='cell medium-6',
            figure=fig2,
        ),
        dcc.Graph(
            className='cell medium-6',
            figure=fig3,
        ),

    ]
)



if __name__ == '__main__':
    app.run_server(debug=True)



