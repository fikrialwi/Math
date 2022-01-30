def bfs(graph,node):
    visisted =[node]
    queue = [node]

    while queue:
        s = queue.pop(0)
        print(s, end='->')

    for neighboor in graph[s]:
        if neighboor not in visisted:
            visisted.append(neighboor)
            queue.append(neighboor)



