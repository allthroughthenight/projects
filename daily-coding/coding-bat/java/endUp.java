// Given a string, return a new string where the last 3 chars are now in upper case. If the string has less than 3 chars, uppercase whatever is there. Note that str.toUpperCase() returns the uppercase version of a string.

public String endUp(String str) {
  String[] myArray = str.split("");
  String endCaps = "";
  int length = myArray.length;

  if(myArray.length <= 3){
    endCaps = str.toUpperCase();
  } else {
    for(int i = length - 1; i > length - 4; i--){
      myArray[i] = myArray[i].toUpperCase();
    }
    endCaps = String.join("",myArray);
  }

  return endCaps;
}
