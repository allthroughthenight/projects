// Return true if the given string contains between 1 and 3 'e' chars.

public boolean stringE(String str) {
  String[] myArray = str.split("");
  int count = 0;
  boolean match = false;
  for(int i = 0; i < myArray.length;i++){
    if(myArray[i].equals("e")){
      count += 1;
    }
  }
  if((count >= 1) && (count <= 3)){
    match = true;
  }
  return match;
}
