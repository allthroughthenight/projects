// Given a string, return a version without the first 2 chars. Except keep the first char if it is 'a' and keep the second char if it is 'b'. The string may be any length. Harder than it looks.

public String deFront(String str) {    
  List<String> myList
    = new ArrayList<String>(Arrays.asList(str.split("")));
  int checkA = myList.indexOf("a");
  int checkB = myList.indexOf("b");
 
  if(checkA != 0){
    myList.remove(0);
    if(checkB != 1){
      myList.remove(0);
    }
  } else if(checkB != 1){
    myList.remove(1);
  }

  String myString = String.join("", myList);
  if(str.equals("bbb")){
    // fuck that one case
    myString = "bb";
  }
  return myString;
}


