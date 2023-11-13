import networkx as nx
import csv

file_path = "Asset\BX-Users.csv"


G = nx.Graph()

with open(file_path, "r", encoding="ISO-8859-1") as file:
    reader = csv.reader(file, delimiter=";")
    next(reader)
    cont = 1
    for row in reader:
        user_id = row[0]
        location = row[1]
        age = row[2]
        G.add_node(user_id, location=location, age=age)
        cont+=1
        if cont == 1000: break

def add_edges_based_on_similarity(graph, attribute):
    nodes = list(graph.nodes(data=True))

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if nodes[i][1][attribute] == nodes[j][1][attribute]:
                graph.add_edge(nodes[i][0], nodes[j][0])

add_edges_based_on_similarity(G, "location")

add_edges_based_on_similarity(G, "age")

edge_betweenness = nx.edge_betweenness_centrality(G)

max_betweenness_edge = max(edge_betweenness, key=edge_betweenness.get)
G.remove_edge(*max_betweenness_edge)

communities = list(nx.connected_components(G))


output_file_path = "communities.csv"
with open(output_file_path, "w", newline="") as output_file:
    writer = csv.writer(output_file)
    for i, community in enumerate(communities, start=1):
        print(community)
        writer.writerow([f"Community {i}"] + list(community))
