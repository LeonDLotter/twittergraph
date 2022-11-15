#%%

# import
import pandas as pd
import networkx as nx
from pyvis.network import Network
from igraph import Graph
import numpy as np

# download orcid data
orc_list = pd.read_csv("https://opencheck.is/scitwitter/orcidgraph", header=None)

# create graph (networkx because the easiest)
nx_graph = nx.Graph()
nx_graph.add_edges_from(orc_list.to_numpy())
n_edges = nx_graph.number_of_edges()
n_nodes = nx_graph.number_of_nodes()
print("Number of edges:", n_edges)
print("Number of nodes:", n_nodes)

# estimate layout (igraph because fast)
ig_graph = Graph.from_networkx(nx_graph)
layout = ig_graph.layout("fr")
layout_factor = 1000 # factor to multiply the node positions with (maybe adjust with more nodes)

# convert to pyvis graph (because nice HTML plotting)
pv_graph = Network(height="600px", width="100%", select_menu=True, bgcolor="#000e1e")
pv_graph.from_nx(nx_graph)
# global layout
pv_layout = """
    const options = {
        "nodes": {
            "scaling": {
                "min": 10,
                "max": 60
            },
            "color": {
                "border": "rgb(43, 124, 233, 1)",
                "background": "rgb(160, 198, 247)"
            },
            "font": {
                "color": "rgba(255, 255, 255, 0.8)"
            }
        },
        "edges": {
            "color": {
                "color": "rgba(43, 124, 233, 0.2)",
                "highlight": "rgba(139, 0, 0, 1)"  
            },
            "smooth": {
                "type": "continuous",
                "roundness": 0.75
            }
        },
        "physics": {
            "enabled": false
        }
    }
    """
pv_graph.set_options(pv_layout)

# specific layout
for i, node in enumerate(pv_graph.get_nodes()):
    # position from igraph
    pv_graph.get_node(node)["x"] = layout.coords[i][0] * layout_factor
    pv_graph.get_node(node)["y"] = layout.coords[i][1] * layout_factor
    # node size
    degree = nx_graph.degree()[node]
    pv_graph.get_node(node)["value"] = degree
    # hover information
    pv_graph.get_node(node)["title"] = f'<a href=https://orcid.org/{node} target="_parent">{node}</a><br>{degree} edges'
    # color when selected
    pv_graph.get_node(node)["color"] = {
        "highlight": {
            "border": 'darkred',
            "background": 'red'
        }
    }

# save as HTML
pv_graph.show('graph.html')


# %%
