# -*- coding:utf-8 -*-
import sys

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


def find_lowest_node(costs):
    lowest_cost = float('inf')
    lowest_node = None
    for node in costs.keys():
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_node = node
    return lowest_node

if __name__ == '__main__':
    node = find_lowest_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parent_node[n] = node
        processed.append(node)
        node = find_lowest_node(costs)

    p_node = 'final'
    print p_node
    while p_node != 'start':
        p_node = parent_node[p_node]
        print p_node
