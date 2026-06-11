

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

    public static int binarySearch(int[] sorted, int target){

        int lo=0;
        int hi=sorted.length-1;
    


        //interate through the list- while loop is best

        while(lo<=hi){
             // find the median index 
        int med= lo+(hi-lo)/2;

        // if target is found, return the index
        if(target==sorted[med]){
            return med;

        }else if(target<sorted[med]){
            hi=med-1;
    
        }else{

            lo=med+1; 
        }

        }
       
        return -1; 
    }
    

}
