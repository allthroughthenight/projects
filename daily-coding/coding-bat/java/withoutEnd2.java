// Given a string, return a version without both the first and last char of the string. The string may be any length, including 0.

public String withouEnd2(String str) {
  int length = str.length();
  String middle = "";

  if(length <= 1){
    // break
  } else {
    middle = str.substring(1,length - 1);
  }
  return middle;
}
