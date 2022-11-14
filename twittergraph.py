#%%

# import
import pandas as pd
import networkx as nx
from pyvis.network import Network

# download orcid list
orc_list = pd.read_csv("https://opencheck.is/scitwitter/orcidgraph", header=None)
n_edges = orc_list.shape[0]
print("Number of edges:", n_edges)

# network settings # IMPORTANT
springLength = 20 # default length of edges
springConstant = 0.001 # decrease for less power pushing nodes away from one another
minVelocity = 20 # the velocity of moving nodes that has to be reached to stabilize

# create graph (networkx -> pyvis)
nx_graph = nx.Graph()
nx_graph.add_edges_from([tuple(orc_list.iloc[i,:]) for i in range(n_edges)])
pv_graph = Network(height="700px", width="100%", select_menu=True)
pv_graph.from_nx(nx_graph)
print("Number of nodes:", len(pv_graph.get_nodes()))

# layout
options = """
    const options = {
        "nodes": {
            "color": {
                "border": "rgb(43, 124, 233, 1)",
                "background": "rgb(160, 198, 247)"
            }
        },
        "edges": {
            "color": {
                "color": "rgb(43, 124, 233, 0.5)",
                "opacity": 0.3,
                "highlight": "darkred"  
            }
        },
        "physics": {
            "barnesHut": {
                "springLength": %f,
                "springConstant": %f
            },
            "minVelocity": %f,
            "stabilization": {
                "enabled": true,
                "iterations": 100,
                "fit": true
            }
        }
    }
    """ % (springLength, springConstant, minVelocity)
pv_graph.set_options(options)

# node size by connection number
for node in pv_graph.get_nodes():
    pv_graph.get_node(node)["value"] = nx_graph.degree()[node]
    pv_graph.get_node(node)["title"] = f'<a href=https://orcid.org/{node}>{node}</a>'
    pv_graph.get_node(node)["color"] = {
        "highlight": {
            "border": 'darkred',
            "background": 'red'
        }
    }
#pv_graph.show_buttons(filter_=['physics'])

# save as HTML
pv_graph.show('graph.html')


# %%
