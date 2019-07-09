// Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "". Note that str.length() returns the length of a string.

public String firstTwo(String str) {
  String front = "";
  if (str.length() == 0){
    front = "";
  } else if (str.length() == 1){
    front = str;
  } else {
    front = str.substring(0,2);
  }

  return front;
}
