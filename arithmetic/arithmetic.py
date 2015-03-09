
"""
Input string is a number or an expression
Expression is a number, operator, and a valid input string

Number is digits
Operators are +-

"""

def parsetimesdivide(input_str):
    acc3 = 1
    dividesornumber = input_str.split('*') # Elements are either number or / expression
    for finalstuff in dividesornumber:
        grr = finalstuff.split('/')
        acc4 = int(grr[0])
        for grrrr in grr[1:]:
           acc4 /= int(grrrr)
           print("acc4 " + str(acc4))
        acc3 *= acc4
        print("acc3 " + str(acc3))
    return acc3
    

def parseplusminus(input_str):
    acc = 0
    thing = input_str.split('+') # Elements are either number or other expression
    for el in thing:
        acc2 = 0
        other = el.split('-') # Elements of "other" are either number or * / expression
        acc2 = parsetimesdivide(other[0])
        for more in other[1:]:
            acc2 -= parsetimesdivide(more)
        acc += acc2
    return acc

def calc(input_str):
    return parseplusminus(input_str)




