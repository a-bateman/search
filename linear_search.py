def linear_search(list_to_search, target):
    counter = 0
    for x in list_to_search:
        if x == target:
            return True, counter
        counter += 1
    return False


search_list = [12,453,6545,235,76576]
target = 232

print(linear_search(search_list, target))