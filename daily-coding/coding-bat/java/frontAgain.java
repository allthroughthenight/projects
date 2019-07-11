public boolean frontAgain(String str) {
	int length = str.length();
	String front = "";
	String back = "";
	boolean match = false;

	if(length < 2){
		match = false;
	}

	if(length >= 2){
		front = str.substring(0, 2);
		back = str.substring(length - 2, length);
		if(front.equals(back)){
			match = true;
		}
	}

	return match;
}
