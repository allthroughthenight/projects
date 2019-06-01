// Given a string, if the string "del" appears starting at index 1, return a string where that "del" has been deleted. Otherwise, return the string unchanged.

public String delDel(String str) {
  String myStr = "";
  int length = str.length();
  if(length <= 3){
    myStr = str;
  } else if (str.substring(1,4).equals("del")){
    myStr = str.substring(0,1) + str.substring(4);
  } else {
    myStr = str;
  }
  return myStr;
}
