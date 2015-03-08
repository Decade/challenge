
var readline = require('readline');

var rl = readline.createInterface({
  input: process.stdin
});

var getmonth = function (monthstring){ // Expects a 3-character month like Apache gives
  "use strict";
  var months = [0,'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
      i = months.indexOf(monthstring);
  return i < 10? '0' + i : i ;
};

var parsedate = function (datestring) { // Expects an Apache date-time string like [10/Oct/2000:13:55:36 -0700]
  "use strict";                         // INCLUDING BRACKETS
  var day = datestring.slice(1,3),
      month = getmonth(datestring.slice(4,7)),
      year = datestring.slice(8,12),
      time = datestring.slice(13,21),
      tz = datestring.slice(22,27)
  ;
  return year + '-' + month + '-' + day + 'T' + time + '.000' +
    (+tz === 0 ? 'Z' : tz);
};

var parseline = function (line){
  "use strict";
  var quoteareas = line.split('"'), // 0 is before quote, 1 is in first quote, 2 is outside first quote, 3 is inside next quote...

      firstareas = quoteareas[0].split(' '), // 0 is IP, 1 is identity, 2 is user, 3 and 4 are date in brackets
      ip = firstareas[0],
      identity = firstareas[1] === '-'? null : firstareas[1],
      user = firstareas[2] === '-'? null : firstareas[2],
      datestring = parsedate(firstareas[3] + ' ' + firstareas[4]),

      requestareas = quoteareas[1].split(' '), // 0 is method, 1 is url, 2 is protocol
      method = requestareas[0],
      url = requestareas[1],
      protocol = requestareas[2],

      midareas = quoteareas[2].split(' '), // 0 is spacer, 1 is status, 2 is bytes
      status = +midareas[1],
      bytes = +midareas[2],

      referer = quoteareas[3] === '-' ? null: quoteareas[3],
      // quoteareas[4] is space between quotation marks
      useragent = quoteareas[5] === '-' ? null: quoteareas[5]
  ;

  return {
    remote: ip,
    identity: identity,
    user: user,
    date: datestring,
    method: method,
    url: url,
    protocol: protocol,
    status: status,
    bytes: bytes,
    referer: referer,
    "user-agent": useragent
  };
}

rl.on('line', function (line) {
  "use strict";
  console.log(JSON.stringify(parseline(line)));
}).on('close', function () {
  "use strict";
  process.exit(0);
});