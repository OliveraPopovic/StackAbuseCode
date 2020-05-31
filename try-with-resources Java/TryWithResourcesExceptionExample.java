public class TryWithResourcesExceptionExample {
    public static class MyResource implements AutoCloseable {
        // method throws RuntimeException
        public void doSomething() {
            throw new RuntimeException("From the doSomething method");
        }

        // we'll override close so that it throws an exception in the implicit finally block of try-with-resources (when it attempts to close our resource)
        @Override
        public void close() throws Exception {
            throw new ArithmeticException("I can throw whatever I want, you can't stop me.");
        }
    }

    public static void main(String[] arguments) throws Exception {
        // declare our resource in try
        try (MyResource resource = new MyResource()) {
            resource.doSomething();
        }
        catch (Exception e) {
            System.out.println("Regular exception: " + e.toString());

            // getting the array of suppressed exceptions, and its length
            Throwable[] suppressedExceptions = e.getSuppressed();
            int n = suppressedExceptions.length;

            if (n > 0) {
                System.out.println("We've found " + n + " suppressed exceptions:");
                for (Throwable exception : suppressedExceptions) {
                    System.out.println(exception.toString());
                }
            }
        }
    }
}
