


var connectionsNumber = document.querySelector("#connections")
var requestsNumber = document.querySelector("#requests")



function editName() {
    var userName = document.querySelector("#user-name")
    userName.innerText = "Mia John"
}

function accept(id) {
    /* Aseel Code review comment var element = document.querySelector(id);
    element.remove();
    requestsNumber.innerText --; */
    ignore(id); 
    connectionsNumber.innerText ++;

}

function ignore(id) {
    var element = document.querySelector(id);
    element.remove(); 
    requestsNumber.innerText --;
}

