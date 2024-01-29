import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout, to_agraph
import csv as csv
import pygraphviz as gv
import pydot
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir")
args = parser.parse_args()
prefix = args.dir

#name = "sample-program-changed"
#prefix = "/home/kotname/Documents/Diplom/Code/cpec-doop-and-jdime-experiments/" + name + "/PDG_Analysis"
Nodes =  prefix + "/PDGNodes.csv"
CD_file = prefix  + "/ControlDep.csv"
DD_file = prefix  + "/DataDep.csv"

def normalizeString(node):
    if node.__contains__(":"):
        node = node.replace(":", '')
    '''if node.__contains__("/"):
        node = node.partition("/")[2]'''
    if len(node) > 20:
        node = node[0:20] + "\n" + node[20:]
    return node

if __name__== "__main__":
    G = nx.MultiDiGraph()
    last_node_name = ""
    start_node_name = ""
    line_mod = 0
    last_method = ""
    node_width = 1
    # nodes: (method, name, lineNr)
    # dependencies: (method, name1, name2)
    with open(Nodes, newline='') as csvfile:
        nodes = {}
        line = csv.reader(csvfile, delimiter="\t")
        for node in line:

            #if node[0].__contains__("<GPLAG2_Ex"):
            node_name = normalizeString(node[1])

            if last_node_name != "":
                if last_method != node[0]:
                    line_mod = nodes[last_node_name]
                    line_nr += line_mod
                    node_width += 1
                    last_method = node[0]
                w2 = abs(line_nr - nodes[start_node_name])
                w1 = abs(line_nr - nodes[last_node_name])
                #G.add_node(node, pos= "100," + str(int(line[2])) +"!")
                G.add_edge(last_node_name, node_name, weight=w1, style="invis", key=3)
                G.add_edge(start_node_name, node_name, weight=w2, style="invis", key=3)
            else:
                start_node_name = node_name
                last_method = node[0]
            G.add_node(node_name, penwidth=node_width)
            line_nr = int(node[2])
            nodes[node_name] = line_nr
            last_node_name = node_name


    edge_list = []
    datasource = [(CD_file, "blue"), (DD_file, "red")]
    i = 1

    for type in datasource:
        last_method = ""
        edge_width = 0.5
        with open(type[0], newline='') as csvfile:
            line = csv.reader(csvfile, delimiter="\t")
            for edge in line:
                #if edge[0].__contains__("<GPLAG2_Ex"):
                node1 = normalizeString(edge[1])
                node2 = normalizeString(edge[2])
                w = 2* abs(nodes[node2] - nodes[node1])
                if last_method != edge[0]:
                    edge_width += 0.6
                    last_method = edge[0]
                #"weight": w,
                edge_list.append((node1, node2, {"penwidth": edge_width, "weight" : w, "color" : type[1]}))
        G.add_edges_from(edge_list)
        edge_list.clear()
        i += 1

    #CD = nx.read_edgelist(CD_file, create_using=nx.DiGraph, nodetype= str, delimiter="\t")
    #DD = nx.read_edgelist(DD_file, create_using=nx.DiGraph, nodetype= str, delimiter="\t")

    #G.add_nodes_from(DD)
    #G.add_nodes_from(CD)
    #G.add_edges_from(CD.edges, color="red")
    #G.add_edges_from(DD.edges, color="blue")

    '''pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, connectionstyle='arc3, rad = 0.1')
    #edge_labels = dict([((u, v,), d['length'])                         for u, v, d in G.edges(data=True)])
    plt.show()
    pos = nx.nx_pydot.graphviz_layout(G)
    plt.figure()
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1, node_size=10, node_color='blue', alpha=0.9)
    plt.axis('on')
    plt.show()
    PG = nx.nx_pydot.to_pydot(G)
    '''
    # set defaults
    G.graph['graph'] = {'rankdir': 'TD'}
    G.graph['node'] = {'shape': 'ellipse'}
    G.graph['edges'] = {'arrowsize': '3.0'}

    A = to_agraph(G)

    for node in G.nodes:
        A.add_subgraph([node], rank='same')
    A.layout('dot')
    A.draw('PDG.png')
    nx.drawing.nx_pydot.write_dot(G, "multi.dot")
