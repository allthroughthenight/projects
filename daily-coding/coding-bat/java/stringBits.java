// Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

public String stringBits(String str) {
  String[] myArray = str.split("");
  String newStr = "";
  int length = myArray.length;

  for(int i = 0; i < length;i+=2){
    newStr = newStr + myArray[i];
  }

  return newStr;
}
