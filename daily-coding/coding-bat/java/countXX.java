// Count the number of "xx" in the given string. We'll say that overlapping is allowed, so "xxx" contains 2 "xx".// Count the number of "xx" in the given string. We'll say that overlapping is allowed, so "xxx" contains 2 "xx".

int countXX(String str) {
	String[] myArray = str.split("");
	int length = myArray.length;
	int count = 0;
	for(int i = 0; i < length - 1;i++){
		if((myArray[i]+myArray[i+1]).equals("xx")){
			count += 1;
		}
	}
	return count;
}

