// Create your an Event Tracker object. 
var EventTracker = function(name){
    this.name = name;
    this._events = {};
    this._notify = {};
}

// extend the `EventTracker` prototype to "on"
EventTracker.prototype.on = function(event, callback){
    if (this._events[event] === undefined){
        this._events[event] = [];
    }
    this._events[event].push( callback );
};

// extend the `EventTracker` prototype to "notify"
EventTracker.prototype.notify = function(trackerObject, event){
    if (this._notify[event] === undefined){
        this._notify[event] = [];
    }
    this._notify[event].push( trackerObject );
};

// extend the `EventTracker` prototype to "trigger"
EventTracker.prototype.trigger = function(event, someData){
    var listOfCallbacks = this._events[event] || 0;
    var objectsToNotify = this._notify[event] || 0;
    var count;

    for (count = 0; count < listOfCallbacks.length; count++){
        listOfCallbacks[count].call(this, someData); 
    }

    for (count = 0; count < objectsToNotify.length; count++){
        objectsToNotify[count].trigger(event, someData);
    }
};











// Create your own Event Tracker system:
//
// 1. create an `EventTracker` object
//    • it should accept a name when constructed
// 2. extend the `EventTracker` prototype with:
//    • an `on` method
//    • a `notify` method
//    • a `trigger` method
//
// EXAMPLE:
// function purchase(item) { console.log( 'purchasing ' + item); }
// function celebrate() { console.log( this.name + ' says birthday parties are awesome!' ); }
//
// var nephewParties = new EventTracker( 'nephews ');
// var richard = new EventTracker( 'Richard' );
//
// nephewParties.on( 'mainEvent', purchase );
// richard.on( 'mainEvent', celebrate );
// nephewParties.notify( richard, 'mainEvent' );
//
// nephewParties.trigger( 'mainEvent', 'ice cream' );



