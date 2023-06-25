import java.io.*;
import java.util.*;
import java.util.stream.IntStream;


public class ToyStore {
    Queue<Toy> myQueue;
    int[] arrayId;
    int[] arrayFrequency;
    String[] names;
    Scanner scanner = new Scanner(System.in);
    Random random = new Random();

    public void getInfoAboutList() {
        System.out.println("This is your queue in the store.");
        while (!myQueue.isEmpty()) {
            System.out.println(myQueue.poll());
        }
    }

    public void addToy(int count) {
        arrayFrequency = new int[count];
        arrayId = new int[count];
        names = new String[count];
        for (int i = 0; i < count; i++) {
            try {
                System.out.println("Enter a id:");
                String str1 = scanner.next();
                int id = Integer.parseInt(str1);
                System.out.println("Enter a name:");
                String name = scanner.next();
                System.out.println("Enter a frequency:");
                String str2 = scanner.next();
                int frequency = Integer.parseInt(str2);
                checkResult(id, name, frequency);
                checkIdInArray(id);
                fillArrays(i, id, name, frequency);
            } catch (RuntimeException e) {
                System.out.println("You made a mistake ---> " + e.getMessage());
                System.out.println("This trying was not counted!");
                i--;
            }
        }
    }

    private void fillArrays(int i, int id, String name, int frequency) {
        arrayId[i] = id;
        names[i] = name;
        arrayFrequency[i] = frequency;
    }

    public void createQueue() {
        System.out.println("""
                You can choose priority for queue:
                1. Id priority
                2. Name priority
                3. Frequency priority
                """);
        String choice = scanner.next().strip();
        if (choice.equals("1")) {
            myQueue = new PriorityQueue<>((o1, o2) -> o1.getId() - o2.getId());
        } else if (choice.equals("2")) {
            myQueue = new PriorityQueue<>((o1, o2) -> o1.getName().compareTo(o2.getName()));
        } else if (choice.equals("3")) {
            myQueue = new PriorityQueue<>((o2, o1) -> o1.getFrequency() - o2.getFrequency());
        } else {
            System.out.println("You entered another symbol! Priority will be for id!");
            myQueue = new PriorityQueue<>((o1, o2) -> o1.getId() - o2.getId());
        }
        for (int i = 0; i < arrayId.length; i++) {
            myQueue.add(new Toy(arrayId[i], names[i], arrayFrequency[i]));
        }
    }

    public Toy getToyProbabilityTheory() {
        int index = probabilityTheory();
        return new Toy(arrayId[index], names[index], arrayFrequency[index]);
    }

    private int probabilityTheory() {
        int result;

        int size = IntStream.of(arrayFrequency).sum();
        int index = random.nextInt(size);
        for (int i = 0; i < arrayFrequency.length; i++) {
            index -= arrayFrequency[i];
            if (index < 0) {
                result = i;
                return result;
            }
        }
        return -1;
    }

    public void saveInFile(Toy toy) throws IOException {
        File file = new File("test.txt");
        FileWriter fw = new FileWriter(file, true);
        fw.write(toy.toString() + '\n');
        fw.close();
    }

    public int[] getArrayId() {
        return arrayId;
    }

    public int[] getArrayFrequency() {
        return arrayFrequency;
    }

    public String[] getNames() {
        return names;
    }


    private void checkResult(int id, String name, int frequency) throws RuntimeException {
        if (id < 1) {
            throw new RuntimeException("Wrong id! ---> " + id);
        }
        if (name.isEmpty()) {
            throw new RuntimeException("Wrong name! Name can't be empty!");
        }
        if (frequency < 0 || frequency >= 100) {
            throw new RuntimeException("Wrong frequency! ---> " + frequency);
        }
    }


    private void checkIdInArray (int id) throws RuntimeException{
        for (int temp: arrayId) {
            if (temp==id) throw new RuntimeException("This id is exist!");
        }
    }


}


