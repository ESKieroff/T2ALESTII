import java.util.Arrays;

public class Box implements Comparable<Box> {
    int[] dimensions;
    int box_id;

    public Box(int[] dimensions, int box_id) {
        this.dimensions = dimensions;
        this.box_id = box_id;
        
        Arrays.sort(this.dimensions); // Ensure dimensions are sorted
    }

    public boolean fitsInside(Box other) {
        for (int i = 0; i < 3; i++) {
            if (this.dimensions[i] >= other.dimensions[i]) {
                return false;
            }
        }
        return true;
    }

    public int getBoxId() {
        return box_id;
    }


    @Override
    public int compareTo(Box other) {
        for (int i = 2; i >= 0; i--) { // Compare dimensions in descending order

            if (this.dimensions[i] != other.dimensions[i]) {
                return other.dimensions[i] - this.dimensions[i];
            }
        }
        return 0;
    }
}
