import java.util.Comparator;

public class Toy implements Comparator<Toy> {
    private int id;
    private String name;
    private int frequency;

    public Toy(int id, String name, int frequency) {
        if (id > 0) {
            this.id = id;
        } else {
            throw new RuntimeException("Wrong id!");
        }
        if (!name.isEmpty()) {
            this.name = name;
        } else {
            throw new RuntimeException();
        }
        if (frequency >= 0 && frequency <= 100) {
            this.frequency = frequency;
        } else {
            throw new RuntimeException("Wrong frequency!");
        }
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getFrequency() {
        return frequency;
    }

    @Override
    public int compare(Toy o1, Toy o2) {
        return o1.id - o2.id;
    }

    @Override
    public String toString() {
        return
                "id = " + id +
                        ", name = '" + name + '\'' +
                        ", frequency = " + frequency;
    }
}
