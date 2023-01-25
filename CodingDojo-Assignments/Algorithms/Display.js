class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}
class LinkedList {
    constructor() {
        this.head = null;
    }
    addFront(val) {
        let new_node = new Node(val);
        if (!this.head) {
            this.head = new_node
            return this;
        }
        new_node.next = this.head;
        this.head = new_node
        return this;
    }
    display() {
        var valuesList = ""; 
        if (this.head == null) {
            return valuesList;
        }
        valuesList += this.head.data; 
        var current = this.head.next;
        while (current != null) {
            valuesList += ", " + current.data; 
            current = current.next; 
        }
        return valuesList;
    }

}

let SLL1 = new LinkedList();
console.log(SLL1.addFront(76)); // Node { data: 76, next: null }
console.log(SLL1.addFront(2)); // Node { data: 2, next: Node { data: 76, next: null } }
console.log(SLL1.display()); //  ", 2, 76"
console.log(SLL1.addFront(11.41)); // Node { data: 11.41, next: Node { data: 2, next: Node { data: 76, next: null } } }
console.log(SLL1.display()); // ", 11.41, 2, 76"
