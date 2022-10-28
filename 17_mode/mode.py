def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1, 9 , 9, 9])
        9

        >>> mode([2, 2, 3, 3, 2, 2])
        2
    """
    lst={}
    for num in nums:
        if not lst.get(num):
            lst.update({num:1})
        else:
            lst[num]=lst[num]+1
    for key1 in lst:
        for key2 in lst:
            if lst[key1] > lst[key2]:
                result = key1
            elif lst[key1] < lst[key2]:
                result = key2
    return result
