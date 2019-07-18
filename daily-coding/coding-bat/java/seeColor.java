// Given a string, if the string begins with "red" or "blue" return that color string, otherwise return the empty string.

public String seeColor(String str) {
  String red = "red";
  String blue = "blue";
  String found = "";
  int length = str.length();

  if(length < 3){
    //break
  } else if(length == 3 && red.equals(str.substring(0,3))){
    found = red;
  } else if(red.equals(str.substring(0,3))){
    found = red;
  } else if(length >= 4 && blue.equals(str.substring(0,4))){
    found = blue;
  }
  return found;
}
