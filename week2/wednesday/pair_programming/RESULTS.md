Results for test 1:
Array Size: 1000000
Target: 667934

Results for Linear Search
Time elapsed: 2436500 ns

Results for Binary Search
Time elapsed: 10700 ns

Linear Search took longer: 2436500 ns



Results for Test 2:
Array Size: 1000000
Target: 790200

Results for Linear Search
Time elapsed: 2664400 ns

Results for Binary Search
Time elapsed: 9700 ns

Linear Search took longer: 2664400 ns



# Search Benchmark Report

## Table: Round 1 and Round 2 Results

| Test | Array Size | Linear Search Time | Binary Search Time |
|------|------------|--------------------|---------------------|
| 1    | 1,000,000  | 2,436,500 ns       | 10,700 ns           |
| 2    | 1,000,000  | 2,664,400 ns       | 9,700 ns            |

---

## Expected vs Actual Behavior

### Linear Search (O(n))
Linear search goes through the array one item at a time. As the array gets bigger, it takes longer. In both tests, it took about 2–3 milliseconds, which is expected for scanning a large array.

### Binary Search (O(log n))
Binary search splits the array in half each time. Even with 1,000,000 elements, it only takes about 20 steps. That is why it stays consistently fast in both tests.

---

## Caveat

These times are not perfectly stable because Java performance changes while running. The JVM may optimize code after it runs. CPU caching and background processes also affect timing.

Big-O matters because it shows how performance scales as input grows, even if exact times change.
