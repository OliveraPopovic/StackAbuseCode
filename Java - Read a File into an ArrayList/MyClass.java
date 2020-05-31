import java.io.Serializable;

public class MyClass implements Serializable {
    int someInt;
    String someString;

    public MyClass(int someInt, String someString) {
        this.someInt = someInt;
        this.someString = someString;
    }
}