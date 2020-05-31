import java.io.*;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class ReadFileIntoArrayList {
    public static void main(String[] args) {
        String fileName = "example.txt";
    }

    void UsingFilesV1(String fileName)
    {
        try {
            ArrayList<String> lines = new ArrayList<>(Files.readAllLines(Paths.get(fileName)));
        }
        catch (IOException e) {
            // Handle a potential exception
        }
    }

    void UsingFilesV2(String fileName)
    {
        try {
            Charset charset = StandardCharsets.UTF_8;
            ArrayList<String> lines = new ArrayList<>(Files.readAllLines(Paths.get(fileName), charset));
        }
        catch (IOException e) {
            // Handle a potential exception
        }
    }

    void UsingScanner(String fileName)
    {
        // We'll use "-" as our delimiter
        ArrayList<String> arrayList = new ArrayList<>();
        try (Scanner s = new Scanner(new File(fileName)).useDelimiter("\\s*-\\s*")) {
            // \\s* in regular expressions means "any number or whitespaces".
            // We could've said simply useDelimiter("-") and Scanner would have
            // included the whitespaces as part of the data it extracted.
            while (s.hasNext()) {
                arrayList.add(s.next());
            }
        }
        catch (FileNotFoundException e) {
            // Handle the potential exception
        }
    }

    void UsingBufferedReader(String fileName)
    {
        ArrayList<String> arrayList = new ArrayList<>();

        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            while (reader.ready()) {
                arrayList.add(reader.readLine());
            }
        }
        catch (IOException e) {
            // Handle a potential exception
        }
    }

    void UsingObjectInputStream(String fileName)
    {
        try {
            ObjectOutputStream objectOutputStream =
                    new ObjectOutputStream(new FileOutputStream("data.olivera"));

            MyClass first = new MyClass(1, "abc");
            MyClass second = new MyClass(2, "abc");

            objectOutputStream.writeObject(first);
            objectOutputStream.writeObject(second);
            objectOutputStream.close();

            ObjectInputStream objectInputStream =
                    new ObjectInputStream(new FileInputStream("data.olivera"));

            ArrayList<MyClass> arrayList = new ArrayList<>();

            try (objectInputStream) {
                while (true) {
                    Object read = objectInputStream.readObject();
                    if (read == null)
                        break;

                    // We should always cast explicitly
                    MyClass myClassRead = (MyClass) read;
                    arrayList.add(myClassRead);
                }
            } catch (EOFException e) {
                // This exception is expected
            }

            for (MyClass m : arrayList) {
                System.out.println(m.someInt + " " + m.someString);
            }
        }
        catch (IOException e)
        {
            // Handle a potential exception
        }
        catch (ClassNotFoundException e)
        {
            // Handle a potential exception
        }
    }

    void UsingStreams(String fileName)
    {
        // Using try-with-resources so the stream closes automatically
        try (Stream<String> stream = Files.lines(Paths.get(fileName))) {
            ArrayList<String> arrayList = stream.collect(Collectors.toCollection(ArrayList::new));
        }
        catch (IOException e) {
            // Handle a potential exception
        }
    }
}
