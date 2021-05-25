// BASIC input/output using cin and cout with a string
// basic use of getline and get function
// basic use of if/else statement 


#include <string>
#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

int main() {
  
  string name;
  char isName = 'n';

  cout << "What is yo name dawg? ";
  getline(cin, name);
  
  cout << "Hello.\n";
  cout << "So is yo name " << name << "?? (y/n)\n";
  cin >> isName;
  cout << endl << endl;

  if (isName == 'y') {
        cout << "Dawg that's a nice name," << name << ".\n";
  }
  else {
      cout << "Oops. My bad Dawg";
  }

  return 0;
}
