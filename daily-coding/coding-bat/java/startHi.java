// Given a string, return true if the string starts with "hi" and false otherwise.

public boolean startHi(String str) {
  boolean hello = false;
  int length = str.length();
  if (length <= 1) {
    //break
  } else if (str.substring(0,2).equals("hi")){
    hello = true;
  }
  return hello;
}
