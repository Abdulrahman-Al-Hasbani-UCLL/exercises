def split_in_two(ns):
    left = ns[:len(ns)//2]
    right = ns[(len(ns)//2):]

    return (left, right)

def merge_sorted(ks, ns):
    result = []
    i = 0
    j = 0
    while i < len(ks) and j < len(ns):
        if ks[i] < ns[j]:
            result.append(ks[i])
            i += 1
        else:
            result.append(ns[j])
            j += 1
    result.extend(ks[i:])
    result.extend(ns[j:])
    return result

def merge_sort(ns):
    if len(ns) <= 1:
        return ns

    left, right = split_in_two(ns)
    return merge_sorted(left.sort(), right.sort())