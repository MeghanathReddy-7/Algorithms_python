def shortestpath(current, count, cost, cycle):
    if no == count and graph[current][0] > 0:
        cycle = min(cycle, cost + graph[current][0])
        return cycle
    for i in range(no):
        if not visited[i] and graph[current][i] > 0:
            visited[i] = True
            cycle = shortestpath( i, count + 1, cost + graph[current][i], cycle)
            visited[i] = False
    return cycle
no = int(input("Enter number of Cities: "))
graph = [[0] * no for i in range(no)]
for i in range(no):
    for j in range(no):
        graph[i][j] = int(input("Enter Distance from City " + str(i+1) + " to City " + str(j+1) + " "))
visited = [False] * no
visited[0] = True
cycle = float('inf')
cycle = shortestpath( 0, 1, 0, cycle)
print("Minimum Price is ",cycle)