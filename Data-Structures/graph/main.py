import sys
import math


def get_ints_in_list(): return list(
    map(int, sys.stdin.readline().strip().split()))


def genericGraph(G, u, v, GType="ArrayList", bidir=True):
    if bidir and GType == "ArrayList":
        createArrayListGraph(G, u, v)
        return
    elif not bidir and GType == "ArrayList":
        createArrayListDirectedGraph(G, u, v)
        return

    # // Make HashMap
    if u in G:
        G[u].append(v)
    else:
        G[u] = [v]
    if bidir:
        if v in G:
            G[v].append(u)
        else:
            G[v] = [u]


def createArrayListDirectedGraph(G, u, v):
    G[u].append(v)


def createArrayListGraph(G, u, v):
    G[u].append(v)
    G[v].append(u)


HashMap = {}
genericGraph(HashMap, "Delhi", "Mumbai", "HashMap", False)
genericGraph(HashMap, "Jaipur", "Delhi", "HashMap", False)
genericGraph(HashMap, "Gujrat", "Channai", "HashMap", False)
print(HashMap)
