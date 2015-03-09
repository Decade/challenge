// This function is a reflection of my opinion that Javascript is a horrible language.
// There are neato closure stuff, but the type system is almost the worst type system ever.
// The worst is probably PHP.

function dedup(it){
  function objectcompare(a,b){
    var equalsofar = true;
    for (var i in a){
      if (a.hasOwnProperty(i)){
        if (!b.hasOwnProperty(i))
          return false;
        equalsofar = deepcompare(a[i],b[i]);
        if (!equalsofar) return false;
      }
    }
    for (i in b)
      if (b.hasOwnProperty(i))
        if(!a.hasOwnProperty(i))
          return false;
    return true;
  }
  function deepcompare(a,b){ // Some of these might be redundant
    var typea = typeof(a), typeb = typeof(b);
    if (typea !== typeb) return false;
    if (typea === 'number') return isNaN(a) ? isNaN(b) : a === b;
    if (typea === 'string') return a === b;
    if (typea === 'boolean') return !a^b;
    if (typea === 'undefined') return true;
    if (a === b) return true;
    return objectcompare(a,b);
  }
  var result = [];
  for (var i in it){
    var hasalready = false;
    for (var j in result){
      if (deepcompare(it[i],result[j])) {
        hasalready = true;
        break;
      }
    }
    if (!hasalready)
      result.push(it[i]);
  }
  return result;
}