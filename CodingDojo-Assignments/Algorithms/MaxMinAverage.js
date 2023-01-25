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

    addFront(value) {
        let new_node = new Node(value);
        if (!this.head) {
            this.head = new_node
            return this;
        }
        new_node.next = this.head;
        this.head = new_node
        return this;
    }

    length() {
        let current = this.head;
        let count = 0;
        while (current) {
            count++;
            current = current.next;
        }
        return count;
    }
    maxMinAvg() {
        let sum = 0;
        let max = this.head.data;
        let min = this.head.data;
        let current = this.head;
        while(current) {
            sum += current.data;
            if(current.data > max) {
                max = current.data;
            }
            else if(current.data < min) {
                min = current.data;
            }
            current = current.next
        }
        return `max: ${max}, min: ${min}, avg: ${sum/this.length()}`
    }

}

let SLL1 = new LinkedList();
SLL1.addFront(16); 
SLL1.addFront(8); 
SLL1.addFront(11); 
SLL1.addFront(22); 
console.log(SLL1.maxMinAvg()); 
