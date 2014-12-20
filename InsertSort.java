package cs61b_algo;

/**
 * @author Z
 *
 * "insertion sort", compares the ITEM to each of the items before the current searching item
 */

import java.util.Arrays;

public class InsertSort {

    public static void main(String[] args) {
	InsertSort sortA = new InsertSort();
	// int[] testArray = {2};
	int[] testArray = { 2, 111, 66, 76, 65, 1, 5, 3 };
	sortA.inSorted(testArray);
	System.out.println(Arrays.toString(testArray));

    }

    public void inSorted(int[] inputArray) {

	int len = inputArray.length;
	int c = 1;

	// assume the 1st item is in order, start searching the unsorted part
	// from the 2nd item in the array
	for (int i = 1; i < len; i++) {
	    int temp = inputArray[i];

	    // to compare each of the items before the position item

	    for (int j = i - 1; j >= 0; j--) { // everything before the current
					       // ITEM
		if (temp < inputArray[j]) {
		    inputArray[j + 1] = inputArray[j];
		    inputArray[j] = temp;
		    // System.out.println(c++);
		}
	    }
	}
    }
}

/* array[] or linked-list?
 * 
 * in array structure, the runtime is in O(n^2);
 * in balanced binary tree, the runtime is O(nlog(n))
 */