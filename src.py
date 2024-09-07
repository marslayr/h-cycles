import itertools
import networkx as nx
import matplotlib.pyplot as plt
from math import comb


# Finds all tournaments
def tournaments(n):
    matches = list(itertools.combinations(list(range(n)), 2))
    results = list(itertools.product([0, 1], repeat=comb(n,2)))
    return matches, results

# Make a graph 
def random_graph(matches, result):
    G = nx.DiGraph()
    for(i, (A, B)) in enumerate(matches): # assume A and B as teams
        if result[i] == 1:
            G.add_edge(A, B)
        else: 
            G.add_edge(B, A)
    return G
# check if cop exists by equating length of cycle to number of nodes
def has_cop(G):
    if nx.is_strongly_connected(G):
        return True
    return False

# count cop
def count_cop(n):
    matches, results = tournaments(n)
    cop = 0

    for result in results: 
        G = random_graph(matches, result)
        if has_cop(G):
            cop += 1

    return cop

# example
n = 7
matches, results = tournaments(n)
print(count_cop(n))
