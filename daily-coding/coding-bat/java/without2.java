// Given a string, if a length 2 substring appears at both its beginning and end, return a string without the substring at the beginning, so "HelloHe" yields "lloHe". The substring may overlap with itself, so "Hi" yields "". Otherwise, return the original string unchanged.

public String without2(String str) {
  int length = str.length();
  String noFront = "";
  String front = "";
  String back = "";

  if(length < 2){
    noFront = str;
  } else {
    front = str.substring(0,2);
    back = str.substring(length - 2 ,length);
  }

  if(front.equals(back) && length >= 2){
    noFront = str.substring(2,length);
  } else {
    noFront = str;
  }
  return noFront;
}
