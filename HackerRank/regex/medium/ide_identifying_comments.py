import re

code = """// my  program in C++
#include <iostream>
/** playing around in
a new programming language **/
using namespace std;
int main ()
{
  cout << "Hello World";
  cout << "I'm a C++ program"; //use cout
  return 0;
}"""
# import sys
# code = sys.stdin.read()
comments = re.findall(r'(?:(//.*?)\n|(/\*.*?\*/))', code, re.DOTALL)
[print(*comment) for comment in comments]
