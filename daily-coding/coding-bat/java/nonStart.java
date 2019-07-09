// Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

public String nonStart(String a, String b) {
  int aLength = a.length();
  int bLength = b.length();
  String aEnd = a.substring(1,aLength);
  String bEnd = b.substring(1,bLength);

  return aEnd + bEnd;
}
