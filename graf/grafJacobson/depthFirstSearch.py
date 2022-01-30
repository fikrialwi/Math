def dfs(visisted,graph, node):
    if node not in visisted:
        visisted.add(node)
        print(node, end='->')
        for neighboor in graph[node]:
            dfs(visisted,graph,neighboor)


graph = {
    1 : [3,2],
    2 : [1],
    3 : [1,4],
    4 : [3]
}
visisted = set()