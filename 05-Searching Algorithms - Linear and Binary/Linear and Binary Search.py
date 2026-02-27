## Linear Search Algorithm
## time complexity: O(n)
## space complexity: O(1)

def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
    
## Driver code
arr = [20, 45, 27, 47, 55, 67, 75, 88, 90]
x = 67
## function calling
result = linearSearch(arr, x)
print("Searching element is present at index:",result)




## Binary Search Algorithm using recursion
def binarySearch(arr, x, i, j):
    while i <= j:
        mid = i + (j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            ## right side of the mid
            ## seach space - mid+1 to j
            ## recursion - calling the same function again inside the 
            return binarySearch(arr, x, mid+1, j)
        else:
            ## left side of the mid
            ## search space - i to mid-1
            return binarySearch(arr, x, i, mid-1)
    ## searching element is not present in an array
    return -1

## Driver code
arr = [20, 30, 40, 50, 60, 70, 80, 90]
x = 60
i = 0
j = len(arr) - 1
## function calling
result = binarySearch(arr, x, i, j)
print("Searching element is present at the location:",result)




## Binary Search Algorithm without using recursion(iterative)
def binarySearch(arr, x, i, j):
    while i <= j:
        ## lower bound while division
        mid = i + (j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            ## right side of the mid
            ## seach space - mid+1 to j
            i = mid + 1
            ## arr[mid] > x:
        else:
            ## left side of the mid
            ## search space - i to mid-1
            j = mid - 1
    ## searching element is not present in an array
    return -1

## Driver code
arr = [20, 30, 40, 50, 60, 70, 80, 90]
x = 20
i = 0
j = len(arr) - 1
## function calling
result = binarySearch(arr, x, i, j)
print("Searching element is present at the location:",result)