def linear_search(list_to_search, target):
    counter = 0
    for x in list_to_search:
        if x == target:
            return True, counter
        counter += 1
    return False
