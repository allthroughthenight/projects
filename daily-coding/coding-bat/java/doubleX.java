// Given a string, return true if the first instance of "x" in the string is immediately followed by another "x".

boolean doubleX(String str) {
  String[] myArray = str.split("");
  int length = myArray.length;
  boolean match = false;

  for(int i = 0; i < length - 1; i++){
    if((myArray[i]+myArray[i+1]).equals("xx") && !match){
      match = true;
    }
  }
  return match;
}
