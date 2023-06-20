import java.util.NoSuchElementException;
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ToyStore ts = new ToyStore();
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < 4; i++) {
           try{
               System.out.println("Enter a id:");
               String str1 = scanner.next();
               int id = Integer.parseInt(str1);
               System.out.println("Enter a name:");
               String name = scanner.next();
               System.out.println("Enter a frequency:");
               String str2= scanner.next();
               int frequency = Integer.parseInt(str2);
               ts.put(id,name,frequency);
           }catch (RuntimeException e){
               System.out.println("You made a mistake ---> "+e.getMessage());
               i--;
           }
        }
    }
}