def calculate_ratios(arr):
    n=len(arr)
    
    positives = sum(1 for x in arr if x>0)
    negatives = sum(1 for x in arr if x<0)
    zeros     = sum(1 for x in arr if x==0)
    
    positive_ratio = positives/n
    negative_ratio  = negatives/n
    zero_ratio      = zeros/n
    
    print(f"{positive_ratio:.3f}")
    print(f"{negative_ratio:.3f}")
    print(f"{zero_ratio:.3f}")
    
n = int(input())

arr = list(map(int,input().split()))
calculate_ratios(arr)