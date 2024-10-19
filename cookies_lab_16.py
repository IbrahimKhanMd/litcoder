import heapq

def min_steps_to_target_sweetness(target, candies):
    heapq.heapify(candies)  # Convert the list into a heap
    steps = 0

    while len(candies) > 1 and candies[0] < target:
        # Pop the two least sweet candies
        least_sweet = heapq.heappop(candies)
        second_least_sweet = heapq.heappop(candies)
        
        # Combine them into a new candy
        new_candy = least_sweet + 2 * second_least_sweet
        
        # Add the new candy back into the heap
        heapq.heappush(candies, new_candy)
        
        # Increment the step counter
        steps += 1

    # After combining, if the sweetness of the least sweet candy is still less than the target
    if candies[0] < target:
        return -1  # Not possible to reach the target sweetness
    
    return steps

# Input
target = int(input())  # Target sweetness level
candies = list(map(int, input().split()))  # List of candy sweetness values

# Output the number of steps
print(min_steps_to_target_sweetness(target, candies))