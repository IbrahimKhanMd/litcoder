def findCommonElements(arr1, arr2, arr3):
    # Initialize pointers for all three arrays
    i, j, k = 0, 0, 0
    common_elements = []

    # Loop through all arrays while the pointers are within their bounds
    while i < 3 and j < 3 and k < 3:
        # If all three elements are the same, it's a common element
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            common_elements.append(arr1[i])
            i += 1
            j += 1
            k += 1
        # Move the pointer of the array with the smallest element
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    # If common elements exist, print them, otherwise print "NO Elements"
    if common_elements:
        print(' '.join(map(str, common_elements)))
    else:
        print("NO Elements")

# Input handling with default array size as 3
if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = list(map(int, input().split()))
    findCommonElements(arr1, arr2, arr3)