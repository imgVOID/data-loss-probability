import random as module_random
import argparse


def mirror(x):
    quantity = 100
    data_fragments = [i for i in range(0, quantity)]
    subset_length = len(data_fragments) / (x / 2)
    data_set = []
    last = 0.0
    while last < len(data_fragments):
        data_set.append(data_fragments[int(last):int(last + subset_length)])
        last += subset_length
    for i in range(0, len(data_set)):
        data_set.append(data_set[i])
    return probability(data_set)


def random(x):
    quantity = 100
    data_set = [[] for i in range(0, x)]
    for i in range(0, quantity):
        for j in range(0, 2):
            random_subset = module_random.randrange(0, len(data_set))
            if i not in data_set[random_subset]:
                data_set[random_subset].append(i)
            elif j < 2 and i in data_set[random_subset]:
                while i in data_set[random_subset]:
                    random_subset = module_random.randrange(0, len(data_set))
                    if i not in data_set[random_subset]:
                        data_set[random_subset].append(i)
                        break
    return probability(data_set)


def probability(mas):
    combinations = 0
    data_losses = 0
    for i in range(0, x):
        for j in range(0, x):
            if i != j:
                t = [z for z in mas[i] if z in mas[j]]
                combinations += 1
                if len(t) > 0:
                    data_losses += 1
                else:
                    pass
            else:
                pass
    return \
        "Killing 2 arbitrary servers results in data loss in {}% cases".format(
            str(data_losses * 100 // combinations))


parser = argparse.ArgumentParser()
parser.add_argument("--random", action='store_true')
parser.add_argument("--mirror", action='store_true')
parser.add_argument('-n', action="store", dest="count", type=int)
args = parser.parse_args()

x = args.count

if args.random:
    print(random(x))
elif args.mirror:
    print(mirror(x))
else:
    pass
