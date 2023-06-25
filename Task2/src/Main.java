import java.io.IOException;
import java.util.NoSuchElementException;
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        ToyStore ts = new ToyStore();
        ts.addToy(4);
        ts.createQueue();
        ts.getInfoAboutList();
        System.out.println("*********************************");
        for (int i = 0; i < 10; i++) {
            ts.saveInFile(ts.getToyProbabilityTheory());
        }
    }
}