with open('input.txt') as f:
    data = list(map(int, f.readlines()[0].split(' ')))

# example
# data = list(map(int, '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split(' ')))


def get_sum_metadata(sum_metadata, pos):
    n_children = data[pos]
    n_metadata = data[pos + 1]
    current_pos = pos + 2
    if n_children > 0:
        for i in range(n_children):
            sum_metadata, current_pos = get_sum_metadata(sum_metadata, current_pos)
    sum_metadata += sum(data[current_pos:current_pos + n_metadata])
    return sum_metadata, current_pos + n_metadata


def get_ref_sum_metadata(metadata, pos):
    n_children = data[pos]
    n_metadata = data[pos + 1]
    current_pos = pos + 2
    children_metadata = []
    if n_children > 0:
        for i in range(n_children):
            cm, current_pos = get_ref_sum_metadata(0, current_pos)
            children_metadata.append(cm)
        for i in data[current_pos:current_pos + n_metadata]:
            if 0 <= i - 1 < n_children:
                metadata += children_metadata[i - 1]
    else:
        metadata += sum(data[current_pos:current_pos + n_metadata])
    return metadata, current_pos + n_metadata


print(get_sum_metadata(0, 0)[0])
print(get_ref_sum_metadata(0, 0)[0])
