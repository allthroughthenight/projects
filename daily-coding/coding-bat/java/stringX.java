// Given a string, return a version where all the "x" have been removed. Except an "x" at the very start or end should not be removed.

public String stringX(String str) {
  String[] myArray = str.split("");
  String newString = "";
  int length = myArray.length;

  for(int i = 0; i < length; i++){
    // if the item is an 'x' and is either the first or last item
    if((myArray[i].equals("x")) && ((i == 0) || (i == length-1))){
      newString += myArray[i];
    }
    // if the item is not an 'x' and not either the first or last item
    if(!(myArray[i].equals("x")) && ((i != 0) || (i != length))){
      newString += myArray[i];
    }
  }

  return newString;
}
