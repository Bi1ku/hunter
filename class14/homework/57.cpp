// Name: Owen Shi
// Date: Dec. 19th, 2024
// Determine what happy season it is!

#include <iostream>
using namespace std;

int main() {
  int num;
  cout << "Enter month (as number): ";
  cin >> num;

  if (num < 3 || num > 11) {
    cout << "Happy Winter";
  } else if (num >= 3 && num < 7) {
    cout << "Happy Spring";
  } else if (num >= 7 && num < 9) {
    cout << "Happy Summer";
  } else {
    cout << "Happy Fall";
  }

  return 0;
}
