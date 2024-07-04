"""You are given a network of n nodes, labeledfrom
1 to n.You are also given times, a list of travel times as directed
edges times[i] = (ui, vi, wi), where
ui is the source node,
vi is the target node, and
wi is the time it takes for a signal to travel from source to target.

We
will
send
a
signal
from a given

node
k.Return
the
minimum
time
it
takes
for all the n nodes to receive the signal.If it is impossible for all the n nodes to receive the signal, return -1.

Example
1:

Input: times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], n = 4, k = 2
Output: 2
Example
2:

Input: times = [[1, 2, 1]], n = 2, k = 1
Output: 1
Example
3:

Input: times = [[1, 2, 1]], n = 2, k = 2
Output: -1

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All
the
pairs(ui, vi)
are
unique.(i.e., no
multiple
edges.)"""




import heapq


def networkDelayTime(times, n, k):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))

    # Step 2: Initialize the min heap with the start node
    min_heap = [(0, k)]  # (time, node)
    # Travel time to reach each node
    min_time = {i: float('inf') for i in range(1, n + 1)}
    min_time[k] = 0

    # Step 3: Process the nodes in the heap
    while min_heap:
        current_time, node = heapq.heappop(min_heap)

        # Explore neighbors
        for neighbor, time in graph[node]:
            new_time = current_time + time
            # If we find a shorter time path to neighbor, update and push to heap
            if new_time < min_time[neighbor]:
                min_time[neighbor] = new_time
                heapq.heappush(min_heap, (new_time, neighbor))

    # Step 4: Check if all nodes are reachable
    max_time = max(min_time.values())
    return max_time if max_time < float('inf') else -1


# Example usage
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))  # Output: 2
