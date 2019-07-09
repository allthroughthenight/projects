// Given a string, return a string length 1 from its front, unless front is false, in which case return a string length 1 from its back. The string will be non-empty.

public String theEnd(String str, boolean front) {
  int length = str.length();
  String myChar = "";

  if(front){
    myChar = str.substring(0, 1);
  } else {
    myChar = str.substring(length - 1, length);
  }

  return myChar;
}
