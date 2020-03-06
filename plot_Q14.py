
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

# G_data #
G1 = TemporalNetwork("mail.xlsx")

# G_2 with random shuffled edges (random=True parameters) #
G2 = TemporalNetwork("mail.xlsx", True)
G2.edges.sort(key=lambda tup: tup[2]) 

# G_3 random assignment from timestamps #
G3 = TemporalNetwork("mail.xlsx")
G_links=[(x[0],x[1]) for x in G3.edges] #Topology of G
G3_links = []
for link in G_links:
    n_links_list = [x for x in range(0,random.randrange(20))]
    if len(n_links_list) != 0:
        n_links=random.choice(n_links_list)
        tmstm = []
        for l in range(0,n_links):
            tmstm.append(G3.timestamps[random.randrange(len(G3.timestamps)-1)])
        for t in tmstm:
            G3_links.append((link[0],link[1],t))
G3_links.sort(key=lambda tup: tup[2]) 
print(G3_links)
#plot_intervals_distribution(G1.edges ,"G1")
#plt.clf()
#plot_intervals_distribution(G2.edges , "G2")
#plt.clf()
plot_intervals_distribution(G3_links, "G3")
