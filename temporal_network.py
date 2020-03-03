import xlrd
import numpy as np
import json

class TemporalNetwork:

    def __init__(self, file_name):
        self.file_name = file_name
        self.raws = self.read_xlsx()
        self.nodes = self.get_nodes_list()
        self.edges = self.get_edges_list()
        self.timestamps = self.get_timestamp_list()
        self.max_timestamp = self.get_max_timestamp()
        self.temporal_edges = self.temporal_edges_list()



    def read_xlsx(self):
        workbook = xlrd.open_workbook(self.file_name)
        sheet = workbook.sheet_by_name('Sheet1')
        num_rows = sheet.nrows
        res = []
        for i in range(1,num_rows):
            res.append(sheet.row_values(i))
        return res

    def get_nodes_list(self):
        nodes_in_list=[]
        nodes_out_list=[]
        for link in self.raws:
            node_in = int(link[0])
            node_out = int(link[1])
            nodes_in_list.append(node_in)
            nodes_out_list.append(node_out)
        return np.unique(nodes_in_list+nodes_out_list)

    def get_edges_list(self):
        edges_list=[]
        for link in self.raws:
            node_in = int(link[0])
            node_out = int(link[1])
            timestamp = int(link[2])
            edges_list.append((node_in,node_out,timestamp))
        return edges_list

    def get_timestamp_list(self):
        timestamp_list=[]
        for link in self.raws:
            timestamp = int(link[2])
            timestamp_list.append(timestamp)
        return np.unique(timestamp_list).tolist()

    def get_max_timestamp(self):
        ts = self.timestamps
        return int(ts[len(ts)-1])+1

    def temporal_edges_list(self):
        edges_list=self.edges
        temporal_edges=[]
        for ts in self.timestamps:
            l=[[y[0],y[1]] for y in edges_list if y[2] == ts]
            temporal_edges.insert(ts,l)
        return temporal_edges

    def parser_to_taco(self):
        graph = {}
        graph['type'] = "edge_lists"
        graph['tmax'] = self.max_timestamp
        graph['t'] = self.timestamps
        graph["N"] = len(self.nodes)
        graph["edges"] = self.temporal_edges
        graph["int_to_node"]={}
        graph["notes"]=""
        graph["time_unit"]="s"
        with open('temporal_graph.taco', 'w') as outfile:
            json.dump(graph, outfile)