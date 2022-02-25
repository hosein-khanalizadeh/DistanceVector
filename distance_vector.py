#!/usr/bin/python
'coded by hosein-khanali'


import sys

def load_topology(file):
    f = open(file)
    data = f.read().splitlines()
    f.close()
    frame = {}
    nodes = data[0][1:].split(',')
    for d in data[1:]:
        row = d.split(',')
        node = row[0]
        weights = row[1:]
        frame[node] = {n:int(w) for n,w in zip(nodes,weights)}
    return frame

def distance_vector(topology):
    dv = {}
    for node in topology:
        dv[node] = {n:{"cost":c, "path":node+n} for n,c in topology[node].items()}
    for i in range(len(dv)-1):
        for node in dv:
            for d in dv[node]:
                for n in dv:
                    if (dv[node][d]["cost"] > dv[node][n]["cost"] + dv[n][d]["cost"]):
                        dv[node][d]["cost"] = dv[node][n]["cost"] + dv[n][d]["cost"]

    return dv
def usage():
    print("Usage : python distance_vector.py .\TopologyName")

def main():
    if len(sys.argv)==2:
        data_frame = load_topology(str(sys.argv[1]))
        dv_frame = distance_vector(data_frame)
        for n in dv_frame:
            weights = " ".join([str(dv_frame[n][t]["cost"]) for t in dv_frame[n]])
            print("Distance_Vector for node {}: {}".format(n, weights))
    else:
        usage()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(f'{red} [-] ^C received . shutting down server !{reset}')
        sys.exit()
