arr = [5,3,1,6,4,2]
def min_max(arr):
    min = arr[0]
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]
    return min, max
print(min_max(arr))

print(f"Minimum: {min(arr)}, Maximum: {max(arr)}")