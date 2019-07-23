// Given a string, if one or both of the first 2 chars is 'x', return the string without those 'x' chars, and otherwise return the string unchanged. This is a little harder than it looks.

public String withoutX2(String str) {
  List<String> myList
    = new ArrayList<String>(Arrays.asList(str.split("")));
  String oneX = "";
  String twoX = "";
  String myString = "";
  boolean tooShort = str.length() <= 1;

  if(!tooShort){
    oneX = myList.get(0);
    twoX = myList.get(1);
  }

  if(oneX.equals("x") && !tooShort){
    myList.remove(0);
    if(twoX.equals("x")){
      myList.remove(0);
    }
  } else if(twoX.equals("x")){
    myList.remove(1);
  }

  if(tooShort){
    myString = "";
  } else {
    myString = String.join("", myList);
  }

  return myString;
}
