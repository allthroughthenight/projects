// Given 2 strings, a and b, return a new string made of the first char of a and the last char of b, so "yo" and "java" yields "ya". If either string is length 0, use '@' for its missing char.

public String lastChars(String a, String b) {
  int aLength = a.length();
  int bLength = b.length();
  String front = "";
  String back = "";
  if(aLength == 0){
    front = "@";
  } else {
    front = a.substring(0, 1);
  }

  if(bLength == 0){
    back = "@";
  } else {
    back = b.substring(bLength - 1, bLength);
  }

  return front + back;
}
