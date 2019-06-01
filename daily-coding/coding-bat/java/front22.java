// Given a string, take the first 2 chars and return the string with the 2 chars added at both the front and back, so "kitten" yields"kikittenki". If the string length is less than 2, use whatever chars are there.

public String front22(String str) {
  int length = str.length();
  String together = "";
  String front = "";

  if (length == 0) {
    //break;
  } else if (length <= 2){
    together = str + str + str;
  } else {
    front = str.substring(0,2);
    together = front + str + front;
  }
  return together;
}
