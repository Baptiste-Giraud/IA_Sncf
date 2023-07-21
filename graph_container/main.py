from flask import Flask, request
import pandas as pd
import networkx as nx
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

G = nx.DiGraph()
df_stops = pd.read_csv('data_sncf/stops.txt', delimiter = ',')
df_stop_times = pd.read_csv('data_sncf/stop_times.txt', delimiter = ',')

@app.before_first_request
def generate_graph():

    for index, row in df_stops.iterrows():
        G.add_node(row['stop_id'], name=row['stop_name'])

    for index, row in df_stop_times.iterrows():
      if index == df_stop_times.shape[0] - 1:
        break
      if df_stop_times.loc[index+1, 'stop_sequence'] != 0:
          departure_time = row['departure_time']
          departure_tab = departure_time.split(':')
          departure_time_second = int(departure_tab[0]) * 3600 + int(departure_tab[1]) * 60 + int(departure_tab[2])

          arrival_time = df_stop_times.loc[index+1, 'arrival_time']
          arrival_tab = arrival_time.split(':')
          arrival_time_second = int(arrival_tab[0]) * 3600 + int(arrival_tab[1]) * 60 + int(arrival_tab[2])

          travel_time = arrival_time_second - departure_time_second
          G.add_edge(row['stop_id'], df_stop_times.loc[index+1, 'stop_id'], weight=travel_time)

@app.route('/shortest_path', methods=['GET'])
def find_shortest_path():
    gare_depart = request.args.get('gare_depart')
    gare_arrive = request.args.get('gare_arrive')
    
    shortest_path = nx.dijkstra_path(G, source=gare_depart, target=gare_arrive, weight='weight')
    shortest_path_length = nx.dijkstra_path_length(G, gare_depart, gare_arrive, weight='weight')
    nom_gare_depart = df_stops.loc[df_stops["stop_id"] == gare_depart, 'stop_name'].values[0]
    nom_gare_arrive = df_stops.loc[df_stops["stop_id"] == gare_arrive, 'stop_name'].values[0]

    m, s = divmod(shortest_path_length, 60)
    h, m = divmod(m, 60)
    result = f"Pour aller de {nom_gare_depart} a {nom_gare_arrive} il faut {h:d} heures {m:d} minutes et {s:d} secondes."
    return {"result" : shortest_path, "time": shortest_path_length}

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)
