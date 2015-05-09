# Now with 45 minutes, but getting the corners right takes a bit more time. Total time within a couple hours so far, though, probably.
import functools
from fractions import Fraction

def rationalize(term):
    return Fraction(*(int(i) for i in term.split(',')))
def derationalize(term):
    return str(term.numerator) + ',' + str(term.denominator)

def calculatediv(term):
    divterms = term.split('/')
    return functools.reduce(lambda x,y: x/y, (rationalize(i) for i in divterms[1:]), rationalize(divterms[0]))

def calculatefactor(term):
    multterms = term.split('*')
    return functools.reduce(lambda x,y: x*y, (calculatediv(i) for i in multterms))

def calculateandsubtract(addterm):
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
                input = str(calculaterational(input[:index])) + '*' + input[index+1:]
            else:
                input = str(calculaterational(input[:index])) + input[index+1:]
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

def calculaterational(input):
    input = doparens(input)
    addterms = input.split('+')
    return derationalize(functools.reduce(lambda x,y: x+y, (calculateandsubtract(i) for i in addterms)))

def calculate(input):
    value = rationalize(calculaterational(input))
    return value.numerator if value.denominator == 1 else value.numerator/value.denominator

