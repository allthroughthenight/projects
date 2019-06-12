// Given a non-empty string like "Code" return a string like "CCoCodCode".

public String stringSplosion(String str) {
  String[] myArray = str.split("");
  String newStr = "";
  int length = myArray.length;

  for(int i = 0; i < length; i++){
    for(int j = 0; j < i + 1; j++){
      newStr = newStr + myArray[j];
    }
  }
  return newStr;
}
