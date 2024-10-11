# Function to compare the triplets
def compare_triplets(c, d):
    # Initialize points for Charlie and Dave
    charlie_points = 0
    dave_points = 0

    # Compare each score
    for i in range(len(c)):
        if c[i] > d[i]:
            charlie_points += 1
        elif c[i] < d[i]:
            dave_points += 1
    
    # Return the result as a tuple
    return charlie_points, dave_points

# Input handling
c = list(map(int, input("Enter Charlie's scores: ").split()))
d = list(map(int, input("Enter Dave's scores: ").split()))

# Get the result
result = compare_triplets(c, d)

# Output the result
print(result[0], result[1])