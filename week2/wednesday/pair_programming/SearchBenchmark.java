import java.util.Random;

public class SearchBenchmark {

    public static void main(String[] args) {

        final int N = 1_000_000;

        int[] sorted_arr = new int[N];

        for (int i = 0; i < N; i++) {
            sorted_arr[i] = i * 2;
        }

        Random random = new Random();
        int random_index = random.nextInt(N);
        int target = sorted_arr[random_index];

        System.out.println("Array Size: " + N);
        System.out.println("Target: " + target);

        // Linear Search
        long start_linear = System.nanoTime();
        SearchLib.linearSearch(sorted_arr, target);
        long end_linear = System.nanoTime();

        long diff = end_linear - start_linear;

        System.out.println("\nResults for Linear Search");
        System.out.println("Time elapsed: " + diff + " ns");

        // Binary Search
        long start_binary = System.nanoTime();
        SearchLib.binarySearch(sorted_arr, target);
        long end_binary = System.nanoTime();

        long diff2 = end_binary - start_binary;

        System.out.println("\nResults for Binary Search");
        System.out.println("Time elapsed: " + diff2 + " ns");

        if (diff > diff2) {
            System.out.println("\nLinear Search took longer: " + diff + " ns");
        } else {
            System.out.println("\nBinary Search took longer: " + diff2 + " ns");
        }
    }
}