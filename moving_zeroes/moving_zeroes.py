'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        # make sure we flip at an index that isn't 0
        while arr[end] == 0:
            end -= 1
            if start == end:
                break

        if arr[start] == 0:
            arr[start], arr[end] = arr[end], arr[start]
            end -= 1

        start += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
