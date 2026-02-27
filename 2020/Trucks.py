import networkx as nx

start = input()
end = input()
roads = int(input())

G = nx.DiGraph()

for _ in range(roads):
    parts = input().strip().split()
    if len(parts) != 3:
        continue
    x, y, z = parts
    z = int(z)

    if G.has_edge(x, y):
        G[x][y]['capacity'] += z
    else:
        G.add_edge(x, y, capacity=z)

if not G.has_node(start):
    G.add_node(start)
if not G.has_node(end):
    G.add_node(end)

flow_value, flow_dict = nx.maximum_flow(G, start, end)
print(flow_value)