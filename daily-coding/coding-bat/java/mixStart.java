// Return true if the given string begins with "mix", except the 'm' can be anything, so "pix", "9ix" .. all count.

public boolean mixStart(String str) {
  boolean match = false;
  String front = "";

  if(str.length() <= 2){
    //break
  } else {
    front = str.substring(1,3);
  }

  if (front.equals("ix") ){
    match = true;
  }
  return match;
}
