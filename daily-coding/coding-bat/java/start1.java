// Start with 2 int arrays, a and b, of any length. Return how many of the arrays have 1 as their first element.

public int start1(int[] a, int[] b) {
	int aLen = a.length;
	int bLen = b.length;
	int found = 0;

	if(aLen > 0){
		if(a[0] == 1){
			found += 1;
		}
	}

	if(bLen > 0){
		if(b[0] == 1){
			found += 1;
		}
	}

	return found;
}

