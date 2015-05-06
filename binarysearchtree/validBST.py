# Return whether a pre-order traversal comes from a valid BST.
# BST has values to the left lower, values to the right higher, compared to a root. (In this case, higher or equal)
# Pre-order traversal goes: Root, left subtree, right subtree. And each subtree goes similarly.
# Example:
#     5
#    / \
#   3   7
#      /
#     6
# Gives: 5 3 7 6. Valid.
#
# Main function: Do tests from stdin.
# Line 1: How many tests.
# Line 2n+1: How many nodes.
# Line 2n+2: Space-separated pre-order traversal list.

import itertools

def validBST(tree):
    iterator = iter(tree)
    try:
        thisroot = next(iterator)
    except StopIteration:
        return True
    subtrees = itertools.groupby(iterator, key = lambda x: x < thisroot)
    seenright = False
    for islefttree, subtree in subtrees:
        if seenright: return False
        if not validBST(subtree): return False
        seenright = not islefttree
    # Theory of why that works:
    # itertools.groupby groups consecutive values by what the key function maps them to.
    #   And returns an iterator of tuples of the key value and an iterator that leads to that key value
    # In this case, the key function returns True when the value belongs on a left subtree.
    # A valid sequence of subtrees would have 0 or 1 left subtrees followed by 0 or 1 right subtrees.
    # There is at most 1 left subtree before a right subtree.
    # So, if you see any subtree grouping after a right subtree, then it's a left subtree, and that's invalid.
    return True

def main():
    cases = int(input())
    for i in range(cases):
        length = int(input())
        print("YES" if validBST(int(i) for i in input().split(' ')) else "NO")

if __name__ == '__main__': main()
