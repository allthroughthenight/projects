// Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

public String left2(String str) {
  int length = str.length();
  String front = str.substring(0,2);
  String back = str.substring(2,length);

  return back + front;
}
