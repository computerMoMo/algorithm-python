# -*- coding:utf-8 -*-
from collections import deque
import sys

graph_names = dict()
graph_names['bob'] = ['alice', 'daniel', 'jack']
graph_names['alice'] = []
graph_names['daniel'] = ['james']
graph_names['jack'] = []
graph_names['james'] = []


def graph_search(names, key_name):
    search_que = deque()
    searched = []
    search_que += graph_names[names]
    searched.append(names)
    while len(search_que) > 0:
        check_name = search_que.popleft()
        if check_name not in searched:
            if check_name == key_name:
                return True
            else:
                search_que += (graph_names[check_name])
                searched.append(check_name)
    return False

if __name__ == '__main__':
    print graph_search('bob', 'james')
    print graph_search('bob', 'zhang')
