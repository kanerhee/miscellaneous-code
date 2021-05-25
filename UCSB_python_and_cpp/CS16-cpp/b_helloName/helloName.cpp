// BASIC input/output using cin and cout with a string

#include <iostream>
#include <string>
using namespace std;

int main() {
  
  string name;
  cout << "What is your name? ";
  getline(cin, name);
  cout << "Hello, " << name << "!\n";

  return 0;
}
