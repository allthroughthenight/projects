// Given a string, if the first or last chars are 'x', return the string without those 'x' chars, and otherwise return the string unchanged.

public String withoutX(String str) {
  int length = str.length();
  String back = "";
  String front = "";
  String without = str;
  boolean tooShort = length <= 1;

  if(!tooShort){
    back = str.substring(length - 1, length);
    front = str.substring(0,1);
  }

  if(str.equals("x") || tooShort){
    without = "";
  }

  if(front.equals("x") && !tooShort){
    without = without.substring(1,length);
    length = without.length();
  }

  if(back.equals("x") && !tooShort){
    without = without.substring(0,length - 1);
  }

  return  without;
}
