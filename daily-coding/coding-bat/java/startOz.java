// Given a string, return a string made of the first 2 chars (if present), however include first char only if it is 'o' and include the second only if it is 'z', so "ozymandias" yields "oz".

public String startOz(String str) {
  String charO = "";
  String charZ = "";
  String strOz = "";

  if(str.length() < 1){
    //break
  } else if(str.length() == 1){
    charO = str.substring(0,1);
  } else {
    charO = str.substring(0,1);
    charZ = str.substring(1,2);
  }

  if(charO.equals("o")){
    strOz += "o";
  }
  if(charZ.equals("z")){
    strOz += "z";
  }
  return strOz;
}
