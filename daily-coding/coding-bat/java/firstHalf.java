// Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

public String firstHalf(String str) {
  int length = str.length();
  String half = str.substring(0,length/2);
  return half;
}
