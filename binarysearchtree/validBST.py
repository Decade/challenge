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
import functools

def validBST(tree):
    if len(tree) < 2:
        return True
    thisroot = tree[0]
    subtrees = [(lessthan,list(subtree)) for lessthan, subtree in
                itertools.groupby(tree[1:], key = lambda x: x < thisroot)]
    if len(subtrees) == 1: return validBST(subtrees[0][1])
    if len(subtrees) > 2 or subtrees[0][0] == False: return False
    return functools.reduce(lambda x, y: x and validBST(y[1]),subtrees)

def main():
    cases = int(input())
    for i in range(cases):
        length = int(input())
        if length > 0:
            testcase = [int(i) for i in input().split(' ')]
            print("YES" if validBST(testcase) else "NO")
        else: print ("YES")

if __name__ == '__main__': main()

