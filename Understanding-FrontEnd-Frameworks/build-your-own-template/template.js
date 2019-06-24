var template = function(str, delims) {
  
  // declared delimiters as an object.  
  var delimiters = {
    open: '*(', // property for open delimiter
    close: ')*' // property for close delimiter.
  };

  var templateString = [];
  var count = 1; 
  var closingDelimiterLoc = 0;
  var functionArguments = [];
  var theVariable, remaining; 

  // wrap the str in quotes to make it a string. 
  var strWrapInQuotes = function ( str ){
    return "'" + str + "'";
  };

  for (var key in delims){
    if (delims.hasOwnProperty(key)){
      if (delims[key] != undefined){
        delimiters[key] = delims[key];
      }
    }
  }

  var segments = str.split(delimiters.open);
  var numOfSegments = segments.length;

  templateString.push(strWrapInQuotes(segments[0]));

  while (count < numOfSegments){
    closingDelimiterLoc = segments[count].indexOf(delimiters.close);
    
    theVariable = segments[count].slice(0, closingDelimiterLoc);
    functionArguments.push( theVariable );
    templateString.push(  theVariable );

    remaining = segments[count].slice(closingDelimiterLoc + delimiters.close.length );
    templateString.push(  strWrapInQuotes(remaining)  );

    count++;
  }

  templateString = 'while(turns--) { console.log(' + templateString.join('+') + ')}';

  return new Function ( functionArguments.join( ',' ), 'turns', templateString);
};
