# Now with 45 minutes, but getting the corners right takes a bit more time.
import functools
from fractions import Fraction

def calculatediv(term):
    divterms = term.split('/')
    return functools.reduce(lambda x,y: x/y, (int(i) for i in divterms[1:]), Fraction(divterms[0]))

def calculatefactor(term):
    multterms = term.split('*')
    return functools.reduce(lambda x,y: x*y, (calculatediv(i) for i in multterms))

def calculateadd(addterm):
    subtractterms = addterm.split('-')
    prefixsubtractterms = []
    for index, term in enumerate(subtractterms):
        if term == '':
            subtractterms[index+1] = '-1*' + subtractterms[index+1]
        else:
            prefixsubtractterms.append(term)
    return functools.reduce(lambda x,y: x-y, (calculatefactor(i) for i in prefixsubtractterms))

def doparenactive(input):
    for index, character in enumerate(input):
        if character == '(':
            if index > 0 and input[index-1] not in '+-*/(':
                input = input[:index] + '*' + doparenactive(input[index+1:])
            else:
                input = input[:index] + doparenactive(input[index+1:])
            return doparenactive(input)
        if character == ')':
            if index + 1 < len(input) and input[index+1] not in '+-*/)':
                input = str(calculate(input[:index])) + '*' + input[index+1:]
            else:
                input = str(calculate(input[:index])) + input[index+1:]
            return input

def doparens(input):
    for index, character in enumerate(input):
        if character == '(':
            if index > 0 and input[index-1] not in '+-*/(':
                input = input[:index] + '*' + doparenactive(input[index+1:])
            else:
                input = input[:index] + doparenactive(input[index+1:])
            return doparens(input)
    return input

def calculate(input):
    input = doparens(input)
    addterms = input.split('+')
    value = functools.reduce(lambda x,y: x+y, (calculateadd(i) for i in addterms))
    return value.numerator if value.denominator == 1 else value.numerator/value.denominator

