// Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

public int last2(String str) {
  String[] myArray = str.split("");
  String theEnd = "";
  int length = myArray.length;
  int count = 0;

  if(length > 2){
    theEnd = myArray[length-2] + myArray[length-1];
  }

  for(int i = 0; i < length-2;i++){
    if((myArray[i]+myArray[i+1]).equals(theEnd)){
      count += 1;
    }
  }

  return count;
}
