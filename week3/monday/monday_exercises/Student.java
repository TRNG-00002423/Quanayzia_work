import java.util.Objects;

/**
 * Lab 2 — Student. Replace UnsupportedOperationException bodies with real logic.
 * See ../README.md
 */
public class Student {
    // TODO: private static nextId, private static count of instances
    // TODO: private final int id; private String name; private String program

    private final int id;


    private  String name;
    private String program;

    private static  int nextId;
    private static int instanceCount;



    public Student(String name, String program) {

        this.id=instanceCount;
        Student.instanceCount++;

        //throw new UnsupportedOperationException("TODO assign id, increment count");
    }

    public int getId() {
        return this.id;

        //throw new UnsupportedOperationException("TODO");
    }

    public String getName() {

        return this.name;

        //throw new UnsupportedOperationException("TODO");
    }

    public String getProgram() {

        return this.program;
        //throw new UnsupportedOperationException("TODO");
    }

    public void setName(String name) {
        this.name=name;


        //throw new UnsupportedOperationException("TODO");
    }

    public void setProgram(String program) {

        this.program=program;

        //throw new UnsupportedOperationException("TODO");
    }

    public static int getEnrollmentCount() {
        return Student.instanceCount;


        //throw new UnsupportedOperationException("TODO");
    }

    @Override
    public String toString() {
        throw new UnsupportedOperationException("TODO");
    }

    @Override
    public boolean equals(Object o) {
        throw new UnsupportedOperationException("TODO — same id => equal");
    }

    @Override
    public int hashCode() {
        throw new UnsupportedOperationException("TODO — consistent with equals");
    }
}