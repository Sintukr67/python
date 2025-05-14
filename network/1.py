import networkx as nx 
import matplotlib.pyplot as plt
# G=nx.complete_graph(10)
G=nx.gnp_random_graph(10,0.3)
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
# G.add_edge(1,2)
# G.add_edge(1,3)
# G.add_edge(3,2)
print(G.edges())
nx.draw(G)
# nx.draw(G, with_labels=True)
plt.show()