import re, sys, math, random, csv, types, networkx as nx
from collections import defaultdict

def parse(filename, isDirected):
    print ("Reading and parsing the data into memory...")
    if isDirected:
        return parse_directed(filename)
    else:
        return parse_undirected(filename)

def parse_undirected(filename):
    G=nx.read_edgelist(filename)
    return G

def parse_directed(filename):
    DG = nx.read_edgelist(path=filename,create_using=nx.DiGraph)
    return DG

def digits(val):
    return int(re.sub("\D", "", val))

def format_key(key):
    key = key.strip() 
    if key.startswith('"') and key.endswith('"'):
        key = key[1:-1]
    return key 


def print_results(f, method, results):
    print (method)

