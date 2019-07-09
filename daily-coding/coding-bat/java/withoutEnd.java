// Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

public String withoutEnd(String str) {
  int length = str.length();
  String middle = str.substring(1, length - 1);
  return middle;
}
