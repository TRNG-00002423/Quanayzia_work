import org.w3c.dom.ls.LSOutput;

/**
 * Lab 1 — Arrays & loops. Implement the bodies.
 * See ../README.md
 */
public class ArrayLoopsLab {

    /** Reverse array in place. */
    public static void reverse(int[] data) {

        // can use the two pointer method to reveres an array inplace
        // 1,2,3,4,5,6,7,8,9
        // l
        //
        int left=0;
        int right= data.length-1;

        while(left <=right){

            int swap=0;

            swap=data[left];
            data[left]=data[right];
            data[right]=swap;

            left++;
            right--;


        }


    }

    /** Smallest element; illegal if null or empty. */
    public static int min(int[] data) {
        if(data==null || data.length==0) throw new IllegalArgumentException("Array cannot be null or empty");

        int min=data[0];

        for(int i=1; i<data.length;i++){

            if(data[i]<min){
                min=data[i];
            }
        }
        return min;

    }

    /** Largest element; illegal if null or empty. */
    public static int max(int[] data) {
        if(data==null || data.length==0) throw new IllegalArgumentException("Array cannot be null or empty");

        int max=data[0];

        for(int i=1; i<data.length;i++){

            if(data[i]>max){
                max=data[i];
            }
        }
        return max;
    }

    /** In-place ascending sort using nested loops only (no Arrays.sort). */
    public static void sortAscending(int[] data) {

        for(int i=0; i<data.length-1;i++){
            int min=i;

            // interate until smallest is found
            for(int x = i + 1; x < data.length; x++){

                //compare data[min] with data[x]
                if (data[x] < data[min]) {
                    min = x;
                }
            }

            //swap
            int temp = data[i];
            data[i] = data[min];
            data[min] = temp;

        }
    }

    public static void main(String[] args) {
        // TODO: demo arrays — print before/after reverse and sort

        int[] data = {5, 2, 9, 1, 6, 3};

        // ---- ORIGINAL ----
        System.out.println("Original array:");
        printArray(data);

        // ---- REVERSE ----
        reverse(data);
        System.out.println("\nAfter reverse:");
        printArray(data);

        // ---- MIN / MAX ----
        System.out.println("\nMin: " + min(data));
        System.out.println("Max: " + max(data));

        // ---- SORT ----
        sortAscending(data);
        System.out.println("\nAfter sort ascending:");
        printArray(data);
    }


    public static void printArray(int[] data) {
        for (int num : data) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}