// Name: Owen Shi
// Date: Dec. 19th, 2024
// Calculate the interest for first five years

#include <iostream>
using namespace std;

int main() {
  float amt = 0;
  cout << "Please enter the starting amount: ";
  cin >> amt;

  cout << "Year 1  " << amt * 1.1 << "\n";
  amt = amt * 1.1;
  cout << "Year 2  " << amt * 1.1<< "\n";
  amt = amt * 1.1;
  cout << "Year 3  " << amt * 1.1<< "\n";
  amt = amt * 1.1;
  cout << "Year 4  " << amt * 1.1<< "\n";
  amt = amt * 1.1;
  cout << "Year 5  " << amt * 1.1<< "\n";
  amt = amt * 1.1;

  return 0;
}
