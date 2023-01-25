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
        if(!this.head) {
            this.head = new_node;
            return this;
        }
        new_node.next = this.head;
        this.head = new_node;
        return this;
    }
    
    removeFront() {
        // Checking if the list is empty
        if(!this.head) return null;
        // Assigning the head's next node to be the new head
        let new_head = this.head.next;
        this.head = new_head;
        return new_head;
    }
    
    front() {
        // Checking if the list is empty
        if(!this.head) return null;
        // Returning the data of the head node
        return this.head.data;
    }
}    