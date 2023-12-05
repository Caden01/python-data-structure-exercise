def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    value_frequency = {num: nums.count(num) for num in nums}
    
    highest_frequency = 0

    for (val, freq) in value_frequency.items() :
        if freq > highest_frequency :
            highest_frequency = val 

    
    return highest_frequency 

print(mode([1, 2, 1]))
