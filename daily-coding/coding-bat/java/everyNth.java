// Given a non-empty string and an int N, return the string made starting with char 0, and then every Nth char of the string. So if N is 3, use char 0, 3, 6, ... and so on. N is 1 or more.

public String everyNth(String str, int n) {
  String[] myArray = str.split("");
  String myString = "";
  int length = myArray.length;

  for(int i = 0;i < length;i ++){
    if(i%n != 0){
      //break
    } else {
      myString += myArray[i];
    }
  }

  return myString;
}
