// Given two strings, append them together (known as "concatenation") and return the result. However, if the concatenation creates a double-char, then omit one of the chars, so "abc" and "cat" yields "abcat".

public String conCat(String a, String b) {
  int aLength = a.length();
  int bLength = b.length();

  String aEnd = "";
  String cat = "";

  if(aLength < 0){
    aEnd = a.substring(aLength - 1, aLength);
  }

  if(aLength == 0 || bLength == 0){
    cat = a + b;
  } else if(aEnd.equals(b.substring(0,1))){
    cat = a.substring(0,aLength - 1) + b;
  } else {
    cat = a + b;
  }

  return cat;
}
