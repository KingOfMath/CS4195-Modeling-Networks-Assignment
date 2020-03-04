import networkx as nx
import dynetx as dn
import ndlib.models.ModelConfig as mc
import ndlib.models.dynamic as dm
import json 

### SI MODEL FROM A DYNETX GRAPH ###

def load_dynetx_from_json(links_files="edges.json"):
    with open('edges.json') as json_file:
        data = json.load(json_file)
    new_edge_list=[]
    for edges_list in data["edges"]:
        edges=[]
        for edge in edges_list:
            edges.append(tuple(edge))
        new_edge_list.append(edges)
    g = dn.DynGraph(edge_removal=True)
    for i, links in enumerate(new_edge_list):
        g.add_interactions_from(links, t=i)
    return g

# Load Graph
g = load_dynetx_from_json("mail.json")
# test correct load
# print(g.interactions(t=0))

# Model selection
model = dm.DynSIModel(g)

# Model Configuration
config = mc.Configuration()
config.add_model_initial_configuration("Infected", [1])
config.add_model_parameter('beta', 1)
model.set_initial_status(config)

# Simulation execution
iterations = model.iteration_bunch()
