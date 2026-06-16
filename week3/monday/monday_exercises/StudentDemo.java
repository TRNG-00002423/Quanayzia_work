/** Lab 2 driver — run after Student is implemented. */
public class StudentDemo {
    public static void main(String[] args) {

        Student s1 = new Student("Alice", "CS");
        Student s2 = new Student("Bob", "Math");
        Student s3 = new Student("Charlie", "Physics");

        Student s4= s3;

        System.out.println("Enrollment count: " + Student.getEnrollmentCount());

        System.out.println(s3 == s4);
        System.out.println(s3.equals(s4));



        System.out.println(s1 == s2);
        System.out.println(s1.equals(s2));


        // TODO: create 3 Student instances, print enrollment count,
        // demonstrate equals vs == with two references to same id scenario if possible
    }
}