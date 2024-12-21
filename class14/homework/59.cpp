// Name: Owen Shi
// Date: Dec. 19th, 2024
// Asks the user until a pos. int

#include <iostream>
using namespace std;

int main() {
  int age = 0;
  cout << "Please enter age: ";
  cin >> age;

  while (age < 0) {
    cout << "Entered a negative number. \n";
    cout << "Please enter age: ";
    cin >> age;
  }

  cout << "You entered your age as: " << age;

  return 0;
}
