// Given a string, return a string length 2 made of its first 2 chars. If the string length is less than 2, use '@' for the missing chars.

public String atFirst(String str) {
  int length = str.length();
  String first = "";
  if (length == 0){
    first = "@@";
  } else if (length == 1){
    first = str + "@";
  } else {
    first = str.substring(0,2);
  }

  return first;
}
