// exercise 1: count through all MIDI note numbers from 0 to 127
// initialisation, termination, increment
// for (var i = 0; i <= 127; i = i + 1) {
//     console.log(i);
// }
// {} for a code block

// a variation:

// for (var i = 0; i <= 127; i++) {    // i + 1 can be abbreviated as i++
// console.log(i);
// }

// arithmetic series; we increment by addition or basic arithmetic

// ex. 2: geometric series

// for (var i = 1; i <= 127; i = i * 1.5) {    // i + 1 can be abbreviated as i++
//     console.log(i);
//     }

// exercise 3: build a harmonic series

// var f0 = parseFloat(prompt("Enter the base frequency (f0) in Hz:"));
// var numPartials = parseInt(prompt("How many partials should I make?:"));

// for (var i = 1; i <= numPartials; i++) {
//     var harmonicFrequency = (f0 * i).toFixed(2); 
//     console.log(harmonicFrequency);
// };

// toFixed: how many decimal places do I want?


// exercise 4:

var scale = [60, 62, 64, 65, 67, 69, 71, 72];

scale.forEach(function(note){
    console.log(note);
});