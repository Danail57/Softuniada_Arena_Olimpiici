def merge_sort(array):
    """
    base case: if the array has 1 or 0 elements => it is already sorted
    """
    if len(array) <= 1:
        return array

    # finding the middle
    middle_array_part = len(array) // 2
    left_array = array[:middle_array_part]
    right_array = array[middle_array_part:]

    # recursively call the function for the two halves
    left_array_sorted = merge_sort(left_array)
    right_array_sorted = merge_sort(right_array)

    return merge(left_array_sorted, right_array_sorted)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

numbers = [int(nums) for nums in input().split()]
sorted_numbers = merge_sort(numbers)
print("Sorted array:",*sorted_numbers)
