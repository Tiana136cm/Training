for _ in range(int(input().strip())):
    n = int(input().strip())
    graph = {}
    for _ in range(int(n)):
        u, v = map(int, input().strip().split())
        graph[u] = v

    def traverse(x, k, visited):
        return k if x in visited else traverse(graph[x], k + 1, visited | {x})

    res = [traverse(x, 0, set()) for x in range(1, n + 1)]
    print(res.index(max(res)) + 1)
