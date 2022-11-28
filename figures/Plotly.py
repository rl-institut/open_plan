


import plotly.graph_objects as go

n = 4                                #Anzahl der Szenarien, die verglichen werden sollen

x=[str(chr(ord('@')+number)) for number in range(1,n+1)] 
#x = ['A','B','C','D']

# Eine Datenreihe für jede Technologie -> Wie viele Technologien werden pro Szenario verwendet? (betrachten hauptsächlich Producer)

fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='PV', width = 0.8))                  #Kapazität aus Szenarien für Technologie 1 
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Wind', width = 0.8))              #Kapazität aus Szenarien für Technologie 2
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Solarthermie', width = 0.8))     #Kapazität aus Szenarien für Technologie 3

fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'}, 
                  xaxis_title='Szenario', yaxis_title='Installierte Kapazität in kWp',
                  bargap=0)
fig.show()


# In[ ]:


n = 4                                #Anzahl der Szenarien, die verglichen werden sollen

x=[str(chr(ord('@')+number)) for number in range(1,n+1)] 
#x = ['A','B','C','D']

fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='PV', width = 0.8))                  #Kapazität aus Szenarien für Technologie 1 
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Wind', width = 0.8))              #Kapazität aus Szenarien für Technologie 2
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Solarthermie', width = 0.8))     #Kapazität aus Szenarien für Technologie 3

fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'}, 
                  xaxis_title='Szenario', yaxis_title='Installierte Kapazität',
                  bargap=0)
fig.show()

