// Given a string, return a new string made of 3 copies of the first 2 chars of the original string. The string may be any length. If there are fewer than 2 chars, use whatever is there.

public String extraFront(String str) {
  String triple = "";
  int length = str.length();
  int end = 2;
  if(length < 2){
    end = length;
  }

  return str.substring(0, end)
    + str.substring(0, end)
    + str.substring(0, end);
}
