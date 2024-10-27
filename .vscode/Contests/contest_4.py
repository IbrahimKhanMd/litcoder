def validate_input(start_times, end_times):
    """Validate input according to constraints"""
    if not start_times or not end_times:
        return False, "Invalid Input"
    if len(start_times) != len(end_times):
        return False, "Invalid Input"
    if len(start_times) <= 1:
        return False, "Invalid Input"
    # Check if all inputs are integers
    if not all(isinstance(x, int) for x in start_times + end_times):
        return False, "Invalid Input"
    return True, ""

def merge_intervals(start_times, end_times):
    # Validate input
    is_valid, error_msg = validate_input(start_times, end_times)
    if not is_valid:
        return [], 0, 0, error_msg

    # Create interval pairs and identify invalid intervals
    intervals = list(zip(start_times, end_times))
    invalid_count = sum(1 for start, end in intervals if start >= end)
    
    # Remove invalid intervals and sort by start time
    valid_intervals = [(start, end) for start, end in intervals if start < end]
    valid_intervals.sort(key=lambda x: x[0])
    
    if not valid_intervals:
        return [], 0, invalid_count, ""

    # Merge overlapping intervals
    merged = [valid_intervals[0]]
    non_overlapping_count = 1
    
    for current in valid_intervals[1:]:
        if current[0] > merged[-1][1]:  # No overlap
            merged.append(current)
            non_overlapping_count += 1
        else:  # Overlap found
            merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))
    
    return merged, non_overlapping_count, invalid_count, ""

def main():
    try:
        # Get input from user
        start_times = list(map(int, input("Enter start times separated by spaces: ").strip().split()))
        end_times = list(map(int, input("Enter end times separated by spaces: ").strip().split()))
        
        # Process intervals
        merged_intervals, non_overlapping_count, invalid_count, error_msg = merge_intervals(start_times, end_times)
        
        if error_msg:
            print(error_msg)
            return
            
        # Print results
        if merged_intervals:
            # Print merged intervals
            output = []
            for start, end in merged_intervals:
                output.extend([start, end])
            print(*output)
            
            # Print counts
            print(non_overlapping_count)
            print(invalid_count)
        else:
            print("No valid intervals found")
            
    except ValueError:
        print("Invalid Input")

if __name__ == "_main_":
    main()