// Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

public String frontTimes(String str, int n) {
  String[] myArray = str.split("");
  String front = "";
  String times = "";
  int myLength = myArray.length;

  if(myLength >= 3){
    myArray = Arrays.copyOfRange(myArray, 0, 3);
  } else {
    myArray = Arrays.copyOfRange(myArray, 0, myLength);
  }

  front = String.join("",myArray);

  for(int i = 0;i < n;i++){
    times += front;
  }

  return times;
}
