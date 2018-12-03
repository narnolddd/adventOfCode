from itertools import *
from collections import Counter

def read_lines():
    import sys
    raw = sys.stdin.read()

    for line in raw.split():
        if not line: continue
        yield line



def part_one():
    ids = list(read_lines())
    n_contains_duplicate = sum(1 for word in ids if 2 in Counter(word).values())
    n_contains_triplicate = sum(1 for word in ids if 3 in Counter(word).values())
    checksum = n_contains_duplicate * n_contains_triplicate
    print(checksum)


def differ_barely(a, b):
    n_differ = sum(achar != bchar for achar, bchar in zip(a, b))
    return n_differ == 1


def part_two():
    # need just two strings that differ by a single letter
    import pygtrie as trie
    # Build a prefix tree out of the words
    t = trie.CharTrie()
    ids = list(read_lines())
    # Populate trie, values are random (True)
    for word in ids:
        t[word] = True

    def trie_walk(path_conv, chars, children, whatsthis=None):
        path = path_conv(chars)
        # Got two subtrees here, where do they differ?
        words = list(t.keys(path))
        if len(words) == 2 and differ_barely(*words):
            # Found them! Propagate them back up
            return words
        if len(words) < 1:
            return
        if len(words) > 2:
            # we need to go deeper, this results in recursive call
            result = list(children)
            # Either there is one result, or none
            # Filter out the result and bubble back up
            result = list(filter(lambda x: x, result))
            result = result[0] if result else None
            return result

    res = t.traverse(trie_walk)

    # Now just print the common letters
    for a, b in zip(*res):
        if a == b:
            print(a, end='')
    print()


if __name__ == "__main__":
    part_two()

