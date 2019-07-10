// Given a string of any length, return a new string where the last 2 chars, if present, are swapped, so "coding" yields "codign".

public String lastTwo(String str) {
  int length = str.length();
  String swapped = "";

  if(length < 2){
    swapped = str;
  } else {
    swapped = str.substring(0,length - 2)
    + str.substring(length - 1, length)
    + str.substring(length - 2, length - 1);
  }

  return swapped;
}
