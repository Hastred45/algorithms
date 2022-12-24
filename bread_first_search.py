from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['tom', 'jack']
graph['bob'] = ['mark']
graph['claire'] = []
graph['tom'] = []
graph['jack'] = ['pit']
graph['mark'] = []
graph['pit'] = []

def person_seler(name):
    if name[-1] == 't':
        return True
    else:
        return False

def search(name):
    search_deq = deque()
    search_deq += graph[name]
    searched = []
    while search_deq:
        person = search_deq.popleft()
        if person not in searched:
            if person_seler(person):
                print(f'{person} is a seller!')
                return True
            else:
                search_deq += graph[person]
                searched.append(person)
    print('No seller')

search('you')
