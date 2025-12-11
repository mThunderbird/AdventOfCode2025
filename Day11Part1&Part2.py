import queue

from Util import  fetch_input

from collections import deque

data = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

data_2 = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

big_data = fetch_input("https://adventofcode.com/2025/day/11/input")


def paths(data, start, end):


    # Construct adjacency list for graph
    graph = {}
    for r in data.split("\n"):
        key = r.split()[0].replace(":", "")
        for n in r.split()[1:]:
            graph[key] = graph.get(key, []) + [n]
            graph[n] = graph.get(n, [])

    indegree = {u: 0 for u in graph.keys()}
    for u in graph.keys():
        for v in graph[u]:
            indegree[v] += 1

    # Kahn's algorithm to find topological ordering
    q = deque([u for u in graph.keys() if indegree[u] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    dp = {key: 0 for key in graph.keys()}
    dp[end] = 0

    dp[start] = 1
    i = topo.index(start)

    while i < len(topo) and topo[i] != end:
        for n in graph.get(topo[i], []):
            dp[n] += dp[topo[i]]
        i += 1

    return dp[end]

def part1(data):
    return paths(data, "you", "out")

def part2(data):

    route1 = (paths(data, "svr", "fft")
              * paths(data, "fft", "dac")
              * paths(data, "dac", "out"))
    route2 = (paths(data, "svr", "dac")
              * paths(data, "dac", "fft")
              * paths(data, "fft", "out"))

    return route1 + route2

print(part1(data))
print(part1(big_data))

print(part2(data_2))
print(part2(big_data))