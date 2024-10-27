def find_provinces(isConnected):
    def dfs(city):
        visited[city] = True
        for neighbor in range(len(isConnected)):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    n = len(isConnected)
    visited = [False] * n
    province_count = 0

    for city in range(n):
        if not visited[city]:
            dfs(city)
            province_count += 1

    return province_count

# Read input
n = int(input())
isConnected = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(find_provinces(isConnected))