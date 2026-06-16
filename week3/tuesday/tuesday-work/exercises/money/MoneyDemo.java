package money;

import java.util.HashSet;
import java.util.Set;

public class MoneyDemo {
    public static void main(String[] args) {
        // TODO: build Money USD 1000 cents twice, add to HashSet, print size
        // TODO: print equals vs ==


        Money m1 = new Money("USD", 1000);
        Money m2 = new Money("USD", 1000);

        // equals vs ==
        System.out.println("m1 == m2: " + (m1 == m2));
        System.out.println("m1.equals(m2): " + m1.equals(m2));

        // HashSet dedup test
        Set<Money> set = new HashSet<>();
        set.add(m1);
        set.add(m2);
        // because hashCode is the same and equals() returns true

        System.out.println("Set size: " + set.size());
    }
}