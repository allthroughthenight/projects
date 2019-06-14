// Given a string, return a string made of the chars at indexes 0,1, 4,5, 8,9 ... so "kittens" yields "kien".

public String altPairs(String str) {
  String[] myArray = str.split("");
  String myString = "";
  int length = myArray.length;

  for(int i = 0; i < length;){
    myString += myArray[i];
    if(i % 2 == 0){
      i+=1;
    } else {
      i+=3;
    }
  }
  return myString;
}
