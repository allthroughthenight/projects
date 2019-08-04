// Start with 2 int arrays, a and b, each length 2. Consider the sum of the values in each array. Return the array which has the largest sum. In event of a tie, return a.

public int[] biggerTwo(int[] a, int[] b) {
	int sumA = 0;
	int sumB = 0;
	int[] large = a;
	for (int value : a) {
		sumA += value;
	}

	for (int value : b) {
		sumB += value;
	}
	if(sumB > sumA){
		large = b;
	}
	return large;
}

