import numpy as np
from scipy import sparse
from graph_tool.all import *
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import sys


df = pd.read_csv('data/original/retweet_list_relabeled.csv',names = ['user_id','retweeted'],sep="\t")
df_new = df[(df.user_id < 10000) & (df.retweeted < 10000)]
df_new.to_csv("data/original/retweet_list_relabeled_filtered.csv", header = False, columns = ['user_id','retweeted'], sep=' ', index = False)