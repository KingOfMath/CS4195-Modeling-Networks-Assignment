
import numpy as np
import matplotlib.pyplot as plt
from temporal_network import TemporalNetwork
import seaborn as sns
import random

def plot_intervals_distribution(edges,name):
    pairs=[]
    for i in edges:
        print(i)
        pairs.append((i[0],i[1]))
    y = np.unique(pairs, axis=0)
    z = [] 
    for i in y:
        z.append(tuple(i))

    intervals=[]
    for link in z:
        print(link)
        t = [edge[2] for edge in edges if edge[0]==link[0] and edge[1]==link[1]]
        if len(t)>1:
            for i in range(1, len(t)):
                intervals.append(t[i]-t[i-1])
    sns.distplot(intervals, hist=True, kde=True, 
                bins=int(57791/500), color = 'darkblue', 
                hist_kws={'edgecolor':'black'},
                kde_kws={'linewidth': 2})
    # Add labels
    plt.title('Histogram of Intervals')
    plt.xlabel('Intervals (t) ')
    plt.ylabel('Occurency')
    plt.savefig(name+'_distribution.pdf')



#TODO: Fix multiple timestamp at same edges
def generate_G3_links(G):
    G3_links = []
    for link in G.edges:
        n_links_list = [x for x in range(0,random.randrange(20))] # Random list of int for selcting number of links (at most 20 links)
        if len(n_links_list) != 0:
            n_links=random.choice(n_links_list)
            tmstm = []
            for l in range(0,n_links):
                tmstm.append(G.timestamps[random.randrange(len(G.timestamps)-1)])
            for t in tmstm:
                G3_links.append((int(link[0]),int(link[1]),int(t)))
    return G3_links


# G_data #
G1 = TemporalNetwork()
#G1.load_from_xlsx("mail.xlsx")
#G1.save_network_to_json("G1.json")
G1.load_network_from_json("G1.json")

# G_2 with random shuffled edges (random=True parameters) #
G2 = TemporalNetwork()
#G2.load_from_xlsx("mail.xlsx", True)
#G2.save_network_to_json("G2.json")
G2.load_network_from_json("G2.json")

# G3 #
G3_links = generate_G3_links(G1)
G3 = TemporalNetwork()
G3.load_from_edges(G3_links)
G3.save_network_to_json("G3.json")