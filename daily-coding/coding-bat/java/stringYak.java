// Suppose the string "yak" is unlucky. Given a string, return a version where all the "yak" are removed, but the "a" can be any char. The "yak" strings will not overlap.

public String stringYak(String str) {
  String[] myArray = str.split("");
  String noYak = "";
  int length = myArray.length;

  for(int i = 0;i < length; i++ ){
    if(i+2 < length){
      if(myArray[i].equals("y")
        && (myArray[i+2].equals("k"))){
          i += 3;
      }
    }

    if(i < length){
      noYak += myArray[i];
    }
  }
  return noYak;
}
