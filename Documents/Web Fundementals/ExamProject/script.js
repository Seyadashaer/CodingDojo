
var clickCount = 0;

function displayAlert() {
    clickCount ++;
    alert("The number of Clicks "+ clickCount)
}

function changeButton(element) {
    element.classList.add("new-style");
}

function returnButton(element) { 
    element.classList.remove("new-style");

}