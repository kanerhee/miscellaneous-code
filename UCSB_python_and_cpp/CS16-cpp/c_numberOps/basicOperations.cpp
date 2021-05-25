// Perform operations on a number
// Operations include:

#include <iostream>
using namespace std;

// Number Operations
double add(double your_number);

double subtract(double your_number);

double multiply(double your_number);

double divide(double your_number);

// Terminal UI
void print_menu(double your_number);

char get_command();

int main()
{
  double your_number;
  char command;

  cout << "Choose a number: ";
  cin >> your_number;
  cout << endl;
  cout << endl;

  do {
    print_menu(your_number);
    command = toupper(get_command());

    switch(command)
    {
      case 'S': // some function;
      break;
      case '1': add(your_number);
        break;
      case '2': subtract(your_number);
        break;
      case '3': multiply(your_number);
        break;
      case 'Q': // Do nothing...
        break;
      default: cout << "Invalid Input." << endl;
        break;
    }
  }
  while (command != 'Q');

  return(EXIT_SUCCESS);
}



//FUNCTION IMPLEMENTATIONS
double add(double your_number) {
  double a, b;
  cout << your_number << " + ";
  cin >> a;
  cout << " = " << (your_number + a);
  b = (your_number + a);
  return b;
}

double subtract(double your_number) {
  double a;
  cout << your_number << " - ";
  cin >> a;
  cout << endl << " = ";
  return your_number -= a;
}

double multiply(double your_number) {
  double a;
  cout << your_number << " * ";
  cin >> a;
  cout << endl << " = ";
  return your_number *= a;
}

double divide(double your_number) {
  double a;
  cout << your_number << " / ";
  cin >> a;
  cout << endl << " = ";
  return your_number /= a;
}

void print_menu(double your_number)
{
  cout << "----------------- The Commands -----------------" << endl;
  cout << "Your number is: " << your_number << endl;
  cout << "  -   -   -   -   -   -   -   -   -   -   -   -" << endl;
  cout << "1 - Add to your number" << endl;
  cout << "2 - Subract from your number" << endl;
  cout << "3 - Multiply to your number" << endl;
  cout << "  -   -   -   -   -   -   -   -   -   -   -   -" << endl;
  cout << "Q - quit this interactive test program" << endl;
  cout << "-------------------------------------------------" << endl;
}

char get_command()
{
  char command;

  cout << ">";
  cin >> command;

  return(toupper(command));
}