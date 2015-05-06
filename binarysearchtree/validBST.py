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
        subtrees = itertools.groupby(iterator, key = lambda x: x < thisroot)
        seenright = False
        for lessthan, subtree in subtrees:
            if seenright: return False
            if not validBST(subtree): return False
            seenright = not lessthan
        return True
    except StopIteration:
        return True

def main():
    cases = int(input())
    for i in range(cases):
        length = int(input())
        print("YES" if validBST(int(i) for i in input().split(' ')) else "NO")

if __name__ == '__main__': main()
