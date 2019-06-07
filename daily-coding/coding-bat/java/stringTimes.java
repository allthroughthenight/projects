// Given a string and a non-negative int n, return a larger string that is n copies of the original string.

public String stringTimes(String str, int n) {
  String myString = "";
  for(int i = 0; i < n; i++){
    myString += str;
  }
  return myString;
}
