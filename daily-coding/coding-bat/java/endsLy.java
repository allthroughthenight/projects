// Given a string, return true if it ends in "ly".

public boolean endsLy(String str) {
  int length = str.length();
  boolean match = false;
  String end = "";
  if(length <= 1){
    // break
  } else {
    end = str.substring(length - 2, length);
  }

  return end.equals("ly");
}
