public String minCat(String a, String b) {
	int aLen = a.length();
	int bLen = b.length();
	int diff = Math.abs(aLen - bLen);
	String theCat = "";

	if(aLen > bLen){
		theCat = a.substring(diff, aLen) + b;
	} else {
		theCat = a + b.substring(diff, bLen);
	}
	return theCat;
}
