

// SearchLib.java — two static methods:
// linearSearch(int[] sorted, int target) → index or -1
// binarySearch(int[] sorted, int target) → index or -1

public class SearchLib {

    public static int linearSearch(int[] sorted, int target){

        for(int i=0; i<sorted.length; i++){

            if(target==sorted[i]){
                return i; 
            }
        }
        return -1;

    }

}
