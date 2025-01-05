def pairwise_sum(list1, list2):
    """
    The function calculates the pairwise sum of the elements of two lists.
    Args:
        list1: The first list.
        list2: The second list. It is assumed that both lists are the same length.
    Returns:
        A list containing the pairwise sum of the elements from list1 and list2.
    """
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result