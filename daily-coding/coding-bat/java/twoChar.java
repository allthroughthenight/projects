// Given a string and an index, return a string length 2 starting at the given index. If the index is too big or too small to define a string length 2, use the first 2 chars. The string length will be at least 2.

public String twoChar(String str, int index) {
  int length = str.length();
  String first = "";
  if(index < 0 || index > length - 2){
    first = str.substring(0, 2);
  } else{
    first = str.substring(index, index + 2);
  }
  return first;
}
