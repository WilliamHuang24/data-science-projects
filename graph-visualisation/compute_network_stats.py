import json
import argparse
import networkx as nx

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input')
parser.add_argument('-o', '--output')

args = parser.parse_args()
    
with open(args.input, 'r') as f:
    js_graph = json.load(f)
    G = nx.DiGraph(js_graph)

    degree_centrality = nx.degree_centrality(G)
    top_three_degree = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[0:3]

    weighted_centrality = nx.eigenvector_centrality(G, weight = 'weight')
    top_three_weight = sorted(weighted_centrality, key=weighted_centrality.get, reverse=True)[0:3]

    closeness_centraliry = nx.closeness_centrality(G)
    top_three_closenss = sorted(closeness_centraliry, key=closeness_centraliry.get, reverse=True)[0:3]

    betweeness_centrality = nx.betweenness_centrality(G)
    top_three_between = sorted(betweeness_centrality, key=betweeness_centrality.get, reverse=True)[0:3]

    output = {}
    output['degree'] = top_three_degree
    output['weighted_degree'] = top_three_weight
    output['closeness'] = top_three_closenss
    output['betweenness'] = top_three_between

    with open(args.output, 'w') as of:
        json.dump(output, of)
