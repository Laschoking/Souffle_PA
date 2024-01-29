import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout, to_agraph
import csv as csv
import pygraphviz as gv
import pydot
import argparse
from collections import deque

#parser = argparse.ArgumentParser()
#parser.add_argument("-d", "--dir")
#args = parser.parse_args()
#prefix = args.dir

#name = "sample-program-changed"
prefix = "/home/kotname/Documents/Diplom/Code/ex_souffle/out/Liveness/vgl7_8"
DD_file = prefix  + "/VarDep2.csv"
Method_file = prefix + "/VarMeth2.csv"

def normalizeString(node):
    if node.__contains__(":"):
        node = node.replace(":", '')
    if node.__contains__("$"):
        node = node.replace("$", '')
    if node.__contains__("/"):
        node = node.partition("/")[2]
    if len(node) > 20:
        node = node[0:20] + "\n" + node[20:]
    return node

if __name__== "__main__":
    G = nx.DiGraph()
    last_node_name = ""
    start_node_name = ""
    line_mod = 0
    last_method = ""
    node_width = 1
    edge_list = []

    color_map = deque(['b','g','c','m','y','k'])
    methods = dict()
    var_dict = dict()
    with open(Method_file, newline='') as csvfile:
        line = csv.reader(csvfile, delimiter="\t")
        for entry in line:
            var = normalizeString(entry[0])
            meth = normalizeString(entry[1])
            if meth not in methods:
                c = color_map.popleft()
                methods[meth] = c
            else:
                c = methods[meth]
            var_dict[var] = c

    edge_width = 0.5
    edge_col = []
    with open(DD_file, newline='') as csvfile:
        line = csv.reader(csvfile, delimiter="\t")
        for edge in line:
            node1 = normalizeString(edge[0])
            node2 = normalizeString(edge[1])
            c1 = var_dict[node1]
            if c1 == var_dict[node2]:
                col = c1
            else:
                col = "red"
            print(node1 + " -> " + node2 + " color: " + col)
            edge_list.append((node1, node2, {"col": col}))
            #edge_col.append(col)
        G.add_edges_from(edge_list)

    pos = nx.nx_pydot.graphviz_layout(G,prog='dot')
    plt.figure()
    base_size = 300
    size=[len(v) * base_size for v in G.nodes()]
    edge_col = list(nx.get_edge_attributes(G, "col").values())
    #for e in G.edges:
    #    edge_col.append(e.col)
    #nx.draw_networkx_nodes(G, pos, linewidths=0.5,  edgecolors='red',node_color='none',node_size=size)
    nx.draw_networkx_edges(G, pos, edge_color=edge_col, arrowsize=30,node_size=450, width=2, alpha=0.9)
    nx.draw_networkx_labels(G,pos,bbox=dict(facecolor = "skyblue"), font_size=12)

    #plt.savefig("VarDependencies7.png")
    plt.show()

    #nx.draw_networkx_nodes(G,pos,,node_size=500, node_shape='o')
    #, edge_color=edge_col
    # set defaults
