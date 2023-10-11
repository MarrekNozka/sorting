import random


def get_random_list(count, min=0, max=100):
    seznam = []
    if min >= max:
        raise ValueError("max must be great then min")
    for _ in range(count):
        seznam.append(random.randint(min, max))
        # seznam += [ random.randint(min,max) ]
    # seznam = [ random.randint(min,max) for _ in range(n) ]

    return seznam


if __name__ == "__main__":
    print(get_random_list(10))
