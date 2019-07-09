// Given a string, return true if "bad" appears starting at index 0 or 1 in the string, such as with "badxxx" or "xbadxx" but not "xxbadxx". The string may be any length, including 0. Note: use .equals() to compare 2 strings.

public boolean hasBad(String str) {
  String bad = "bad";
  boolean match = false;
  boolean bad1 = false;
  boolean bad2 = false;
  int length = str.length();

  if(length < 3){
    //break
  } else if(length == 3){
    bad1 = bad.equals(str.substring(0,3));
  } else if(length > 3){
    bad1 = bad.equals(str.substring(0,3));
    bad2 = bad.equals(str.substring(1,4));
  }

  return bad1 || bad2;
}
