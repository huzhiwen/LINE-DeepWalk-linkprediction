import numpy as np
from scipy import sparse
from graph_tool.all import *
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import sys

# file = open('data/original/dblp.txt', 'r')
# lines = file.readlines()
# print (lines)


df = pd.read_csv('data/original/retweet_list.csv',sep="\t")
g = nx.from_pandas_edgelist(df, "user_id", "retweeted", edge_attr=True)
mapping = {old_label:new_label for new_label, old_label in enumerate(g.nodes())}
new_g = nx.relabel_nodes(g, mapping)
adjacent_list = nx.to_dict_of_lists(new_g, nodelist=None)
new_edgelist = nx.to_pandas_edgelist(new_g)
new_edgelist = new_edgelist[['source','target']]
new_edgelist = new_edgelist.rename(columns = {"target": "retweeted", "source":"user_id"}) 
new_edgelist.to_csv("data/original/retweet_list_relabeled.csv", header = False, columns = ['user_id','retweeted'], sep='\t', index = False)