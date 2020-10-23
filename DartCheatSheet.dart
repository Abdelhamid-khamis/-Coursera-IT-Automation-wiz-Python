/*                          main function                   */
void main(List<String> args) {
  print("Hello, Dart!");

}






/*                          Variables, Data Types & Comments                  */

// Variables must be declared using the keywords 'const', 'final',
// 'var' or a type name(var) or (type name)
// وممكن اعرفه ف بداية الكود او قبل المتغير

var myAge = 35;             // inferred int, created wiz var
var pi = 3.14;              // inferred double
int yourAge = 27;           // type name(int)
double e = 2.178;           // double = float


// to write comments: (//) or (/**/)

// this is a comment
/* this is also a comment */


// dynamic can have value of any type

dynamic numberOfKittens;
numberOfKittens = 'There are no kittens!';    // dynamic string
numberOfKittens = 0;                          // dynamic int
numberOfKittens = 1.0;                        // dynamic double

bool areThereKittens = true;                  // bool

// Compile-time constants 
const speedOflight = 299792458; 

// Immutables with final 
final planet= 'Jupiter'; 

planet= 'Mars';   // error: planet is imutable 

// Enumerations 
enum Month { january, february, march, april, may, june, july, august, september, october, november, december 
}

final Month = Month.april;


