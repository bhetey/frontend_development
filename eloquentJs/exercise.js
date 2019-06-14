/* Eloquent Javascript
 * Chapter 2 : Program Structure
 * Looping a triangle
 */
let count = 7;
let counter = 0;
let tri = "";

while (counter < count) {
  counter++;
  tri = tri + "#";
  console.log(tri);
}

/*
* Eloquent solution 
for (let line = "#"; line.length < 8; line += "#")
  console.log(line);

*/

/*
 * FIZZBUZZ
 */
for (let start = 1; start <= 100; start++) {
  if (start % 3 == 0 && start % 5 == 0) {
    console.log("FizzBuzz");
  } else {
    if (start % 3 == 0) {
      console.log("Fizz");
    } else {
      if (start % 5 == 0) {
        console.log("Buzz");
      } else {
        console.log(start);
      }
    }
  }
}

/*
* Eloquent solution for this.
for (let n = 1; n <= 100; n++) {
  let output = "";
  if (n % 3 == 0) output += "Fizz";
  if (n % 5 == 0) output += "Buzz";
  console.log(output || n);
}
*/

/**
 * Chessboard
 * Write a program that creates a string that represents an 8×8 grid,
 * using newline characters to separate lines.
 * At each position of the grid there is either a space or a "#" character.
 * The characters should form a chessboard.
 */

function chessBoard(width, height) {
  let gridString = "";
  let gridHash = "#";
  // a loop in a loop is need. TBC -->>>>
}
