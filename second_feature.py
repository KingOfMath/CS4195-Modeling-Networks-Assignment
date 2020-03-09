def rank_temporal_degree(G,t):
    rank=[]
    runs=[0 for x in range(len(G.nodes()))]
    for ts in range(0, t):
        counts = [0 for x in range(len(G.nodes()))]
        print(ts)
        degrees = list(G.degree(G.nodes(), t=ts).values())
        for i,d in enumerate(degrees):
            counts[i]=counts[i]+d
        runs[counts.index(max(counts))]+=1
    for i in run:
        ind=runs.index(max(runs))
        rank.append(ind)
        rank.pop(ind)
    return rank

G1 = TemporalNetwork()
G1.load_network_from_json("G1.json")

d = {}
for i in range(samples):
    d[i] = 0
first_time = []
R = []
notUsed = []
limit = int(167 * 0.8)
for seed in range(1, samples):
    Infected = []
    timestamp = 0
    count = 0
    flag = True
    print("seed:" + str(seed))
    for link in raws:
        node_in = int(link[0])
        node_out = int(link[1])
        currentTime = int(link[2])
        if currentTime == timestamp + 1:
            if (node_in == seed) or (node_in in Infected):
                if node_out not in Infected:
                    Infected.append(node_out)
                    count += 1
                if count > limit and flag:
                    flag = False
                    first_time.append((seed, currentTime))
                if currentTime == 57791 and flag:
                    notUsed.append((seed, count))
        else:
            timestamp += 1
            if (node_in == seed) or (node_in in Infected):
                if node_out not in Infected:
                    Infected.append(node_out)
                    count += 1
                if count > limit and flag:
                    flag = False
                    first_time.append((seed, currentTime))
                if currentTime == 57791 and flag:
                    notUsed.append((seed, count))

for i, j in sorted(first_time, key=lambda item: item[1]):
    R.append(i)
for i, j in sorted(notUsed, key=lambda item: item[1])[::-1]:
    R.append(i)
#################################### R ##################################################
timeDrank = rank_temporal_degree(G1.to_dynetx(), G1.timestamps[-1])
rTimeD = []
all_f = np.linspace(0.05, 0.5, 10)
for f in all_f:
    fN = int(f * 167)
    RTimeD = []
    for node in R[:fN]:
        if node in rTimeD[:fN]:
            RTimeD.append(node)
    rRTimeD.append(len(RTimeD) / fN)
plt.figure()
plt.xlabel('f')
plt.ylabel('rRD')
plt.plot(all_f, rRTimeD)
plt.show()