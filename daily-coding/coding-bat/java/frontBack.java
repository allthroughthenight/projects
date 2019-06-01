// Given a string, return a new string where the first and last chars have been exchanged.

public String frontBack(String str) {
  int length = str.length();
  String backFront = "";
  if (length <= 1){
    backFront = str;
  } else{
    backFront += str.substring(length-1);
    backFront += str.substring(1,length-1);
    backFront += str.substring(0,1);
  }
  return backFront;
}
