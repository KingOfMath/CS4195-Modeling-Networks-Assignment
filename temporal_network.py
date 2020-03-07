import xlrd
import numpy as np
import json
import dynetx as dn
import random as rnd
import progressbar

class TemporalNetwork:

    def __init__(self):
        self.temporal_edges = []
        self.nodes=[]
        self.edges=[]
        self.timestamps=[]


    def load_from_xlsx(self, file_name="", rand=False):
        print("[GRAPH INIT] Read xlsx file...")
        raws = self.read_xlsx(file_name,rand)
        print("[GRAPH INIT] Generate temporal edges...")
        self.init_from_raws(raws)
        print("*** TEMPORAL NETWORK INITIALIZED ***")
        print()
    

    def load_from_temporal_edges(self, temporal_edges):
        print("[GRAPH INIT] Read temporal edges...")
        self.temporal_edges = temporal_edges
        print("[GRAPH INIT] Generate nodes...")
        self.nodes=self.get_nodes()
        print("[GRAPH INIT] Generate aggregated edges...")
        self.edges=self.get_edges()
        self.timestamps = [x for x in range(0,len(self.temporal_edges))]
        print("*** TEMPORAL NETWORK INITIALIZED ***")
        print()
    

    def load_from_edges(self, edges):
        print("[GRAPH INIT] Read edges...")
        timestamps=np.unique([x[2] for x in edges])
        temporal_edges=[]
        bar = progressbar.ProgressBar()
        for i in bar(range(len(timestamps))):
            l=[[y[0],y[1]] for y in edges if y[2] == timestamps[i]]
            temporal_edges.insert(timestamps[i],l)
        self.temporal_edges=temporal_edges
        print("[GRAPH INIT] Generate nodes...")
        self.nodes=self.get_nodes()
        print("[GRAPH INIT] Generate aggregated edges...")
        self.edges=self.get_edges()


    def read_xlsx(self,file_name,rand):
        workbook = xlrd.open_workbook(file_name)
        sheet = workbook.sheet_by_name('Sheet1')
        num_rows = sheet.nrows
        res = []
        for i in range(1,num_rows):
            res.append(sheet.row_values(i))
        if (rand):
            res = self.shuffle_timestamps(res)
        return res


    def shuffle_timestamps(self, raws):
        timestamps=[]
        for link in raws:
            timestamps.append(link[2])
        rnd.shuffle(timestamps)
        shuffled_raws=[]
        for i, link in enumerate(raws):
            link[2]=timestamps[i]
            shuffled_raws.append(link)
        return shuffled_raws


    def init_from_raws(self,raws):
        edges_list=[]
        timestamp_list=[]
        for link in raws:
            node_in = int(link[0])
            node_out = int(link[1])
            timestamp = int(link[2]-1)
            timestamp_list.append(timestamp)
            edges_list.append((node_in,node_out,timestamp))
        timestamps=np.unique(timestamp_list).tolist()
        self.timestamps=timestamps
        temporal_edges=[]
        bar = progressbar.ProgressBar()
        for i in bar(range(len(timestamps))):
            l=[[y[0],y[1]] for y in edges_list if y[2] == timestamps[i]]
            temporal_edges.insert(timestamps[i],l)
        self.temporal_edges=temporal_edges
        print("[GRAPH INIT] Generate nodes...")
        self.nodes=self.get_nodes()
        print("[GRAPH INIT] Generate aggregated edges...")
        self.edges=self.get_edges()


    def get_nodes(self):
        nodes=[]
        for edges in self.temporal_edges:
            for link in edges:
                nodes.append(link[0])
                nodes.append(link[1])
        return np.unique(nodes)


    def get_edges(self):
        e=[]
        for edges in self.temporal_edges:
            for link in edges:
                e.append((link[0],link[1]))
        y = np.unique(e, axis=0)
        z = [] 
        for i in y:
            z.append(tuple(i))
        return z


    def load_network_from_json(self, file_name):
        with open(file_name) as json_file:
            data = json.load(json_file)
        self.load_from_temporal_edges(data["edges"])


    def save_network_to_json(self, file_name="graph.json"):
        graph = {}
        graph["edges"] = self.temporal_edges
        print(type(graph))
        with open(file_name, 'w') as outfile:
            json.dump(graph, outfile)


    def to_dynetx(self):
        new_edge_list=[]
        for edges_list in self.temporal_edges:
            edges=[]
            for edge in edges_list:
                edges.append(edge)
            new_edge_list.append(edges)
        g = dn.DynGraph(edge_removal=True)
        for i, links in enumerate(new_edge_list):
            g.add_interactions_from(links, t=i)
        return g
    

