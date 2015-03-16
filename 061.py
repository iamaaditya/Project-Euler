# Project Euler problem 61

def make_polygon(sides):
    n = 1
    while True:
        if sides == 3:
            yield n * (n + 1) / 2
        elif sides == 4:
            yield n * n 
        elif sides == 5:
            yield n * (3*n - 1) / 2
        elif sides == 6:
            yield n * (2*n - 1)
        elif sides == 7:
            yield n * (5*n - 3) / 2
        elif sides == 8:
            yield n * (3*n - 2)
        else:
            raise Exception("Incorrect sides entered")
        n += 1


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] :
            path_id = [i[0] for i in path]
            if next[0] in path_id:
                continue
            if next not in set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))


def get_numbers():
    polygon = [make_polygon(i) for i in xrange(3,9)]
    values = []
    for j in xrange(1000):
        for index, i in enumerate( polygon ):
                v  = i.next()
                if v > 999 and v < 10000: 
                    values.append(( index , v, v//100, v%100))
    return values

def make_graph():
    all_numbers =  get_numbers()
    graph = {}
    for i in all_numbers:
        graph[i] = []
        for j in all_numbers:
            if i[2] == j[3]:
                graph[i].append(j)
    return graph

def search_solution():
    g = make_graph()
    for k1 in g:
        for k2 in g:
            for sols in dfs_paths(g, k1,k2):
                if sols[0][3] == sols[-1][2] and len(sols)==6:
                    print sum([i[1] for i in sols])
                    return

search_solution()


