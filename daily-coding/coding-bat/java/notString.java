// Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged. Note: use .equals() to compare 2 strings.

public String notString(String str) {

  String[] myArray = str.split(" ");

  if(myArray[0].equals("not")) {
    return str;
  }
  else {
    return "not " + str;
  }
}
