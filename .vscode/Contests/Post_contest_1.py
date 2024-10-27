def min_time_to_complete_tasks(num_tasks, task_durations, num_workers):
    def can_complete_in_time(time_limit): # function start 
        workers_needed = 1
        current_time = 0
        
        for duration in task_durations:
            if duration > time_limit:
                return False
                
            if current_time + duration > time_limit:
                workers_needed += 1
                current_time = duration
            else:
                current_time += duration
                
        return workers_needed <= num_workers

    left = max(task_durations)
    right = sum(task_durations)
    
    while left < right:
        mid = (left + right) // 2
        if can_complete_in_time(mid):
            right = mid
        else:
            left = mid + 1
            
    return left

# Accepting user input
num_tasks = int(input())
task_durations = list(map(int, input().split()))
num_workers = int(input())

# output function
print(min_time_to_complete_tasks(num_tasks, task_durations, num_workers))