MOD = 1000000007

# Function to compute the number of ways to arrange bricks in a single row of width 'm'
def row_ways(m):
    dp = [0] * (m + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        dp[i] += dp[i - 1]  # Using brick of width 1
        if i >= 2:
            dp[i] += dp[i - 2]  # Using brick of width 2
        if i >= 3:
            dp[i] += dp[i - 3]  # Using brick of width 3
        if i >= 4:
            dp[i] += dp[i - 4]  # Using brick of width 4
        dp[i] %= MOD
    return dp[m]

# Function to compute the number of valid walls with no vertical cuts
def legoWall(n, m):
    # Compute ways to fill a single row of width 'm'
    row_combinations = [0] * (m + 1)
    for i in range(m + 1):
        row_combinations[i] = row_ways(i)

    # Total ways to build a wall of height 'n' is (ways to build a single row)^n
    total_ways_per_height = [pow(row_combinations[i], n, MOD) for i in range(m + 1)]

    # Compute the stable ways (no vertical splits)
    stable_ways = [0] * (m + 1)
    stable_ways[0] = 1
    for width in range(1, m + 1):
        stable_ways[width] = total_ways_per_height[width]
        for j in range(1, width):
            stable_ways[width] -= (stable_ways[j] * total_ways_per_height[width - j]) % MOD
            stable_ways[width] += MOD  # Ensure no negative values
            stable_ways[width] %= MOD

    return stable_ways[m]

# Input
n = int(input())
m = int(input())

# Output the number of ways modulo 1000000007
print(legoWall(n, m))