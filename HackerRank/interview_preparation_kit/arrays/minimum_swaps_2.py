def minimumSwaps(arr):
    ref_arr = sorted(arr)
    index_dict = {v: i for i, v in enumerate(arr)}
    swaps = 0

    for i, v in enumerate(arr):
        correct_value = ref_arr[i]
        if v != correct_value:
            to_swap_ix = index_dict[correct_value]
            arr[to_swap_ix], arr[i] = arr[i], arr[to_swap_ix]
            index_dict[v] = to_swap_ix
            index_dict[correct_value] = i
            swaps += 1

    return swaps


"""def minimumSwaps(arr):
    # initialize number of swaps as 0 
    swaps = 0
    # create a dictionary which holds value, index pairs of our array
    # [4,3,1,2] --> {4: 1, 3: 2, 1: 3, 2: 4}
    getIndex = dict(zip(arr, range(1, len(arr) + 1)))
    for i in range(1, len(arr) + 1):
        # swap only if value is not equal to index
        if getIndex[i] != i:
            
            # Example of a proper swap when i=1
            # {4: 1, 3: 2, 1: 3, 2: 4} --> {4: 3, 3: 2, 1: 1, 2: 4}
            # [4,3,1,2] --> [1,3,4,2]
            # Full swap is not required i.e. we don't have to set 1:1 or arr[0]=1(i:i or arr[i-1]=i) because we will never use these two values again. Therefore we can keep these two values as it is. And thus our swap looks as follows.
            # {4: 1, 3: 2, 1: 3, 2: 4} --> {4: 3, 3: 2, 1: 3, 2: 4}
            # [4,3,1,2] --> [4,3,4,2]
            
            getIndex[arr[i - 1]] = getIndex[i]
            arr[getIndex[i] - 1] = arr[i - 1]
            swaps += 1
    return swaps
"""

"""def minimumSwaps(arr):
    a = dict(enumerate(arr, 1))
    b = {v: k for k, v in a.items()}
    count = 0
    for i in a:
        x = a[i]
        if x != i:
            y = b[i]
            a[y] = x
            b[x] = y
            count += 1
    return count"""

"""
Esta solución tarda mucho para casos con muchos numeros TIME OUT
def minimumSwaps(arr):
    swaps = 0
    for first_index in range(len(arr)):
        if arr[first_index] != first_index + 1:
            second_index = arr.index(first_index + 1)
            arr[first_index], arr[second_index] = arr[second_index], arr[first_index]
            swaps += 1
    return swaps
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    print(minimumSwaps(arr))
