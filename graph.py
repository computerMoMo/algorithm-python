# -*- coding:utf-8 -*-
import sys
from collections import deque


graph_names = dict()
graph_names['bob'] = ['alice', 'daniel', 'jack']
graph_names['alice'] = []
graph_names['daniel'] = ['james']
graph_names['jack'] = []
graph_names['james'] = []

graph = dict()
graph['start'] = dict()
graph['start']['a'] = 6.
graph['start']['b'] = 2.
graph['a'] = dict()
graph['a']['final'] = 1.
graph['b'] = dict()
graph['b']['a'] = 3.
graph['b']['final'] = 5.
graph['final'] = dict()

costs = dict()
costs['a'] = 6.
costs['b'] = 2.
costs['final'] = float('inf')

processed = []

parent_node = dict()
parent_node['a'] = 'start'
parent_node['b'] = 'start'
parent_node['final'] = None


def find_lowest_cost(node_costs, processed_node):
    lowest_cost = float('inf')
    lowest_node = None
    for node in node_costs.keys():
        if node_costs[node] < lowest_cost and node not in processed_node:
            lowest_node = node
    return lowest_node


def dijkstra():
    processed.append('start')
    node = find_lowest_cost(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parent_node[n] = node
        processed.append(node)
        node = find_lowest_cost(costs, processed)

# def graph_search_width(search_graph, start_name, name):
#     que = deque()
#     searched = []
#     que += search_graph[start_name]
#     while len(que) > 0:
#         check_name = que.popleft()
#         if check_name == name:
#             return True
#         else:
#             searched.append(check_name)
#             que += search_graph[check_name]
#     return False


if __name__ == '__main__':
    # print graph_search_width(graph_names, 'jack', 'james')
    dijkstra()
    p_node = 'final'
    print p_node
    while p_node != 'start':
        p_node = parent_node[p_node]
        print p_node
