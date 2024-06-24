import java.io.*;
import java.util.*;

public class Matrioska {
    List<Box> boxes = new ArrayList<>();
    Map<Box, List<Box>> graph = new HashMap<>();

    public static void main(String[] args) throws IOException {
        long startTime = System.currentTimeMillis();

        // Configurar a propriedade de sistema para usar JavaFX
        System.setProperty("org.graphstream.ui", "javafx");

        Matrioska matrioska = new Matrioska();
        matrioska.readBoxesFromFile("teste.txt");
        matrioska.buildGraph();
        List<Box> longestPath = matrioska.findLongestPath();

        long endTime = System.currentTimeMillis();
        long executionTime = endTime - startTime;

        System.out.println("The longest sequence of boxes is: " + longestPath.size());
        System.out.println("Execution time: " + executionTime + " ms");

        matrioska.writeLogFile(longestPath, "log.txt");

        matrioska.exportGraphToDot("graph.dot");

        matrioska.exportLongestPathToDot(longestPath, "longest_path.dot");

    }

    public void readBoxesFromFile(String filename) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(filename));
        String line;
        int id = 1;
        
        while ((line = reader.readLine()) != null) {
            String[] parts = line.split(" ");
            if (parts.length != 3) {
                throw new IllegalArgumentException("Invalid input format: each line must contain exactly 3 integers");
            }
            int[] dimensions = new int[3];
            for (int i = 0; i < 3; i++) {
                try {
                    dimensions[i] = Integer.parseInt(parts[i]);
                } catch (NumberFormatException e) {
                    throw new IllegalArgumentException("Invalid number format in input file", e);
                }
            }
            boxes.add(new Box(dimensions, id++));
        }
        reader.close();
        Collections.sort(boxes); // Sort boxes in descending order
    }

    public void buildGraph() {
        for (Box box : boxes) {
            graph.putIfAbsent(box, new ArrayList<Box>());
            for (Box otherBox : boxes) {
                if (box != otherBox && otherBox.fitsInside(box)) {
                    graph.get(box).add(otherBox);
                }
            }
        }
    }

    public List<Box> findLongestPath() {
        Map<Box, Integer> memo = new HashMap<>();
        Map<Box, Box> predecessor = new HashMap<>();
        int longestPathLength = 0;
        Box endBox = null;

        for (Box box : boxes) {
            int pathLength = dfs(box, memo, predecessor);
            if (pathLength > longestPathLength) {
                longestPathLength = pathLength;
                endBox = box;
            }
        }

        // Reconstruct the longest path
        List<Box> longestPath = new ArrayList<>();
        while (endBox != null) {
            longestPath.add(endBox);
            endBox = predecessor.get(endBox);
        }

        Collections.reverse(longestPath);
        return longestPath;
    }

    private int dfs(Box box, Map<Box, Integer> memo, Map<Box, Box> predecessor) {
        if (memo.containsKey(box)) {
            return memo.get(box);
        }
        int maxLength = 1; // The box itself is counted as a length of 1
        Box bestPredecessor = null;
        for (Box neighbor : graph.get(box)) {
            int length = 1 + dfs(neighbor, memo, predecessor);
            if (length > maxLength) {
                maxLength = length;
                bestPredecessor = neighbor;
            }
        }
        memo.put(box, maxLength);
        if (bestPredecessor != null) {
            predecessor.put(box, bestPredecessor);
        }
        return maxLength;
    }

    public void writeLogFile(List<Box> path, String filename) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(filename));
        for (Box box : path) {
            writer.write(String.format("%03d [%d %d %d]%n", box.getBoxId(), box.dimensions[0], box.dimensions[1], box.dimensions[2]));
        }
        writer.close();
    }

    public void exportLongestPathToDot(List<Box> path, String filename) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(filename));
        writer.write("digraph G {\n");
        for (int i = 0; i < path.size() - 1; i++) {
            writer.write(String.format("  %d -> %d;\n", path.get(i).getBoxId(), path.get(i + 1).getBoxId()));
        }
        writer.write("}\n");
        writer.close();
    }

    public void exportGraphToDot(String filename) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(filename));
        writer.write("digraph G {\n");
        for (Box box : graph.keySet()) {
            for (Box neighbor : graph.get(box)) {
                writer.write(String.format("  %d -> %d;\n", box.getBoxId(), neighbor.getBoxId()));
            }
        }
        writer.write("}\n");
        writer.close();
    }

}
