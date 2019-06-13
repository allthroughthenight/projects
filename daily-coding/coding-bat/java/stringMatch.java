// Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

public int stringMatch(String a, String b) {
  String[] aArray = a.split("");
  String[] bArray = b.split("");
  int lenA = aArray.length;
  int lenB = bArray.length;
  int lenShort = lenA;
  int count = 0;

  if(lenB < lenA){
    lenShort = lenB;
  }

  for(int i = 0; i < lenShort - 1; i++){
    if((aArray[i]+aArray[i+1]).equals(bArray[i]+bArray[i+1])){
      count += 1;
    }
  }

  return count;
}
