// Given a string and a second "word" string, we'll say that the word matches the string if it appears at the front of the string, except its first char does not need to match exactly. On a match, return the front of the string, or otherwise return the empty string. So, so with the string "hippo" the word "hi" returns "hi" and "xip" returns "hip". The word will be at least length 1.

public String startWord(String str, String word) {
  int wordLen = word.length();
  int strLen = str.length();
  String strFront = "";
  String wordEnd = word.substring(1,wordLen);
  if(strLen >= wordLen){
    strFront = str.substring(0,word.length());
    strLen = strFront.length();

    if(!(strFront.substring(1,strLen).equals(wordEnd))){
      strFront = "";
    }
  }

  return strFront;
}
