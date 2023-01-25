class Node {
    constructor(data) { 
        this.data = data;
        this.next = null;
    }
}

class LinkedList { 
    constructor() {
        this.head = null
    }
    length() { 
        let current = this.head
        let count = 0;
        while (current) {
            count ++;
            current = current.next;
        }
        return count;
    }
}

/* the method starts at the head of the list and iterates through each node,
incrementing a count variable for each node. When the end of the list is reached,
the method returns the count variable, which represents the number of nodes in the list. */