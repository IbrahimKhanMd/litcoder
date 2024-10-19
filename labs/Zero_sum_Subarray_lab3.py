def zero_sum_subarray(arr):
    n = len(arr)
    if n < 1 or n > 10:
        print("Array size must be between 1 and 10")
        return
    sum_set = set()  
    current_sum = 0  
    for num in arr:
        current_sum += num
        if current_sum == 0 or current_sum in sum_set:
            print("True")
            print(n)
            return
        sum_set.add(current_sum)
    print("False")
    print(n)
arr = list(map(int, input().split()))
zero_sum_subarray(arr)
