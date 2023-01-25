class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor(){
        this.head = null;

    }

    contains(value) {
        let current = this.head;
        while (current) {
            if (current.data === value) {
                return true;
            }
            current = current.next;
        }
        return false;
    }
}

/* the method starts at the head of the list and iterates through each node,
checking if the value of the current node matches the provided value. 
If a match is found, the method returns true.
If the end of the list is reached without finding a match, the method returns false. */