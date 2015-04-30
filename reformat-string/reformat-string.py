# Reformat a keystring.
# Idea: The keystring should be normalized to uppercase with the dashes distributed K letters apart
#       with the first segment being the short segment if the length is not a multiple of K.
# Inputs: S string, K int
# Output: New string
#         Also: O(N) time and space complexity.
def reformat(S, K):
    rawstring = ''.join(S.split('-')).upper()
    N = len(rawstring)
    remainder = N%K
    if remainder == 0:
        return '-'.join([rawstring[N-i:N-i+K] for i in range(N,0,-K)])
    else:
        return '-'.join([rawstring[:remainder]] + [rawstring[N-i:N-i+K] for i in range(N-remainder,0,-K)])
