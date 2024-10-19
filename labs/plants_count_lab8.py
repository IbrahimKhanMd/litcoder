def most_common_plant(sightings):
    # Create a dictionary to store the frequency of each plant ID
    plant_count = {}
    
    # Count the frequency of each plant in the sightings
    for plant in sightings:
        if plant in plant_count:
            plant_count[plant] += 1
        else:
            plant_count[plant] = 1
    
    # Find the plant with the maximum frequency and smallest ID in case of a tie
    most_common = min(plant_count, key=lambda x: (-plant_count[x], x))
    
    # Output the most common plant
    print(most_common)

# Input handling
sightings_input = list(map(int, input().strip().split()))  # Take input as a list of integers directly

most_common_plant(sightings_input)
