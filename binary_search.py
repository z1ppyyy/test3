# pinkozz test file

def binary_search(arr, left, right, x):
    mid = (left + right) // 2

    if arr[mid] == x:
        return "Element found at position {}".format(mid)
    elif arr[mid] > x:
        return binary_search(arr, mid+1, right, x)
    else:
        return binary_search(arr, left-1, right, x)
    
arr = [1,2,3,4,5,6]
print(binary_search(arr, 0, len(arr)-1, 3))