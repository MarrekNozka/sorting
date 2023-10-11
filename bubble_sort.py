from sorting.genetator import get_random_list
from copy import deepcopy

seznam = get_random_list(20)

print(seznam)

def buble_sort(list_):
    result = deepcopy(list_)
    max_ = len(result) - 1
    while max_ > 0:
        i = 0
        while i < max_:
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1],  result[i]
            i += 1
        max_ -= 1

    return result

print(buble_sort(seznam))

