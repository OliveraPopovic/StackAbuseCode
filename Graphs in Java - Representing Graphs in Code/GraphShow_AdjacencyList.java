public class GraphShow_AdjacencyList {
    public static void main(String[] args) {

        Graph_AdjacencyList graph = new Graph_AdjacencyList(true);
        Node a = new Node(0, "A");
        Node b = new Node(1, "B");
        Node c = new Node(2, "C");
        Node d = new Node(3, "D");
        Node e = new Node(4, "E");

        graph.addEdge(a,b);
        graph.addEdge(b,c);
        graph.addEdge(b,d);
        graph.addEdge(c,e);
        graph.addEdge(b,a);

        graph.printEdges();

        System.out.println(graph.hasEdge(a,b));
        System.out.println(graph.hasEdge(d,a));
    }
}
