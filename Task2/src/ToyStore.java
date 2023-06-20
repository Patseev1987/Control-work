import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;


public class ToyStore {
    Queue<Toy> myQueue = new PriorityQueue<>((o1, o2) -> o1.getId()-o2.getId());

    public void put(int id, String name, int frequency) {
        int sum = 0;
        for (Toy toy : myQueue) {
            sum += toy.getFrequency();
        }
        if (sum+frequency<=100) {
            myQueue.add(new Toy(id, name, frequency));
            System.out.println("Toy was added in store.");
        } else {
            System.out.println("You can't enter this frequency! Your frequency should be 0 or less "+(100-sum));
        }
    }

}
