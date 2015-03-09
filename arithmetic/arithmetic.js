// Way too complicated arithmetic parser.
/*
  Context-free grammar:
    Expression is a term or a plus-minus expresion.
    Term is a number or a times-divide expression.
    Number is one or more digits, possibly with '-' in front.
    Times-divide expression is a term, a times/divide, a number.
    Plus-minus expression is an expression, a plus/minus, a term.
    Left-associative, doing mult/div precedence, but skipping parentheses, space unimportant.
    Fun fact: SFSU does not have a compiler class.
              CS graduates from SFSU who know really know compilers, did not learn it from SFSU.
	      But there is an elective, CSC 413, where a simple compiler is shown and modified.
	      That compiler uses exceptions for normal program flow control.
*/
function basic_calculator(inputString) {
    var trimmedString = inputString.replace(/\s/g,'');
    var digit = {};
    var plusminus = {};
    var timesdivide = {};
    var terminals = {'+': plusminus, '-': plusminus, '*': timesdivide, '/': timesdivide};
    var i;
    for (i = 0; i < 10; ++i) terminals[i] = digit;
    var readExpression = function (input, start, end){
	var result = readTerm(input, start, end);
	return "number" === typeof(result) ? result: readPlusMinus(input, start, end);
    };
    var readTerm = function(input, start, end){
	var result = readNumber(input, start, end);
	return "number" === typeof(result)? result: readTimesDivide(input, start, end);
    };
    var readNumber = function(input, start, end){
	var result = [];
	if (input[start] === '-') {
	    result[0] = '-';
	    ++start;
	}
	for (var i = start; i < end; ++i)
	    if (terminals[input[i]] === digit)
		result[result.length] = input[i];
	    else
		return undefined;
	if (result.length === 0 || result.length === 1 && result[0] === '-') return undefined;
	return parseInt(result.reduce(function(x,y) { return x + y }, ''));
    };
    var readTimes = function(input, start, end, position){
	var left = readTerm(input, start, position);
	var right = readNumber(input, position+1, end);
	return "number" === typeof(left) && "number" === typeof(right)? left * right: undefined;
    };
    var readDivide = function(input, start, end, position){
	var left = readTerm(input, start, position);
	var right = readNumber(input, position+1, end);
	return "number" === typeof(left) && "number" === typeof(right)? left / right: undefined;
    };
    var readPlus = function(input, start, end, position){
	var left = readExpression(input, start, position);
	var right = readTerm(input, position+1, end);
	return "number" === typeof(left) && "number" === typeof(right)? left + right: undefined;
    };
    var readMinus = function(input, start, end, position){
	var left = readExpression(input, start, position);
	var right = readTerm(input, position+1, end);
	return "number" === typeof(left) && "number" === typeof(right)? left - right: undefined;
    };
    var readTimesDivide = function(input, start, end){
	var timesPosition = input.lastIndexOf('*',end);
	timesPosition = timesPosition > start && timesPosition < end? timesPosition: -1;
	var dividePosition = input.lastIndexOf('/',end);
	dividePosition = dividePosition > start && dividePosition < end? dividePosition: -1;
	if (timesPosition > 0 && dividePosition > 0)
	    return timesPosition > dividePosition?
	    readTimes(input, start, end, timesPosition):
	    readDivide(input, start, end, dividePosition);
	else if (timesPosition > 0 && dividePosition < 0)
	    return readTimes(input, start, end, timesPosition);
	else if (dividePosition > 0 && timesPosition < 0)
	    return readDivide(input, start, end, dividePosition);
	else return undefined;
    };
    var readPlusMinus = function(input, start, end){
	var plusPosition = input.lastIndexOf('+',end);
	plusPosition = plusPosition > start && plusPosition < end? plusPosition: -1;
	var minusPosition=end, beforeMinus;
	do {
	    minusPosition = input.lastIndexOf('-',minusPosition-1);
	    minusPosition = minusPosition > start && minusPosition < end? minusPosition: -1;
	    beforeMinus = minusPosition > 0? terminals[input[minusPosition-1]]:null;
	} while (minusPosition > 0 && (beforeMinus === plusminus || beforeMinus === timesdivide));
	if (plusPosition > 0 && minusPosition > 0)
	    return plusPosition > minusPosition?
	    readPlus(input, start, end, plusPosition):
	    readMinus(input, start, end, minusPosition);
	else if (plusPosition > 0 && minusPosition < 0)
	    return readPlus(input, start, end, plusPosition);
	else if (minusPosition > 0 && plusPosition < 0)
	    return readMinus(input, start, end, minusPosition);
	else return undefined;
    };
    var result = readExpression(trimmedString,0,trimmedString.length);
    if (result !== undefined) return result;
    else throw "Unable to interpret";
}

// Test section
var trials = [
  ["0", 0],
  ["3+4", 7],
  ["-3-4", -7],
  ["-3 - -4*2", 5],
  ["-32 / -4*2 - -2/-4", 15.5]
];

for (var i = 0; i < trials.length; i++) {
  var received = basic_calculator(trials[i][0]);
  var expected = trials[i][1];

  console.log(trials[i][0]
        + ": "
        + received
        + (expected == received ? " ==" : " !=")
        + " " + expected + " (expected)");
}
