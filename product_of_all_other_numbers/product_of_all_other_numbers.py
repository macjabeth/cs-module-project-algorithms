'''
Input: a List of integers
Returns: a List of integers
'''

'''
[1, 7, 3, 4]
[84, 12, 28, 21]
psf = 84
'''
def product_of_all_other_numbers(arr):
    products = [0] * len(arr)

    # For each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1

    for i in range(len(arr)):
        products[i] = product_so_far
        product_so_far *= arr[i]

    # For each integer, we find the product of all the integers
    # after it. Since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1

    for i in range(len(arr) - 1, -1, -1):
        products[i] *= product_so_far
        product_so_far *= arr[i]

    return products


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
