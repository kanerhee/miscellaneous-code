#include <iostream>
#include <cmath>
#include <cstdlib>
#include <string>
#include <iomanip>
using namespace std;

struct Valet {
  string name;
  double totalDrop;
  double totalHours;
  double average;
  double take;
};

double inputDrops(string valet_name) {
  double drop;
  double totalDrop = 0;
  cout << "For valet: " << valet_name << endl;
  cout << "Enter each drop per shift, or total amount dropped." 
       << "Enter 0 if there are no more drops to submit." << endl;
  do {
    cin >> drop;
    totalDrop += drop;
  } while (drop != 0);
  return totalDrop;
}

double inputHours(string valet_name) {
  double hours;
  cout << "Now for valet: " << valet_name << endl;
  cout << "Enter total hours worked in the week. Hit enter to submit: ";
  cin >> hours;
  return hours;
}

//MAIN OF FUNCTION
int main() {
  
  int staff_size = 19;
  double bacaraTotalDrop = 0;
  double bacaraTotalHours = 0;
  double bacaraAverage;
  
  string Valet_names[19] = {"Michael Forrester", "Mitch Miller",
				    "Joe Ferrick", "Cam Sprunk",
				    "Maxx Schnurr", "Christian Basulto",
				    "Dylan Rohde", "Jake Tursick",
				    "Cameron Cripe",
				    "Anthony Spiritosanto", "Max Scarnnechia",
				    "Kane Rhee", "Kevin Cannon",
				    "Justin Cifelli", "Austin Wieck",
				    "Ben Kilpatrick", "Stefan Valenzuela",
				    "Cody Drew", "Cooper Hamilton"};
 
  Valet staff[19];
  
  // FORLOOP TO INPUT STATS FOR ALL VALET
  for (int i=0; i<staff_size; i++) {
    staff[i].name = Valet_names[i];
    staff[i].totalDrop = inputDrops(staff[i].name);
    bacaraTotalDrop += staff[i].totalDrop;
    staff[i].totalHours = inputHours(staff[i].name);
    bacaraTotalHours += staff[i].totalHours;
    cout << endl;
  }

  cout.setf(ios::fixed);
  cout.setf(ios::showpoint);
  cout.precision(2);

  bacaraAverage = (bacaraTotalDrop/bacaraTotalHours);

  // FORLOOP TO CALCULATE AVERAGE AND TAKE FOR ALL VALET
  for (int i=0; i<staff_size; i++) {
    staff[i].average = (staff[i].totalDrop/staff[i].totalHours);
    staff[i].take = (staff[i].totalHours*bacaraAverage);
  }
  
  cout << endl;
  cout << endl;
  cout << endl;

  // FORLOOP THAT OUTPUTS ALL RESULTS IN A FORMATTED MANNER
  cout << setw(25) << "Name: " << setw(15) << "Total Hours:" << setw(15)
       << "Total Drop:" << setw(15) << "Average:" << setw(15)
       << "Take:" << endl;
  for (int i=0; i<staff_size; i++) {
    cout << setw(25) << staff[i].name << setw(15) << staff[i].totalHours
	 << setw(15) << staff[i].totalDrop << setw(15) << staff[i].average
	 << setw(15) << staff[i].take << endl;
  }
  cout << endl;
  cout << "          Bacara Total Drop: " << bacaraTotalDrop << endl;
  cout << "          Bacara Total Hours: " << bacaraTotalHours << endl;
  cout << "          Average for the week: " << bacaraAverage << endl;
  cout << "          Done." << endl;
  return 0;
}